from typing import Dict
from pydantic import BaseModel, Field
from typing_extensions import Annotated

class PositionsRequest(BaseModel):
    pois: str  = Field(..., description="Names of Points of interest to retrieve coordinates for.", max_length=2000)

class PositionData(BaseModel):
    display_name: str = Field(..., example="London, Greater London, England, United Kingdom")
    lon: str = Field(..., example="-0.1277653")
    lat: str = Field(..., example="51.5074456")

class PositionsResponse(BaseModel):
    data: Dict[str, PositionData] = Field(..., alias="__root__")
