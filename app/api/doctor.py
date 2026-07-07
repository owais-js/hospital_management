from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.doctor import(
    DoctorCreate,
    DoctorResponse
)

from app.crud.doctor import(
    create_doctor,
    get_doctor,
    get_doctors,
    update_doctor,
    delete_doctor
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/",response_model=DoctorResponse)
def create(
    doctor : DoctorCreate,
    db : Session = Depends(get_db)
):
    return create_doctor(db,doctor)


