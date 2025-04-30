import requests

API_KEY = "om1_live_xxxxxx"  # ganti nanti di VS Code
url = "https://api.openmind.org/om1/tasks"

payload = {
    "task_type": "text",
    "content": "Hello, world!"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
initial commit for OM1 task sender
