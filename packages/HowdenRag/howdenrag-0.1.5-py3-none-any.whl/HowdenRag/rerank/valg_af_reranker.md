# Valg af reranker


## Mulige valg
*Tabellen er baseret på information fra [1] og [2].*

| Model         | Type         | Ydeevne   | Pris      | Eksempel                                 |
|---------------|--------------|-----------|-----------|-------------------------------------------|
| Cross encoder | Open source  | Fremragende | Mellem    | BGE, sentence, transformers, Mixedbread   |
| Multi-vektor  | Open source  | God       | Lav       | ColBERT                                   |
| LLM           | Open source  | Fremragende | Høj      | RankZephyr, RankT5                        |
| LLM API       | Privat       | Bedst     | Meget høj | GPT, Claude                               |
| Rerank API    | Privat       | Fremragende | Mellem   | Cohere, Mixedbread, Jina                  |


## Valg
Baseret på ovenstående resultater og (begrænsede tests) er der lavet to reranker funktioner: 
1. En open source cross encoder model fra Beijing Academy of Artificial Intelligence
    - Denne er valgt for sin kvalitet især på multilinguale (læs: danske) datasæt og relativt lave pris
2. En funktion der bruger API-kald til OpenAI
    - Denne er valgt fordi den har den højeste kvalitet af alle undersøgte modeller trods den lidt højere pris 

Som udgangspunkt bruges OpenAI-modellen som reranker


**Kilder:**  
[1] [galileo.ai: Mastering RAG: How to Select a Reranking Model](https://galileo.ai/blog/mastering-rag-how-to-select-a-reranking-model)  
[2] [medium.com: From Good to Great: Using Reranking Models to Perfect Your RAGs](https://medium.com/data-reply-it-datatech/from-good-to-great-using-reranking-models-to-perfect-your-rags-a5e73a4d2815)

