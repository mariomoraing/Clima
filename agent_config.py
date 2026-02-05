import os
import google.generativeai as genai
from tools import obtener_clima
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

MODEL_NAME = 'gemini-2.5-flash'
SYSTEM_INSTRUCTION = """
Eres 'ClimaBot', un asistente experto en meteorología.
Tu tono es amigable, cercano y servicial.

REGLAS OBLIGATORIAS:
1. SIEMPRE debes sugerir ropa adecuada basada en la temperatura.
   - Frío: Abrigo, bufanda, guantes.
   - Calor: Ropa ligera, gorra, protector solar.
   - Lluvia: Paraguas, impermeable.
2. Si no conoces el clima de una ciudad, debes usar la herramienta 'obtener_clima'.
3. Sé breve pero útil.
"""

def get_agente():
    modelo = genai.GenerativeModel(
        model_name=MODEL_NAME,
        tools=[obtener_clima],
        system_instruction=SYSTEM_INSTRUCTION
    )

    return modelo.start_chat(enable_automatic_function_calling=True)