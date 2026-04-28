from src.ingestion import ingest_documents
from src.retriever import FAISSRetriever
from src.generator import LLMGenerator

def main():
    # Load and embed documents
    docs = ingest_documents("data/sample_docs/")
    retriever = FAISSRetriever(docs)
    generator = LLMGenerator()

    query = "What are the key findings?"
    context = retriever.retrieve(query, top_k=3)
    answer = generator.generate(query, context)
    print(answer)

if __name__ == "__main__":
    main()
