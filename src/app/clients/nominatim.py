from typing import Dict, List, Optional, Union
from geopy.geocoders import Nominatim


class NominatimClient:
    """Wrapper around GeoPy's Nominatim geocoder."""

    def __init__(self, user_agent: str = "PyMapApi for CLI", timeout: int = 10):
        """Create a Nominatim geocoding client."""
        self.client = Nominatim(user_agent=user_agent, timeout=timeout)

    def get_pos_by_names(
        self, names: List[str]
    ) -> Dict[str, Dict[str, Union[str, bool]]]:
        """Get the position by names using Nominatim geocoding service."""
        responses = {}
        for name in names:
            response = self.get_pos_by_name(name)
            if response:
                responses[name] = response
            else:
                responses[name] = {
                    "display_name": "Not found",
                    "lon": "0",
                    "lat": "0",
                    "found": False,
                }

        return responses

    def get_pos_by_name(self, name: str) -> Optional[Dict[str, Union[str, bool]]]:
        """Get the position by name using Nominatim geocoding service."""
        response = self.client.geocode(name)
        if response:
            return {
                "display_name": response.raw["display_name"],
                "lon": response.raw["lon"],
                "lat": response.raw["lat"],
                "found": True,
            }
        return None
