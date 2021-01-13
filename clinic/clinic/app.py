from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from models import ClinicRequest, Clinic

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

clinics = []
clinics_last_id = 0

@app.get("/clinics")
def read_clinics():
    return clinics


@app.post("/clinics", response_model=Clinic)
def create_clinic(clinic: ClinicRequest):
    global clinics_last_id
    new_clinic = Clinic(**clinic.dict(), id=clinics_last_id)
    clinics.append(new_clinic)
    clinics_last_id = clinics_last_id + 1
    return new_clinic
