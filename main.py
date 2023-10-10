
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt


import llama_index.llms.llama_cpp

from langchain.embeddings import HuggingFaceEmbeddings

import config

# model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin"

# llm = llama_index.llms.llama_cpp.LlamaCPP( model_url= model_url,
#                                           model_kwargs={"n_gpu_layers": 1})

llm = llama_index.llms.llama_cpp.LlamaCPP( 
    # model_url= config.RETRIVAL_MODEL_URL, 
    model_kwargs={"n_gpu_layers": 1}, 
    # model_path=config.RETRIVAL_MODEL_URL
    )

embed_model = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_URL)

# create a service context
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)

# load documents
documents = SimpleDirectoryReader(
    config.KNOWLEDGE_BASE_PATH
).load_data()

# create vector store index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)
# set up query engine
query_engine = index.as_query_engine()

# query_engine = index.as_query_engine()
response = query_engine.query("Who are the authors of this paper?")
print(response)