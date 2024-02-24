from geopy.geocoders import Nominatim

def client():
    """
    Create a Nominatim geocoding client.

    Returns:
        Nominatim: A Nominatim geocoding client.
    """
    return Nominatim(user_agent="PyMapApi for CLI", timeout=10)

def get_pos_by_names(names: list):
    """
    Get the position by names using Nominatim geocoding service.

    Args:
        names (list): A list of names for which to retrieve positions.

    Returns:
        dict: A dictionary containing the responses for each name.
    """
    responses = {}
    for name in names:
        query = name
        response = client().geocode(query)
        responses[name] = response.raw

    return responses


