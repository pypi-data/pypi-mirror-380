from src.chunking import count_tokens
from src.chroma_storage import DocumentMatch
from FlagEmbedding import FlagReranker
from typing import List
from abc import ABC, abstractmethod
from src.services.llm_service import LLMService


class Reranker(ABC):
    @abstractmethod
    def rerank_documents(self, query: str, initial_chunks: List[DocumentMatch]) -> list[DocumentMatch]:
        pass

class LLMReranker(Reranker):
    def __init__(self, llm_service: LLMService, model: str = "gpt-4o"):
        self.llm_service = llm_service
        self.model = model
    def rerank_documents(self, query: str, initial_chunks: List[DocumentMatch]) -> list[DocumentMatch]:
        return rerank_documents_llm(llm_service=self.llm_service, query=query, documents=initial_chunks, model=self.model)

class BGEReranker(Reranker):
    def __init__(self, model):
        self.reranker = FlagReranker(model, use_fp16=True)
    def rerank_documents(self, query: str, initial_chunks: List[DocumentMatch]) -> list[DocumentMatch]:
        return rerank_documents_bge(self.reranker, query, initial_chunks)


def filter_with_gpt(query: str, chunks: list[str], model: str, openai_client) -> list[str]:
    prompt = build_prompt(query, chunks)
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Du er en hjælpsom AI, der assisterer med juridiske dokumenter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    try:
        index_list = eval(response.choices[0].message.content.strip())
        return [chunks[i] for i in index_list if 0 <= i < len(chunks)]
    except Exception:
        return []

def rerank_chunks_with_filter(query: str, chunks: list[str], model: str, max_token: int, openai_client) -> list[str]:
    # Fast path: if it's already within the limit, return as-is
    full_prompt = build_prompt(query, chunks)
    if count_tokens(full_prompt, model) <= max_token:
        return filter_with_gpt(query, chunks, model, openai_client)

    # Else: reduce input size in batches and merge results
    selected = []
    batch = []
    current_tokens = count_tokens(build_prompt(query, []), model)  # base overhead

    for chunk in chunks:
        chunk_tokens = count_tokens(chunk, model)
        if current_tokens + chunk_tokens > max_token:
            if batch:
                selected += filter_with_gpt(query, batch, model, openai_client)
                batch = []
                current_tokens = count_tokens(build_prompt(query, []), model)
        batch.append(chunk)
        current_tokens += chunk_tokens

    if batch:
        selected += filter_with_gpt(query, batch, model, openai_client)

    # Deduplicate and preserve order
    return [chunk for i, chunk in enumerate(chunks) if chunk in selected]

def build_prompt(query: str, chunks: list[str]) -> str:
    chunk_lines = "\n".join(f"[{i}]: {chunk}" for i, chunk in enumerate(chunks))
    return (f"Spørgsmål: {query}\n\n {chunk_lines}\n Svar med en Python-liste med indeksene på relevante afsnit."
    )


def rerank_documents_bge(reranker: FlagReranker, query: str, documents: list[DocumentMatch]) -> list[DocumentMatch]:

    relevant_documents: list[DocumentMatch] = []
    
    scores = reranker.compute_score([[query, document.document] for document in documents])

    scored_chunks = []
    for document, score in zip(documents, scores):
        
        if score >= 4.0:  # Adjust threshold as needed
            print(f"Document {document.doc_id} scored {score} - Adding to relevant_documents\n")

            relevant_documents.append(document)
        else: 
            print(f"Document {document.doc_id} scored {score} - Not relevant enough\n")
        scored_chunks.append((document, score))

    scored_chunks.sort(key=lambda x: x[1], reverse=True)

    return [document for document, score in scored_chunks]


def rerank_documents_llm(
        llm_service: LLMService, query: str, documents: list[DocumentMatch], model: str
) -> list[DocumentMatch]:
    def format_prompt(query: str, doc: str) -> str:
        return (
            f"Given the query:\n\"{query}\"\n\n"
            f"How relevant is the following document on a scale from 1 (irrelevant) to 10 (highly relevant)?\n\n"
            f"output only the number and nothing else"
            f"Document:\n\"\"\"\n{doc}\n\"\"\""
        )

    relevant_documents: list[DocumentMatch] = []
    for document in documents:
        response = llm_service.get_response(
            model=model,
            messages=[
                {"role": "system", "content": "You are a document relevance scoring engine."},
                {"role": "user", "content": format_prompt(query, document.document)},
            ],
            max_tokens=5,
        )

        content = response.choices[0].message.content.strip()

        try:
            score = float(content.split()[0])
        except (ValueError, IndexError):
            score = 0.0

        if score >= 8.0:
            relevant_documents.append(document)

    return relevant_documents

