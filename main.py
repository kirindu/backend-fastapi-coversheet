from fastapi import FastAPI
from api import api

app = FastAPI()

# Configuracion para el docs
app.title = "Rest-Api CoverSheet"
app.version = "1.0.0"

app.include_router(api)

