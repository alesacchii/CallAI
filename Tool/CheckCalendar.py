import requests

def check_calendar(request_meet_datetime: str):
    url = "https://overtensely-unrecessive-kellye.ngrok-free.dev/webhook/CheckCalendar"
    print("CheckCalendar called with: ", request_meet_datetime)
    
    payload = {
        "RequestMeetDateTime": request_meet_datetime
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, json=payload, headers=headers, timeout=10)
    
    return response.json()  # oppure response.text se non restituisce JSON