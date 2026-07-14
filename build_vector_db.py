import os
import shutil

from ingestion.loader import PDFLoader
from ingestion.chunker import DocumentChunker
from ingestion.embeddings import EmbeddingModel
from ingestion.vector_store import VectorStore
from config import CHROMA_DB_DIR


def main():

    print("=" * 60)
    print("Building Vector Database")
    print("=" * 60)

    # Load PDF
    loader = PDFLoader("data/Upwork_API.pdf")
    text = loader.get_full_text()

    print(f"Loaded Characters : {len(text)}")

    # Chunking
    chunker = DocumentChunker()
    chunks = chunker.split_text(text)

    print(f"Chunks Created : {len(chunks)}")

    # Remove old database
    if os.path.exists(CHROMA_DB_DIR):
        shutil.rmtree(CHROMA_DB_DIR)

    # Embeddings
    embedding = EmbeddingModel().get_embedding()

    # Create Vector DB
    vector_db = VectorStore(embedding)

    vector_db.create_vector_db(chunks)

    print("\nVector Database Created Successfully!")
    print(f"Saved at : {CHROMA_DB_DIR}")


if __name__ == "__main__":
    main()