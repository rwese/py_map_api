from app.model import LocationsResponse, LocationsRequest
from app.client import Client

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(
        title="My Python Map Api",
        description="My Python Map Api Gateway to OpenStreetMap via Nominatim",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

    return app


app = create_app()


@app.get("/hello")
async def hello():
    """
    A function to handle requests to the /hello endpoint, returning a simple message.
    """
    return {"message": "Hello, World"}


@app.get("/search_locations", response_model=LocationsResponse)
def get_pos(locationsRequest: LocationsRequest = Depends()):
    """
    Get locations by names, comma separated and return a json of found location names, longitude, and latitude.
    """
    locations = locationsRequest.locations.split(",")
    locations = [location.strip() for location in locations]
    results = Client().get_pos_by_names(names=locations)
    responses = {}
    for name in locations:
        result = results.get(name)
        if result:
            responses[name] = {
                "display_name": result["display_name"],
                "lon": result["lon"],
                "lat": result["lat"],
                "found": True,
            }
        else:
            responses[name] = {
                "display_name": "Not found",
                "lon": "0",
                "lat": "0",
                "found": False,
            }

    return {"positions": responses}
