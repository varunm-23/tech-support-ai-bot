import streamlit as st

from rag.retriever import Retriever
from rag.generator import LLMGenerator

# -----------------------------
# Streamlit Configuration
# -----------------------------
st.set_page_config(
    page_title="Upwork Technical Support AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Upwork Technical Support AI")
st.write("Ask questions about the Upwork API documentation.")

# -----------------------------
# Load Backend
# -----------------------------
@st.cache_resource
def load_backend():
    retriever = Retriever()
    generator = LLMGenerator()
    return retriever, generator

retriever, generator = load_backend()

# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching documentation..."):

        docs = retriever.retrieve(question)

        context = [
            doc.page_content
            for doc in docs
        ]

        answer, latency = generator.generate(
            question,
            context
        )

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for i, doc in enumerate(docs, start=1):

        with st.expander(f"Source {i}"):

            st.write(doc.page_content)

    st.subheader("Latency")

    st.success(f"{latency} seconds")