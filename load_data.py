import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain.document_loaders.directory import DirectoryLoader
from langchain.llms.openai import OpenAI
import gradio as gr
from gradio.themes.base import Base
