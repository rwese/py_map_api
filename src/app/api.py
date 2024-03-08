from fastapi import FastAPI, Depends
from app.model import PositionsRequest, PositionsResponse
from app.client import get_pos_by_names

app = FastAPI()

@app.get("/hello")
async def read_root():
    """
    A function to handle requests to the /hello endpoint, returning a simple message.
    """
    return {"message": "Hello, World"}

@app.get("/pos", response_model=PositionsResponse)
def get_pos(poisRequest: PositionsRequest = Depends()):
    """
    Get positions by names, comma separated and return a json of found location names, longitude, and latitude.
    """
    pois = poisRequest.pois.split(",")
    pois = [poi.strip() for poi in pois]
    results = get_pos_by_names(pois)
    responses = {}
    for name in pois:
        result = results.get(name)
        if result:
            responses[name] = {
                "display_name": result['display_name'],
                "lon": result['lon'],
                "lat": result['lat']
            }
        else:
            responses[name] = {
                "display_name": "Not found",
                "lon": '0',
                "lat": '0'
            }


    return {
        "positions": responses
    }


