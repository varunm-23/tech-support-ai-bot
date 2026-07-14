# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE
from config import CHUNK_OVERLAP


class DocumentChunker:
    """
    Splits the document into overlapping chunks.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_text(self, text):
        """
        Split plain text into chunks.
        """
        return self.splitter.split_text(text)