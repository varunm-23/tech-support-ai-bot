from langchain_chroma import Chroma

from config import CHROMA_DB_DIR


class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create_vector_db(self, chunks):

        db = Chroma.from_texts(
            texts=chunks,
            embedding=self.embedding_model,
            persist_directory=CHROMA_DB_DIR
        )

        return db