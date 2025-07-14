from pydantic import BaseModel, Field
from datetime import date
from typing import Dict,List

class WheelFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submitted_by: str
    submittedDate: date
    fields: WheelFields

class WheelSpecificationOut(BaseModel):
    formNumber: str = Field(..., alias="form_number")
    submitted_by: str
    submittedDate: date = Field(..., alias="submitted_date")
    fields: Dict[str, str]


    class Config:
        from_attributes = True  
        populate_by_name = True 

class WheelSpecListResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecificationOut]