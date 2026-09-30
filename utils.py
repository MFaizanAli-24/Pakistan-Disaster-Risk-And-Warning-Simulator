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

def read_from_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
        
def write_to_json(record, file_path):
    previous_records = read_from_json(file_path)

    previous_records.append(record)

    with open(file_path, "w") as f:
        json.dump(previous_records, f, indent=4)
