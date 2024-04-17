import requests, csv

def get_ip_data(ip_address):
    url = f"http://ip-api.com/csv/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text.split(',')
        
        if "invalid query" in data:
            print("Invalid IP address.")
            return None
        
        ip_data = {
            "Status": data[0],
            "Country": data[1],
            "Country Code": data[2],
            "Region": data[4],
            "City": data[5],
            "ZIP Code": data[6],
            "Latitude": data[7],
            "Longitude": data[8],
            "Timezone": data[9],
            "ISP": data[10],
            "Organization": data[11],
            "AS": data[12],
            "IP Address": data[13].strip()
        }
        
        filename_csv = f"{ip_address}.csv"
        with open(filename_csv, 'w', newline='') as file_csv:
            writer_csv = csv.DictWriter(file_csv, fieldnames=ip_data.keys())
            writer_csv.writeheader()
            writer_csv.writerow(ip_data)
        
        filename_txt = f"{ip_address}.txt"
        with open(filename_txt, 'w') as file_txt:
            for key, value in ip_data.items():
                file_txt.write(f"{key}: {value}\n")
        
        print("\nIP Address data:\n")
        for key, value in ip_data.items():
            print(f"{key}: {value}")
        
        print(f"\nIP Address data saved in {ip_address}.txt and {ip_address}.csv\n")
        
        return ip_data
    else:
        print("Error in requesting data from the site. Status code:", response.status_code)
        return None

def main():
    print(" ___ ____  _        __\n|_ _|  _ \(_)_ __  / _| ___\n | || |_) | | '_ \| |_ / _ \\\n | ||  __/| | | | |  _| (_) |\n|___|_|   |_|_| |_|_|  \___/\nMade by DHackerMe | v1.0")
    ip_address = input("\nEnter an IP address: ")
    get_ip_data(ip_address)

    
if __name__ == "__main__":
    main()
