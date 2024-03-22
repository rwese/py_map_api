from typing import Dict, List, Union
from app.clients import nominatim


class Client:
    """
    Client for Nominatim geocoding service.
    """

    def __init__(self):
        """
        Create a Nominatim geocoding client.
        """
        self.client = nominatim.NominatimClient()

    def get_pos_by_names(
        self, names: List[str]
    ) -> Dict[str, Dict[str, Union[str, bool]]]:
        """
        Get the position by names using Nominatim geocoding service.

        Args:
            names (List[str]): A list of names for which to retrieve positions.

        Returns:
            Dict[str, Dict[str, Union[str, bool]]]: A dictionary containing the responses for each name. Each response is a dictionary with the following keys:
                - "display_name" (str): The display name of the location.
                - "lon" (str): The longitude of the location.
                - "lat" (str): The latitude of the location.
                - "found" (bool): Whether the location was found.
        """
        return self.client.get_pos_by_names(names)
