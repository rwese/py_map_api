import argparse
import json
from app.api import create_app
from app.client import Client
from unittest.mock import MagicMock


class NoMagicMockJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MagicMock):
            return "MockedValue"
        return json.JSONEncoder.default(self, obj)


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for interacting with the API"
    )
    parser.add_argument("--query", type=str, help="Query string for the API")
    args = parser.parse_args()

    app = create_app()
    client = Client()
    if args.query:
        pos_list = args.query.split(";")
        response = client.get_pos_by_names(pos_list)
        json_encoded = json.dumps(
            response, cls=NoMagicMockJSONEncoder, ensure_ascii=False
        )

        print(json_encoded)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
