import requests
import time
import os

def ping_url (url, delay, max_trials):
    number_of_trials = 0
    while number_of_trials < int(max_trials):
            try:
                resp = requests.get(f"{url}", timeout=5)
            except requests.exceptions.RequestException as e:
                print("request error:", e)
                resp = None

            if resp is not None:
                print(f"STATUS CODE: {resp.status_code}")
                if resp.status_code == 200:
                    return True

            try:
                time.sleep(delay)
            except TypeError:
                # fallback if delay wasn't converted
                time.sleep(1)

            number_of_trials += 1
    return False

def run():
    url = os.getenv("INPUT_URL")
    if not url:
        raise RuntimeError("INPUT_URL is required")

    try:
        delay = float(os.getenv("INPUT_DELAY", "1"))
    except (TypeError, ValueError):
        delay = 1.0

    try:
        max_trials = int(os.getenv("INPUT_MAX_TRIALS", "5"))
    except (TypeError, ValueError):
        max_trials = 5

    result = ping_url(url, delay, max_trials)

    print(result)

    with open(os.getenv("GITHUB_OUTPUT"), "a", encoding="utf-8") as f:
        print(f"url-reachable={result}", file=f)

    if not result:
        raise RuntimeError("something went wrong")

if __name__ == "__main__":
    run()



