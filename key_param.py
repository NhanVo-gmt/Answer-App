import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_KEY")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_url = f"mongodb+srv://tonynhanvo:{mongo_password}@cluster0.yuaggbs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"