import csv
import json

classes: list = [
    "club",
    "std",
    "15m",
    "all"
    ]

classes = [f"data/gliders/{c}.txt" for c in classes]

for file in classes:
    lines = []
    # read as csv with ID,CALL,CN,TYPE,NAME
    with open(file, "r" ,encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            lines.append(row[0].split(","))

        with open(file.replace(".txt", ".json"), "w" ,encoding="utf-8") as f:
            json.dump(
                [
                    {
                        "name": line[4] if len(line) > 4 else "",
                        "cn": line[2] if len(line) > 2 else "",
                        "glider": "",
                        "comp": line[2] if len(line) > 2 else "",
                        "flarm": [line[0]] if len(line) > 0 else "",
                    }
                    for line in lines[1:]
                ],
                f,
                indent=4,
            )