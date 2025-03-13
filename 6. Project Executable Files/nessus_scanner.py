# nessus_scanner.py
import requests

class NessusScanner:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.session = None

    def login(self):
        """Login to Nessus to get an authentication token"""
        url = f"{self.host}/session"
        data = {"username": self.username, "password": self.password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            self.session = response.cookies
            print("Logged into Nessus successfully!")
        else:
            print("Failed to login!")
            raise Exception("Unable to authenticate with Nessus")

    def run_scan(self, target_ip):
        """Start a scan on a target IP"""
        if not self.session:
            raise Exception("Not logged in. Please authenticate first.")
        
        # Define the scan parameters
        scan_url = f"{self.host}/scans"
        scan_data = {
            "uuid": "your-uuid",
            "settings": {
                "name": "Test Scan",
                "policy_id": "your-policy-id",
                "text_targets": target_ip
            }
        }

        response = requests.post(scan_url, cookies=self.session, json=scan_data)
        if response.status_code == 200:
            print(f"Scan started successfully for {target_ip}")
        else:
            print(f"Failed to start scan: {response.text}")

if __name__ == "__main__":
    nessus = NessusScanner("https://nessus.example.com", "admin", "password")
    nessus.login()
    nessus.run_scan("192.168.1.100")
