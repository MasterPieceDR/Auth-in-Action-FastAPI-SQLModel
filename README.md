# Auth-in-Action-FastAPI-SQLModel

API REST mínima con **FastAPI** y **SQLModel** para demostrar un proceso simple de login contra una base de datos embebida (definida en el código).

El objetivo es comprender la estructura básica de una API de autenticación sin usar tokens obligatorios, manteniéndolo lo más simple posible.

---

##  Requisitos

- Python 3.9 o superior  
- Entorno virtual (`venv`)  
- Dependencias de `requirements.txt`

---

##  Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MasterPieceDR/Auth-in-Action-FastAPI-SQLModel.git
   cd Auth-in-Action-FastAPI-SQLModel
Crear y activar un entorno virtual:

Windows (PowerShell):

bash
Copiar código
python -m venv venv
venv\Scripts\activate
Linux / MacOS:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
 Ejecución del servidor
Con el entorno virtual activado, ejecutar:

bash
Copiar código
uvicorn main:app --reload
Esto levantará el servidor en:
 http://127.0.0.1:8000

 Documentación automática
FastAPI genera documentación interactiva:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

 Endpoints principales
GET /
Verifica que la API está funcionando.

POST /login
Permite autenticar un usuario con username y password.

Ejemplo de body JSON:

json
Copiar código
{
  "username": "alice",
  "password": "123"
}
Respuesta esperada:

json
Copiar código
{
  "ok": true,
  "msg": "Bienvenido alice"
}
 Estructura básica del proyecto
lua
Copiar código
Auth-in-Action-FastAPI-SQLModel/
│-- main.py
│-- requirements.txt
│-- .gitignore
│-- README.md
✍️ Autor: Diego Ruiz (MasterPieceDR)
