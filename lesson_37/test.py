import requests
import threading
import time

api_url = "https://api.kufar.by/search-api/v2/search/rendered-paginated"


params: dict[str, str] = {
    "cat": "1010",
    "cur": "usd",
    "lang": "ru",
    "size": "10",
    "typ": "let",
}

semaphore = threading.Semaphore(5)


def execute_kufar_request():
    with semaphore:
        response = requests.get(url=api_url, params=params)
        print(response.status_code)
        if response.status_code == 429:
            time.sleep(2)


threads: list[threading.Thread] = []

for i in range(10000):
    threads.append(threading.Thread(target=execute_kufar_request))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
