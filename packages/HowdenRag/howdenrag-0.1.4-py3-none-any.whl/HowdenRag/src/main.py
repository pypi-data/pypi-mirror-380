from dotenv import load_dotenv
from src.parser import LlamaMarkdownParser
from src.chunking import chunk_text
from src.chroma_storage import store_in_chroma
from src.answer_generation import interactive_query_loop
from src.config_model import load_and_validate_config, stable_config_hash, Config
from src.rerank import LLMReranker, BGEReranker
from src.clients.openai_client import OpenAIClient
from src.services.llm_service import LLMService
from src.determine_date import determine_date_from_content
from pathlib import Path
import os
import hashlib
import re
from datetime import datetime
from PyPDF2 import PdfMerger
from src.split_document import split_pdf_by_bookmarks


load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

def save_markdown_to_md_file(markdown_content: str, md_path: Path) -> None:
    with md_path.open('w', encoding='utf-8') as file:
        file.write(markdown_content)


def parse_pdf_to_markdown(config: Config, input_path: Path, output_path: Path) -> str:
    output_path.mkdir(exist_ok=True)
    parser = LlamaMarkdownParser("CLAIMS-RAG-TOKEN", {"llama_parser": {"premium_mode": config.llama_parser.premium_mode}})
    for document in [f for f in Path(input_path).iterdir() if f.is_file()]:
        filename = output_path / Path(document.name).with_suffix(".md")
        markdown = parser.parse_file(document)
        save_markdown_to_md_file(markdown, filename)
    

def store_chunks(chunks, file_path: Path, name: str):
    for idx, chunk in enumerate(chunks):
        name = Path(name)
        name_with_out_suffix = name.stem  # '001.00 - IND - Anmeldelse ulykke'
        suffix = name.suffix  # '.md'
        corrected_name = Path(f"{name_with_out_suffix}_{chunk['page_number']}_{idx}{suffix}")
        path_name = file_path / corrected_name
        with path_name.open('w', encoding='utf-8') as file:
            file.write(chunk['chunk'])



def make_valid_chromadb_name(input_string: str) -> str:
    no_spaces = input_string.replace(' ', '')
    sanitized = re.sub(r'[^a-zA-Z0-9._-]', '_', no_spaces.strip())
    sanitized = re.sub(r'_+', '_', sanitized)

    if not re.match(r'^[a-zA-Z0-9]', sanitized):
        sanitized = f'a{sanitized}'

    if not re.match(r'[a-zA-Z0-9]$', sanitized):
        sanitized = f'{sanitized}'

    if not (3 <= len(sanitized) <= 512):
        hash_suffix = hashlib.sha256(input_string.encode()).hexdigest()[:8]
        sanitized = f'{sanitized[:503]}_{hash_suffix}'
        if len(sanitized) < 3:
            sanitized = f'val_{hash_suffix}'

    return sanitized

def correct_ocr_errors_in_dates_and_numbers(text: str) -> str:
    def replace_ocr_errors_in_match(match: re.Match) -> str:
        ocr_corrections = str.maketrans({
            'z': '2',
            'Z': '2',
            'O': '0',
            'Q': '0',
            'I': '1',
            'l': '1',
            'S': '5',
            'B': '8',
            'G': '6',
        })
        return match.group(0).translate(ocr_corrections)

    # Replace in patterns that look like dates: e.g. YYYY-MM-DD, DD-MM-YYYY, etc.
    date_like_patterns = [
        r'\b[\dOQIlzZSBG]{4}[-/.][\dOQIlzZSBG]{2}[-/.][\dOQIlzZSBG]{2}\b',   # 2023-06-12, OOI2-IZ-IS, z0z3-0l-l2
        r'\b[\dOQIlzZSBG]{2}[-/.][\dOQIlzZSBG]{2}[-/.][\dOQIlzZSBG]{4}\b',   # 12-06-2023, etc.
        r'\b[\dOQIlzZSBG]{2}[-/.][\dOQIlzZSBG]{2}[-/.][\dOQIlzZSBG]{2}\b',   # 12-06-23
    ]
    for pattern in date_like_patterns:
        text = re.sub(pattern, replace_ocr_errors_in_match, text)

    # Replace in patterns that look like numbers (with 3+ chars, to avoid short words)
    text = re.sub(r'\b[\dOQIlzZSBG]{3,}\b', replace_ocr_errors_in_match, text)

    return text

def save_markdown_with_date(llm_service: LLMService, config: Config, input_path: Path, output_path: Path):
    output_path.mkdir(exist_ok=True)

    for file_path_markdown in [f for f in Path(input_path).iterdir() if f.is_file()]:
        markdown_text: str = file_path_markdown.read_text(encoding="utf-8")
        corrected_markdown = correct_ocr_errors_in_dates_and_numbers(markdown_text)
        date = determine_date_from_content(llm_service=llm_service, data=corrected_markdown, model=config.query.model)
        corrected_date = output_path /  f"{date}_{file_path_markdown.name}"
        with corrected_date.open('w', encoding='utf-8') as file:
            file.write(corrected_markdown)

