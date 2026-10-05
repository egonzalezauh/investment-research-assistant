from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def preguntar(texto:str) -> str:
    api_key=os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise ValueError("GEMINI_API_KEY no está configurada en las variables de entorno.")
    client = genai.Client(api_key= api_key)
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=texto
    )
    return response.output_text



