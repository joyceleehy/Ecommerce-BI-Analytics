import os
from dotenv import load_dotenv
from google import genai

# load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# test call (IMPORTANT: use 1.5 flash first)
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Say hello in one short sentence"
)

print(response.text)
