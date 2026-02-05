import os
import requests

from dotenv import load_dotenv
load_dotenv()

def obtener_clima(ciudad: str):
    """
    Consulta el clima real usando OpenWeatherMap.
    Argumentos:
        ciudad: Nombre de la ciudad (ej: 'Santiago', 'Concepción, CL').
    """
    api_key = os.getenv("WEATHER_API_KEY")

    if "," not in ciudad:
        ciudad = f"{ciudad},CL"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            humedad = data['main']['humidity']
            return f"En {data['name']} hace {temp}°C con {desc} y una humedad del {humedad}%."
        else:
            return f"No pude encontrar el clima para '{ciudad}'. Error: {data.get('message', 'desconocido')}"
    except Exception as e:
        return f"Error de conexión: {str(e)}"
