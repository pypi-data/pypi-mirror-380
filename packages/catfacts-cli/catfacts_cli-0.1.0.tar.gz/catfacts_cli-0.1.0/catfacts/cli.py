import requests
import sys
import time

RETRY_LIMIT = 3
WAIT_SECONDS = 2

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        fact = response.json()
        print("Cat FUN Fact:", fact["fact"])
    elif response.status_code in (400, 401, 403, 404):
        print("Client error! Status code:", response.status_code)
    else:
        print("Unexpected error:", response.status_code)

def main():
    if not check_internet():
        print("No internet connection! Exiting...")
        sys.exit(1)

    while True:
        get_cat_fact()

        retries = 0
        while retries < RETRY_LIMIT:
            ExitQuestion = input("Do you want to exit? (Y/Yes or N/No): ").strip().lower()

            if ExitQuestion in ("y", "yes"):
                print("Goodbye!")
                sys.exit(0)
            elif ExitQuestion in ("n", "no"):
                time.sleep(WAIT_SECONDS)
                break
            else:
                retries += 1
                print(f"Not valid! Attempts left: {RETRY_LIMIT - retries}")

        if retries >= RETRY_LIMIT:
            print("❌ Too many invalid attempts. Exiting...")
            sys.exit(1)
