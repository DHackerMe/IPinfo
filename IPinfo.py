import requests
import pandas as pd
from io import StringIO

def get_ip_info(ip_address):
    url = f"http://ip-api.com/csv/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def save_csv(data, ip_address):
    df = pd.read_csv(StringIO(data))
    filename = f"{ip_address}_info.csv"
    df.to_csv(filename, index=False)
    print(f"IP data has been saved in {filename}")

def main():
    ip_address = input("Enter the IP address: ")
    ip_info = get_ip_info(ip_address)
    if ip_info and not "invalid query" in ip_info:
        df = pd.read_csv(StringIO(ip_info))
        print(df.to_string(index=False))
        choice = input("Do you want to save data as CSV? (y/n): ").lower()
        if choice == 'y':
            save_csv(ip_info, ip_address)
    elif "invalid query" in ip_info:
        print("Error: Invalid query.")
    else:
        print("Error: Failed to get IP data.")

if __name__ == "__main__":
    main()
