from langchain_chroma import Chroma

from config import CHROMA_DB_DIR
from config import EMBEDDING_MODEL

from langchain_huggingface import HuggingFaceEmbeddings


class Retriever:

    def __init__(self):

        embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        self.db = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=embedding
        )

    def retrieve(self, query, k=3):

        docs = self.db.similarity_search(
            query=query,
            k=k
        )

        return docs