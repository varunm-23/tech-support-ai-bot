from langchain_community.document_loaders import PyPDFLoader
import os


class PDFLoader:
    """
    Loads the Upwork API documentation.
    """

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def load_pdf(self):
        """
        Load PDF and return LangChain Document objects.
        """
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path}"
            )

        loader = PyPDFLoader(self.pdf_path)

        documents = loader.load()

        return documents

    def get_full_text(self):
        """
        Combine all pages into a single string.
        """
        docs = self.load_pdf()

        text = "\n".join(doc.page_content for doc in docs)

        return text