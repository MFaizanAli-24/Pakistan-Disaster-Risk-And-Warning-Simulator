import json
import uuid

def get_valid_float(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a valid number.")
            
def generate_unique_id():
    return str(uuid.uuid4())

def write_to_json(records, file_path):
    try:
        records = [records]
        prev_records = read_from_json(file_path)
    except Exception as e:
        prev_records = []

    with open(file_path, 'w') as f:
        print(f"Writing {len(prev_records) + len(records)} records to {file_path}")
        json.dump(prev_records + records, f)

def read_from_json(file_path):
    with open(file_path, 'r') as f:
        print(f"Reading records from {file_path}")
        return json.loads(f.read())
