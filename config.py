# get string from .env file
from dotenv import load_dotenv
import os


load_dotenv()

RETRIVAL_MODEL_URL = os.getenv("RETRIVAL_MODEL_URL")
EMBEDDING_MODEL_URL = os.getenv("EMBEDDING_MODEL_URL")
KNOWLEDGE_BASE_PATH = os.getenv("KNOWLEDGE_BASE_PATH")

x=0


