from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

def registrar_costo(interaction):
    registro = {
        "model": interaction.model,
        "timestamp": interaction.created,
        "input_tokens": interaction.usage.total_input_tokens,
        "output_tokens": interaction.usage.total_output_tokens,
        "thought_tokens": interaction.usage.total_thought_tokens,
        "total_tokens": interaction.usage.total_tokens,
    }
    with open("registro_costos.jsonl", "a",encoding="utf-8") as f:
        json.dump(registro, f)
        f.write("\n")
    

def preguntar(texto:str) -> str:
    api_key=os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise ValueError("GEMINI_API_KEY no está configurada en las variables de entorno.")
    client = genai.Client(api_key= api_key)
    response = client.interactions.create(
        model="gemini-3.5-flash",
        input=texto
    )
    registrar_costo(response)
    return response.output_text


def preguntar_stream(texto: str):
    api_key=os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise ValueError("GEMINI_API_KEY no está configurada en las variables de entorno.")
    client = genai.Client(api_key= api_key)
    stream = client.interactions.create(
        model="gemini-3.5-flash",
        input=texto,
        stream=True
    )
    termino = False
    for event in stream:
        if event.event_type == 'step.delta' and event.delta.type == 'text':
            yield event.delta.text
        if event.event_type == 'interaction.completed':
            termino = True
            registrar_costo(event.interaction)
    if not termino:
        raise RuntimeError("La interacción no se completó correctamente.")
    

        
    
    