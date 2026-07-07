from fastapi import FastAPI

from app.api.patient import router as patient_router

app = FastAPI(
    title="Hospital Management API"
)

app.include_router(patient_router)


@app.get("/")
def home():
    return {
        "message": "Hospital Management System!"
    }