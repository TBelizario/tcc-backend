from fastapi import FastAPI
import uvicorn
import utils.config as app_config
from utils.database import Base, engine
from app.sensores.models import sensorModel, leituraSensorModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app_config.routes(app)
app_config.errorHandler(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/home")
def home():
    return {"message": "Hello word"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)