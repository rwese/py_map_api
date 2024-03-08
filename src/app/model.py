from typing import Dict, List
from pydantic import BaseModel, Field
from typing_extensions import Annotated


class LocationsRequest(BaseModel):
    locations: str = Field(..., example="London")


class PositionData(BaseModel):
    display_name: str = Field(
        ..., example="London, Greater London, England, United Kingdom"
    )
    lon: str = Field(..., example="-0.1277653")
    lat: str = Field(..., example="51.5074456")


class Location(BaseModel):
    display_name: str
    lon: str
    lat: str
    found: bool


class LocationsResponse(BaseModel):
    positions: Dict[str, Location]
