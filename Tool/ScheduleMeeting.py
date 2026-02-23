import requests

def schedule_meeting(request_meet_datetime: str, meet_title: str, meet_description: str):
    url = "https://overtensely-unrecessive-kellye.ngrok-free.dev/webhook/ScheduleMeeting"
    print("ScheduleMeeting called with: ", request_meet_datetime, meet_title, meet_description)
    
    payload = {
        "RequestMeetDateTime": request_meet_datetime,
        "MeetTitle": meet_title,
        "MeetDescription": meet_description
    }
    
    response = requests.post(url, json=payload, timeout=10)
    
    return response.json()  # oppure response.text se non restituisce JSON