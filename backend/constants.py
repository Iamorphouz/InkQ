from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = "0.0.0.0"   # 'localhost'
PORT = '8000'
ENV = 'prod'  # 'dev' or 'prod'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")