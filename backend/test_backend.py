import requests

BASE_URL = "http://127.0.0.1:8000"

def fetch_configs():
    print("Fetching configs...")
    response = requests.get(f"{BASE_URL}/configs")
    if response.status_code != 200:
        print("Failed to fetch configs:", response.text)
        return []
    configs = response.json()
    print(f"Fetched {len(configs)} configs.")
    return configs

def start_call(driver_name, driver_phone, load_number, config_id):
    print("Starting call...")
    payload = {
        "driver_name": driver_name,
        "driver_phone": driver_phone,
        "load_number": load_number,
        "config_id": config_id
    }
    response = requests.post(f"{BASE_URL}/start_call", json=payload)
    if response.status_code != 200:
        print("Call failed:", response.text)
        return None
    return response.json()

def main():
    configs = fetch_configs()
    if not configs:
        print("No configs available to test.")
        return

    test_config = configs[0]
    driver_name = "John Doe"
    driver_phone = "+10000000000"
    load_number = "LOAD123"

    result = start_call(driver_name, driver_phone, load_number, test_config["id"])
    if result:
        print("\n=== Call Transcript ===")
        print(result.get("transcript"))
        print("\n=== AI Summary ===")
        print(result.get("summary"))

if __name__ == "__main__":
    main()
