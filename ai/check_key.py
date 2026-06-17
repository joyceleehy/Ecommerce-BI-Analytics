from dotenv import load_dotenv
import os

load_dotenv()
k = os.getenv("GEMINI_API_KEY")
print("Key found:", bool(k))
print("Length:", len(k) if k else 0)