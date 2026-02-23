import requests

def CheckDayAvability(request_meet_date: str):
    url = "https://overtensely-unrecessive-kellye.ngrok-free.dev/webhook/CheckDayAvability"
    print("CheckDayAvability called with: ", request_meet_date)
    
    payload = {
        "RequestMeetDate": request_meet_date
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, json=payload, headers=headers, timeout=10)
    
    return response.json()  # oppure response.text se non restituisce JSON