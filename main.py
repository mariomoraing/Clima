from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_config import get_agente

# --- CONFIGURACIÓN DE FASTAPI ---
app = FastAPI(title="Agente de IA para .NET")


class Consulta(BaseModel):
    mensaje: str

@app.post("/preguntar")
async def chat_handler(consulta: Consulta):
    try:
        agente = get_agente()
        respuesta = agente.send_message(consulta.mensaje)
        return {
            "respuesta": respuesta.text,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

