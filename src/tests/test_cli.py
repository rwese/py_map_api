import unittest
from unittest.mock import patch, call
from cli import main
from app.clients.nominatim import NominatimClient


class TestCLI(unittest.TestCase):

    @patch("geopy.geocoders.Nominatim.geocode")
    def test_main_with_mocked_client(self, mock_client):
        mock_client.return_value.geocode.return_value = MockedGeocodeResponse()

        test_args = ["program_name", "--query", "New York;Los Angeles"]
        with patch("sys.argv", test_args):
            main()

        mock_client.assert_has_calls(
            [
                call("New York"),
                call().__bool__(),
                call().raw.__getitem__("display_name"),
                call().raw.__getitem__("lon"),
                call().raw.__getitem__("lat"),
                call("Los Angeles"),
                call().__bool__(),
                call().raw.__getitem__("display_name"),
                call().raw.__getitem__("lon"),
                call().raw.__getitem__("lat"),
            ],
        )


class MockedGeocodeResponse:
    def __init__(self):
        self.raw = {
            "display_name": "Mocked Display Name",
            "lon": "Mocked Longitude",
            "lat": "Mocked Latitude",
        }


if __name__ == "__main__":
    unittest.main()
