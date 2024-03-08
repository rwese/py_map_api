import argparse

from app.client import *


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for interacting with the API"
    )
    parser.add_argument("--query", type=str, help="Query string for the API")
    args = parser.parse_args()

    if args.query:
        pos_list = args.query.split(";")
        response = get_pos_by_names(pos_list)
        print(response)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
