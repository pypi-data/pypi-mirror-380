from typing import List
import tiktoken
import re 

def chunk_text(text: str, model: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    tokenizer = tiktoken.encoding_for_model(model)
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    last_page = 1
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        text_chunk = tokenizer.decode(chunk_tokens)
        page_numbers = re.findall(r'<--PAGE_NUMBER\s+(\d+)-->', text_chunk)
       
        page_number = int(page_numbers[0]) if page_numbers else last_page
        last_page = int(page_numbers[-1]) + 1 if page_numbers else last_page
        chunks.append({"chunk": text_chunk, "page_number": page_number})
        start += chunk_size - chunk_overlap
    
    return chunks

def count_tokens(text: str, model: str) -> int:
    return len(tiktoken.encoding_for_model(model).encode(text))