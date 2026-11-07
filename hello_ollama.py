from ollama import chat
from pydantic import BaseModel

# 1. Definimos la estructura de datos que queremos que devuelva la IA
# (Por ejemplo, una tarjeta de presentación con el nombre y la edad)
class Persona(BaseModel):
    nombre: str
    edad: int
    profesion: str

# 2. Hacemos la consulta a Ollama especificando el modelo llama3.2:1b
response = chat(
    model='llama3.2:1b',  # <-- Aquí se especifica el modelo exacto
    messages=[
        {
            'role': 'user',
            'content': 'Extrae la información del siguiente texto: Carlos tiene 28 años y trabaja como programador.',
        },
    ],
    # Le indicamos a Pydantic que valide y estructure la salida JSON
    format=Persona.model_json_schema(), 
)

# 3. Validamos e imprimimos la respuesta con Pydantic
datos_extraidos = Persona.model_validate_json(response['message']['content'])

print("Nombre:", datos_extraidos.nombre)
print("Edad:", datos_extraidos.edad)
print("Profesión:", datos_extraidos.profesion)