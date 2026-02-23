from google import genai
from google.genai import types
from google.genai.types import Type
from Tool.CheckCalendar import check_calendar
from Tool.ScheduleMeeting import schedule_meeting
from Tool.CheckDayAvability import CheckDayAvability

# Mappa nome tool (come dichiarato in TOOL_CONFIG) → funzione Python reale
FUNCTION_MAP = {
    "CheckCalendar": check_calendar,
    "ScheduleMeeting": schedule_meeting,
    "CheckDayAvability": CheckDayAvability,
}

TOOL_CONFIG = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="CheckCalendar",
                description="Check if the user is available at the specified date and time.",
                parameters=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["request_meet_datetime"],
                    properties = {
                        "request_meet_datetime": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "The date and time to check for availability. Format: 'YYYY-MM-DDTHH:MM:SS+HH:MM'. Minutes: 00 or 30.",
                        ),
                    },
                ),
                response=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    properties = {
                        "AvailableHour": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "Indicates if the slot is free ('true') or busy ('false').",
                        ),
                    },
                ),
            ),
            types.FunctionDeclaration(
                name="ScheduleMeeting",
                description="Schedule a meeting with a title, description, and specific time.",
                parameters=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["request_meet_datetime", "meet_title", "meet_description"],
                    properties = {
                        "request_meet_datetime": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "The date and time to schedule the meeting. Format: 'YYYY-MM-DDTHH:MM:SS+HH:MM'.",
                        ),
                        "meet_title": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "Must be in the format 'Meet with <name>'. Example: 'Meet with John Doe'. Ask every time the person who call you",
                        ),
                        "meet_description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "The description of the meeting. Example: 'Meeting to discuss project X'. Ask every time the reason of the required call",
                        ),
                    },
                ),
                response=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    properties = {
                        "BookedMeet": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "Confirmation status of the booking ('true' if successful).",
                        ),
                    },
                ),
            ),
            types.FunctionDeclaration(
                name="CheckDayAvability",
                description="Check the availability of a specific day and return all commitments.",
                parameters=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["request_meet_date"],
                    properties = {
                        "request_meet_date": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "The date to check for availability. Format: 'YYYY-MM-DD'.",
                        ),
                    },
                ),
                response=genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    properties = {
                        "DaySchedule": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "A summary or list of all scheduled events for the requested day. Every other hour is free.",
                        ),
                    },
                ),
            ),
        ]
    ),
]