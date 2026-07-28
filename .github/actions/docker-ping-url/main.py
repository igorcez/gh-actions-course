import requests
import time
import os

if __name__ == "__main__":
    run()

def ping_url (url, delay, max_trials):
    number_of_trials = 0
    while number_of_trials < max_trials:
        resp = requests.get(f"{url}", timeout=5)
        print(resp.status_code, resp.text)
        if resp.status_code == 200:
            return True
        else:
            time.sleep(delay)
            number_of_trials += 1
    return False

def run():
    url = os.getenv("INPUT_URL")
    delay = os.getenv("INPUT_DELAY")
    max_trials = os.getenv("INPUT_MAX_TRIALS")

    result = ping_url(url, delay, max_trials)
    if result == False:
        raise RuntimeError("something went wrong") 



        


