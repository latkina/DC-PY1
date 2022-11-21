import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file: str, delimiter: str = ",") -> list[dict]:
    with open(file) as f:
        json_file = []
        lines = [line.strip() for line in f]
        list_column = lines[0].split(delimiter)
        list_value = lines[1:]
        for value in list_value:
            json_file.append(dict(zip(list_column, value.split(delimiter))))
        return json_file


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
