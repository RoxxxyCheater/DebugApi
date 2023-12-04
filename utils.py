import json
import hashlib
import uuid
import random
def is_request_unique(new_request, existing_requests):
    # Проверяем уникальность нового запроса
    new_request_hash = hashlib.sha256(json.dumps(new_request, sort_keys=True).encode()).hexdigest()
    return new_request_hash not in existing_requests

def read_existing_requests(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest() for request in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_request(new_request, file_path="requests.json"):
    existing_requests = read_existing_requests(file_path)

    if is_request_unique(new_request, existing_requests):
        # Добавляем новый запрос к существующим
        existing_requests.append(hashlib.sha256(json.dumps(new_request, sort_keys=True).encode()).hexdigest())
        with open(file_path, "w") as file:
            json.dump(existing_requests, file, indent=2)
        print("Request added successfully.")
        
        # Теперь добавляем данные в файл, как и раньше
        with open("output.txt", "a") as output_file:
            output_file.write("\n")  # Разделитель между запросами
            for key, value in new_request.items():
                output_file.write(f"{key}: {value}\n")
        print("Data written to output.txt.")
    else:
        print("Request is not unique, skipping.")


def generate_random_coordinates():
    latitude = round(random.uniform(-90, 90), 7)
    longitude = round(random.uniform(-180, 180), 7)
    return latitude, longitude

def gen_code():
    global uid
    uid = uuid.uuid1()
    return uid


























# def write_to(data):
#     with open("output.txt", "w") as file:
#         for key, value in data.items():
#             file.write(f"{key}: {value}\n")


    # with open("output.py", "w") as file:
    #     file.write("my_data = " + repr(data))

    # with open("output.json", "w") as file:
    #     json.dump(data, file)