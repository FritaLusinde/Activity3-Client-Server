# Activity 3: Local Client–Server Application

## Project overview
This project demonstrates a simple client–server application running on the same computer (localhost). A browser-based client sends HTTP requests to a Python server. The server responds with JSON data.

## Requirements
- Python 3 installed
- A web browser
- No third-party Python packages are required

## How to run (Windows)
1. Extract the ZIP file into a folder.
2. Open that folder in File Explorer.
3. Click the address bar, type `cmd`, and press Enter. A Command Prompt opens in the project folder.
4. Run:
   ```bash
   python app.py
   ```
   If that command does not work, try `py app.py`.
5. Keep the Command Prompt open while the server runs.
6. Open your browser and visit: `http://127.0.0.1:8000`
7. Confirm the connection status appears. Type a message and click **Send message**.
8. The server response should display the message it received and a timestamp.
9. The Command Prompt also displays request logs. This is additional evidence that the server received requests.
10. To stop the server, return to Command Prompt and press `Ctrl+C`.

## Architecture
1. **Presentation layer (client):** `index.html` displays the interface and accepts the user's message.
2. **Communication layer:** HTTP requests and responses carry JSON between the browser and server.
3. **Application layer (server):** `app.py` validates the request and creates a reply.
4. **Local host/network layer:** `127.0.0.1` routes the communication back to the same computer; port `8000` identifies the server process.

## Endpoints
- `GET /` — serves the client webpage.
- `GET /api/status` — returns a server status message.
- `POST /api/message` — accepts a JSON message and returns a reply.

## Testing checklist
- [ ] Server starts and prints `Server running at http://127.0.0.1:8000`
- [ ] The webpage opens in the browser
- [ ] Connection status says communication is successful
- [ ] Sending a message returns the same message in the server response
- [ ] Command Prompt shows request logs

## Evidence to capture before submitting
Take screenshots of:
1. The webpage showing the successful connection status.
2. The webpage after sending a message and receiving the server response.
3. The Command Prompt showing the server running and request logs.

Insert the screenshots into your report or upload them alongside the project if your lecturer requests them.

## Important note about the submission link
`127.0.0.1` works only on your own computer. It is not a public website link that your lecturer can open. Submit the project through your school's LMS, or upload the ZIP/project to a public GitHub repository and submit that repository URL. Follow your lecturer's instructions about whether a repository link, report, or live deployment is required.