def parse_date(file_path: Path) -> datetime:
    try: 
        file_name = file_path.stem 
        date_str = file_name.split('_')[0]  
        format = "%Y-%m-%d"
        date = datetime.strptime(date_str, format)
        return date
    except Exception:
        return datetime.now()



def merge_pdfs_chronologically(input_path_markdown: Path, input_path_pdf: Path, output_path: Path, output_filename_pdf: str):
    output_path.mkdir(exist_ok=True)
    date_prefix = re.compile(r'^\d{4}-\d{2}-\d{2}_(.+)')
    merger = PdfMerger()
    sorted_files = sorted(input_path_markdown.iterdir(), key=parse_date)
    

    for file_path in sorted_files:
        pdf_file_stem = date_prefix.match(file_path.stem)
        if not pdf_file_stem:
            print(f"Skipping {file_path.name} as it does not match the date format.")
            continue
        pdf_file_name = f"{pdf_file_stem.group(1)}.pdf"
        print(f"Processing {file_path.name} with corresponding PDF {pdf_file_name}")
        pdf_file_path = input_path_pdf / pdf_file_name
        if pdf_file_path.is_file():
            merger.append(pdf_file_path)
    merged_pdf_file_path = output_path / output_filename_pdf.split('/')[-1]
    merger.write(merged_pdf_file_path)
    merger.close()
    print(f"Merged PDF saved to {merged_pdf_file_path}")

def main():
    
    config: Config = load_and_validate_config("./config.toml")
    openai_client = OpenAIClient(model=config.query.model)
    llm_service = LLMService(client=openai_client)

    hashed_value = stable_config_hash(config)
    print(hashed_value)
    path_hash = Path(__file__).resolve().parent / "../.data" / Path(config.input.pdf_path).stem / hashed_value
    path_hash.mkdir(exist_ok=True, parents=True)
    config.write_to_json_file(str(path_hash / "config.json"))
    input_path = config.input.pdf_path

    output_dir_pdf = path_hash / "landing"
    if config.input.split and not output_dir_pdf.exists():
        output_dir_pdf.mkdir(exist_ok=True)
        split_pdf_by_bookmarks(Path(input_path), output_dir_pdf)
    else:
        print("landing folder already exists")

    output_dir_markdown = path_hash / "markdown"
    if not output_dir_markdown.exists():
        parse_pdf_to_markdown(config, output_dir_pdf, output_dir_markdown)
    else:
        print("Markdown folder already exists")


    output_dir_markdown_date = path_hash / "corrected_file_with_date"
    if not output_dir_markdown_date.exists(): 
        save_markdown_with_date(llm_service, config, output_dir_markdown, output_dir_markdown_date)
    else: 
        print("corrected_file_with_date folder already exists")    


    output_dir_chronological_pdf = path_hash / "chronological_pdf"
    if not output_dir_chronological_pdf.exists():
        merge_pdfs_chronologically(output_dir_markdown_date, output_dir_pdf, output_dir_chronological_pdf, config.input.pdf_path)
    else:
        print("chronological_pdf folder already exists")

    output_dir_chunks = path_hash / "chunks"
    if not output_dir_chunks.exists():
        output_dir_chunks.mkdir(exist_ok=True)
        for file_path_markdown in [f for f in Path(output_dir_markdown).iterdir() if f.is_file()]:
            print(file_path_markdown)
            markdown_text: str = file_path_markdown.read_text(encoding="utf-8")
            chunks = chunk_text(markdown_text, config.embedding.model, config.embedding.chunk_size, config.embedding.chunk_overlap)
            store_chunks(chunks, output_dir_chunks, str(file_path_markdown.name))
    else:
        print("chunks folder already exists")

    collection_name = make_valid_chromadb_name(f"{hashed_value}_{Path(input_path).name}")
    db_dir = path_hash / Path(input_path).stem
    print(f"Database directory: {db_dir}")
    print(f"Collection name: {collection_name}")
    if not db_dir.exists():
    #if not collection_exists(str(db_dir), collection_name):
        db_dir.mkdir(exist_ok=True)
        for file_path_chunk in [f for f in Path(output_dir_chunks).iterdir() if f.is_file()]:
            ids = make_valid_chromadb_name(file_path_chunk.name)
            print(file_path_chunk)
            chunk = file_path_chunk.read_text(encoding="utf-8")
            page_number = str(file_path_chunk.stem.split('_')[-2])  
            embeddings = llm_service.get_embeddings(chunk, config.embedding.model)
            store_in_chroma(chunk, embeddings, str(db_dir), collection_name, ids=ids, page_numbers=int(page_number))
    else:
        print(f"ℹ️ Skipping embedding — collection '{collection_name}' already exists in {db_dir}")

    reranker = LLMReranker(llm_service=llm_service, model=config.query.model)
    interactive_query_loop(config, str(db_dir), collection_name, llm_service, reranker)

if __name__ == "__main__":
    main()