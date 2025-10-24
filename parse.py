HEADER = """
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
            },
        ]
    },
    "data": ["""
print(HEADER)

with open('data.dat') as f:
    DATA = f.read()

polls = {}
for y in DATA.split():
    poll = y.split(',')
    polls[poll[0]] = []
    for i, v in enumerate(poll[1:], start=1):
        polls[poll[0]].append((i, v))

for year, poll in polls.items():
    for p in poll:
        if p[1] == '0.0':
            continue
        print(f"[\"{year}/{p[0]}/1\", {p[1]}],")

print("""]
}""")
