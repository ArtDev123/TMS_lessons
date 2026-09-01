# Проверяем «сайты» подряд. Дальше — те же проверки в потоках и сбор упавших.
import random
import threading
import time

from utils import timed

SITES = [
    "https://api.orders.local/health",
    "https://api.users.local/health",
    "https://api.payments.local/health",
    "https://api.reports.local/health",
]


def check_site(url: str) -> dict:
    delay = random.uniform(0.4, 0.8)
    time.sleep(delay)
    is_ok = random.choice([True, True, True, False])
    return {"url": url, "ok": is_ok, "delay": round(delay, 2)}


def print_result(result: dict) -> None:
    status = "OK" if result["ok"] else "FAIL"
    print(f"{status} {result['url']} ({result['delay']} сек.)")


@timed("Последовательно")
def check_all(urls: list[str]) -> list[dict]:
    results = []
    for url in urls:
        result = check_site(url)
        print_result(result)
        results.append(result)
    return results


@timed("В потоках")
def check_all_threads(urls: list[str]) -> list[dict]:
    results: list[dict] = []
    lock = threading.Lock()

    def worker(url: str) -> None:
        result = check_site(url)
        print_result(result)
        with lock:
            results.append(result)

    threads = [
        threading.Thread(target=worker, args=(url,)) for url in urls
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return results


print("=== Последовательно ===")
report = check_all(SITES)
print(f"Проверено: {len(report)}.")

print("\n=== В потоках ===")
report_threads = check_all_threads(SITES)
print(f"Проверено: {len(report_threads)}.")

failed = [result["url"] for result in report_threads if not result["ok"]]
print(f"Упали: {failed}")
