import requests
import json

# Define the API endpoint
api_url = "https://api.educhain.com/v1/transactions"

# Define headers and parameters if needed
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

# Function to extract data from the API
def extract_data(api_url, headers):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Extract data
transaction_data = extract_data(api_url, headers)

# Save data to a file
with open("transaction_data.json", "w") as file:
    json.dump(transaction_data, file)

print("Data extraction complete.")
