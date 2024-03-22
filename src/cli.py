import argparse
import json
from app.api import create_app


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for interacting with the API"
    )
    parser.add_argument("--query", type=str, help="Query string for the API")
    args = parser.parse_args()

    app = create_app()
    client = app.client
    if args.query:
        pos_list = args.query.split(";")
        response = client.get_pos_by_names(pos_list)
        json_response = json.dumps(response)
        print(json_response)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
