# CallAi - Corporate Booking Assistant

CallAi is an AI-powered voice assistant designed to handle corporate appointment scheduling. Leveraging the **Gemini 2.5 Flash Live API**, it provides a real-time, multi-modal interaction experience, supporting voice, video, and screen sharing to assist users in booking meetings via an **n8n** backend.

## 🚀 Features

- **Real-time Voice Interaction**: High-quality audio streaming with the Gemini Live API.
- **Multimodal Support**: Stream from your camera or screen for visual context.
- **n8n & Google Calendar Integration**: Automated availability checks and meeting scheduling through n8n webhooks.
- **Multilingual**: Naturally responds in the language used by the customer.
- **Professional Tone**: Strictly follows corporate protocols for appointment scheduling.

## 🛠️ Architecture

The system consists of three main layers:
1. **Gemini Live API**: Handles the AI logic, natural language understanding, and audio generation.
2. **Python Client (`main.py`)**: Manages local hardware (mic, speakers, camera) and connects to the Gemini session via WebSockets.
3. **n8n Backend**: Executes business logic by interacting with Google Calendar through dedicated webhooks.

## 📋 Prerequisites

- Python 3.10+
- A Google Gemini API Key (with access to the Live API).
- An n8n instance with the `CallAi.json` workflow imported.
- `ngrok` or similar for exposing webhooks if running n8n locally.

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd CallAi
   ```

2. **Install dependencies**:
   ```bash
   pip install google-genai opencv-python pyaudio pillow mss requests
   ```
   *Note: On Linux, you may need additional libraries for `pyaudio` (e.g., `libportaudio2`, `python3-pyaudio`).*

3. **Set Environment Variables**:
   ```bash
   export GEMINI_API_KEY='your_api_key_here'
   ```

## 🖥️ Usage

Run the main script with the desired mode:

- **Audio Only (Default)**:
  ```bash
  python main.py --mode none
  ```
- **Camera Streaming**:
  ```bash
  python main.py --mode camera
  ```
- **Screen Streaming**:
  ```bash
  python main.py --mode screen
  ```

## 🔗 n8n Webhook Integration

The assistant communicates with n8n via the following endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/webhook/CheckCalendar` | `GET` | Verifies availability for a specific date and time. |
| `/webhook/CheckDayAvability` | `GET` | Returns all busy slots for a given day. |
| `/webhook/ScheduleMeeting` | `POST` | Finalizes the booking in Google Calendar. |

**Workflow Import**: Import the [CallAi.json](./N8N-Workflow/CallAi.json) file into your n8n instance to set up the necessary nodes.

## 📂 Project Structure

- `main.py`: The entry point for the application, managing asynchronous loops for audio/video.
- `SystemPrompt.py`: Contains the character identity and strict behavioral rules for the AI.
- `FunctionMap.py`: Maps Gemini tool calls to local Python functions.
- `Tool/`: Directory containing individual tool implementations for n8n API calls.
- `N8N-Workflow/`: Contains the `.json` file for the n8n backend setup.
