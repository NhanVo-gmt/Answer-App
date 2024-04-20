from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain.document_loaders.directory import DirectoryLoader
from langchain.llms.openai import OpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_param

client = MongoClient(key_param.mongo_url)
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

loader = DirectoryLoader('./sample_files', glob="./*.txt", show_progress=True)
data = loader.load()

embeddings = OpenAIEmbeddings(openai_api_key=key_param.openai_key)
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection = collection)
