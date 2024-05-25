
import requests
import concurrent.futures

API_URL = 'http://127.0.0.1:5000/generate'
TEST_TEXT = 'Hello, how are you?'
NUM_USERS = 30

def send_request():
    try:
        response = requests.post(API_URL, json={'text': TEST_TEXT, 'max_length': 50})
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_USERS) as executor:
        futures = [executor.submit(send_request) for _ in range(NUM_USERS)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        for result in results:
            print(result)
