
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


llm = llama_index.llms.llama_cpp.LlamaCPP( 
    model_kwargs={"n_gpu_layers": 1}, 
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





# ================== Querying ================== #
# set up query engine
query_engine = index.as_query_engine()

# query_engine = index.as_query_engine()
response = query_engine.query("Who are the authors of this paper?")
print(response)