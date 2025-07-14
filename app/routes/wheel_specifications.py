from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models
from sqlalchemy import and_
from app.database import Session_local
from typing import Optional
from datetime import date
router=APIRouter()

def get_db():
    db=Session_local()
    try:
        yield db
    finally:
        db.close()
@router.post("/api/forms/wheel-specification",status_code=201)
def create_wheel_specification(request:schemas.WheelSpecificationCreate,db:Session=Depends(get_db)):
    if db.query(models.WheelSpecification).filter_by(form_number=request.formNumber).first():
        raise HTTPException(status_code=400, detail="Form number already exists.")
    wheel_spec = models.WheelSpecification(
        form_number=request.formNumber,
        submitted_by=request.submitted_by,
        submitted_date=request.submittedDate,
        fields=request.fields.dict()
    )
    db.add(wheel_spec)
    db.commit()
    db.refresh(wheel_spec)

    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": wheel_spec.form_number,
            "submitted_by": wheel_spec.submitted_by,
            "submittedDate": str(wheel_spec.submitted_date),
            "status": wheel_spec.status
        }
    }

@router.get("/wheel-specifications", response_model=schemas.WheelSpecListResponse)
def get_wheel_specifications(
    form_number: Optional[str] = None,
    submitted_by: Optional[str] = None,
    submitted_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    filters = []
    if form_number:
        filters.append(models.WheelSpecification.form_number == form_number)
    if submitted_by:
        filters.append(models.WheelSpecification.submitted_by == submitted_by)
    if submitted_date:
        filters.append(models.WheelSpecification.submitted_date == submitted_date)

    results = db.query(models.WheelSpecification).filter(and_(*filters)).all()


    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [schemas.WheelSpecificationOut.model_validate(row) for row in results]
    }