import chromadb
from typing import List, Tuple
from chromadb.errors import NotFoundError

class DocumentMatch:
    def __init__(self, document: str, doc_id: str, chroma_score: float, page_number: int = None):
        self.document = document
        self.doc_id = doc_id
        self.chroma_score = chroma_score
        self.page_number = page_number

def count_documents_in_collection(db_dir: str, collection_name: str) -> int:
    client = chromadb.PersistentClient(path=db_dir)
    collection = client.get_collection(name=collection_name)
    return collection.count()


def store_in_chroma(chunks: List[str], embeddings: List[float], db_dir: str, collection_name: str, ids, page_numbers):
    client = chromadb.PersistentClient(path=db_dir)
    collection = client.get_or_create_collection(name=collection_name)

    collection.add(documents=chunks, embeddings=embeddings, ids=ids, metadatas={"page_number": page_numbers})

import re
from unidecode import unidecode

def sanitise_title_for_chroma_db(title: str) -> str:
    ascii_normalized = unidecode(title)
    lowercase_title = ascii_normalized.lower()
    alphanumeric_with_underscores = re.sub(r"[^a-z0-9]+", "_", lowercase_title)
    trimmed_title = alphanumeric_with_underscores.strip("_")
    return trimmed_title[:100]

def cosine_similarity_filter(distance: float) -> float:
    """
    Filters document-distance pairs based on cosine similarity.

    ChromaDB returns cosine distance, calculated as:
        cosine_distance = 1.0 - cosine_similarity

    Cosine similarity ranges from:
        +1.0 → perfect match
         0.0 → no similarity (orthogonal)
        -1.0 → completely opposite direction

    Since embedding vectors from modern models (e.g., OpenAI, BERT) usually lie in a constrained space,
    distances typically fall in the range [0.0, 1.0].

    """

    return 1.0 - distance


def query_chroma(
        query_embedding: List[float],
        db_dir: str,
        collection_name: str,
        method: str,
        threshold: float,
) -> List[DocumentMatch]:
    """
    Queries a ChromaDB collection using a given embedding and filters results by similarity method.

    Parameters:
        query_embedding (List[float]): The embedding vector for the query.
        db_dir (str): Path to the ChromaDB directory.
        collection_name (str): Name of the collection to query.
        method (MatchingMethod): Similarity method to use for filtering. supports "cosine_similarity".
        threshold (float): Minimum similarity to include a document.

    Returns:
        List[Tuple[str, str]]: Filtered list of (document, id) tuples.
    """
    client = chromadb.PersistentClient(path=db_dir)
    collection = client.get_collection(name=collection_name)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=100,
        include=["documents", "distances", "metadatas"]
    )

    raw_matches = [DocumentMatch(document=doc, 
                                 doc_id=doc_id, 
                                 chroma_score=score, 
                                 page_number=page_number["page_number"]) 
                                               for doc, 
                                                   doc_id, 
                                                   score, 
                                                   page_number in zip(results["documents"][0], 
                                                                      results["ids"][0], 
                                                                      results["distances"][0], 
                                                                      results["metadatas"][0])
                ]

    if method == "cosine_similarity":
        filtered = [match for match in raw_matches if cosine_similarity_filter(match.chroma_score) >= threshold]
    elif method == "none":
        filtered = raw_matches
    else:
        raise ValueError(f"Unknown matching method: {method}")

    return filtered

import chromadb.errors
def collection_exists(db_dir: str, collection_name: str) -> bool:
    client = chromadb.PersistentClient(path=db_dir)
    try:
        client.get_collection(name=collection_name)
        return True
    except chromadb.errors.CollectionNotFoundError:
        return False