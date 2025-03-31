from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import re
import os
from google.cloud import firestore
from google.oauth2 import service_account

app = FastAPI()

# Ruta al archivo JSON de la clave
ruta_clave = os.path.join(os.path.dirname(__file__),  "pf25-lucas-rocha-ea924b8dcbc4.json")

# Conectamos con Firestore usando las credenciales
credenciales = service_account.Credentials.from_service_account_file(ruta_clave)
db = firestore.Client(credentials=credenciales)

# Ruta de prueba
@app.get("/")
def leer_inicio():
    return {"mensaje": "FastAPI está funcionando 😎"}

# Modelo de datos para el formulario
class Registro(BaseModel):
    nombre: str
    dni: str
    email: EmailStr
    fecha_nacimiento: str

# Validación del DNI o NIE
def validar_dni_nie(dni: str):
    dni = dni.strip().upper()
    
    patron_dni = r'^\d{8}[A-Z]$'
    patron_nie = r'^[XYZ]\d{7}[A-Z]$'

    if not re.match(patron_dni, dni) and not re.match(patron_nie, dni):
        raise HTTPException(status_code=400, detail="DNI/NIE inválido")

# Endpoint para registrar usuarios
@app.post("/registro")
def registrar_usuario(datos: Registro):
    validar_dni_nie(datos.dni)  # Validamos el DNI o NIE

    # Guardamos en Firestore
    doc_ref = db.collection("usuarios").document()
    doc_ref.set({
        "nombre": datos.nombre,
        "dni": datos.dni,
        "email": datos.email,
        "fecha_nacimiento": datos.fecha_nacimiento
    })

    return {
        "mensaje": "Registro recibido correctamente",
        "datos": datos
    }
from typing import List

@app.get("/registros")
def listar_usuarios():
    usuarios_ref = db.collection("usuarios").stream()
    usuarios = []

    for doc in usuarios_ref:
        usuario = doc.to_dict()
        usuario["id"] = doc.id  # Añade el ID del documento si quieres
        usuarios.append(usuario)

    return usuarios

