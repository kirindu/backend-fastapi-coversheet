from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
import os

from contextlib import asynccontextmanager

from config.database import ping_database
from config.database import client


from routes.route_routes import router as route_router
from routes.truck_routes import router as truck_router
from routes.material_routes import router as material_router
from routes.driver_routes import router as driver_router
from routes.landfill_routes import router as landfill_router

from routes.coversheet_routes import router as coversheet_router
from routes.sparetruckinfo_routes import router as sparetruckinfo_router
from routes.downtime_routes import router as downtime_router
from routes.load_routes import router as load_router

from routes.user_routes import router as user_router
from routes.email_routes import router as email_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    await ping_database()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    print("Hola desde el middleware")
    return response

# Incluimos los orígenes permitidos en la configuración de CORS
# Si quiere permitir todos los orígenes, puedes usar unicamente ["*"]
origins = [
    "https://coversheet-app.onrender.com",
    "http://www.render.com",
    "https://www.acedisposal.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sirve archivos estáticos desde la carpeta 'uploads'
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Incluijmos las rutas de la API

app.include_router(email_router, prefix="/api/utils", tags=["Email"])


app.include_router(route_router, prefix="/api/routes", tags=["Routes"])
app.include_router(truck_router, prefix="/api/trucks", tags=["Trucks"])
app.include_router(material_router, prefix="/api/materials", tags=["Materiales"])
app.include_router(driver_router, prefix="/api/drivers", tags=["Drivers"])
app.include_router(landfill_router, prefix="/api/landfills", tags=["Landfills"])

app.include_router(coversheet_router, prefix="/api/coversheets", tags=["Coversheets"])
app.include_router(sparetruckinfo_router, prefix="/api/sparetruckinfo", tags=["SpareTruckInfo"])
app.include_router(downtime_router, prefix="/api/downtime", tags=["Downtime"])
app.include_router(load_router, prefix="/api/load", tags=["Load"])

app.include_router(user_router, prefix="/api/users", tags=["Users"])



@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB and Motor!"}