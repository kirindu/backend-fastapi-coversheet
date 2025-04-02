from fastapi import APIRouter, status, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse, StreamingResponse
import os
import shutil
from uuid import uuid4

api = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)



@api.post("/upload/")
async def upload_image(
    nombre: str = Form(...),
    direccion: str = Form(...),
    imagen: UploadFile = File(...)
):
    try:
        # Crear nombre único para el archivo
        filename = f"{uuid4().hex}_{imagen.filename}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Guardar archivo en disco
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(imagen.file, buffer)

        return JSONResponse(
            status_code=200,
            content={
                "message": "Archivo subido correctamente",
                "nombre": nombre,
                "direccion": direccion,
                "filename": filename,
                "filepath": file_path
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )