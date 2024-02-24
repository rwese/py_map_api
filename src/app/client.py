from app.clients import nominatim

def get_pos_by_names(names: list):
    """
    Get the position by names using Nominatim geocoding service.

    Args:
        names (list): A list of names for which to retrieve positions.

    Returns:
        dict: A dictionary containing the responses for each name.
    """
    return nominatim.get_pos_by_names(names)

