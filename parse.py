from argparse import ArgumentParser, Namespace
from csv import reader
from json import dumps


HEADER: str = """
{
    "license": "CC0-1.0",
    "description": {
        "en": "Opinion polling for ****"
    },
    "schema": {
        "fields": [
            {
                "name": "Date",
                "type": "string",
                "title": {
                    "en": "Date"
                }
            },
            {
                "name": "***_polls",
                "type": "number",
                "title": {
                    "en": "***"
                }
            }
        ]
    },
    "data":"""

def parse(filename: str) -> str:
    with open(filename) as f:
        DATA: list[list[str]] = [line for line in reader(f)]

    polls: list[list[str]] = []
    for line in DATA:
        year: str = line[0]
        for i, p in enumerate(line[1:], start=1):
            if p == '0.0':
                continue
            polls.append([f"{year}/{i}/1", float(p)])
    
    return polls

def print_data(polls: list[list[str]]) -> None:
    print(HEADER, end='')
    print(dumps(polls, indent=8))
    print("}")

def get_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(prog='PollDataParser')
    parser.add_argument('filename', nargs='?', default='data.dat')
    return parser.parse_args()


if __name__ == "__main__":
    args: Namespace = get_args()
    polls: list[list[str]] = parse(args.filename)
    print_data(polls)
