import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# DeepInfra Configuration
DEEPINFRA_API_KEY = os.getenv("DEEPINFRA_API_KEY")
MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

# MODEL_NAME = os.getenv("MODEL_NAME")

# API Endpoint
API_URL = "https://api.deepinfra.com/v1/openai/chat/completions"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Vector Database Directory
CHROMA_DB_DIR = "db/chroma"

# Chunk Configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50