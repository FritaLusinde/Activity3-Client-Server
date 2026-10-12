# Activity 3: Design and Implementation of a Simple Client–Server Application

## 1. Introduction
The purpose of this assignment is to design and implement a simple client–server application in a localhost environment. The application demonstrates how a client sends a request to a server and receives a response.

## 2. Objectives
- To implement client and server components.
- To demonstrate communication between the components.
- To identify the layered architecture used.
- To test and show successful communication.

## 3. Tools and technologies
- Python 3: implements the HTTP server.
- HTML and CSS: create the client interface.
- JavaScript Fetch API: sends requests from the browser to the server.
- HTTP and JSON: carry requests and responses.
- Localhost (`127.0.0.1`): allows communication on the same computer.

## 4. System design and layered architecture
The application uses a simple layered architecture:

**Presentation layer:** The browser displays the page, accepts a message, and displays the result.

**Communication layer:** HTTP is used to send GET and POST requests. JSON is used to represent message data.

**Application layer:** The Python server receives the request, checks the message, and prepares a response.

**Host/network layer:** The loopback address `127.0.0.1` and port `8000` direct browser requests to the local server.

### Communication flow
Browser client → HTTP request → Python server → process request → HTTP/JSON response → Browser client

## 5. Implementation
The server is implemented in `app.py`. It listens on `127.0.0.1:8000`, serves the webpage, provides a status endpoint, and processes messages sent to `/api/message`.

The client is implemented in `index.html`. It checks whether the server is available and uses JavaScript's Fetch API to send a message. The response from the server is displayed on the page.

## 6. Testing and expected results
Run `python app.py` (or `py app.py`) and open `http://127.0.0.1:8000` in a browser.

| Test | Action | Expected result |
|---|---|---|
| Server start | Run the Python program | Server reports that it is running on port 8000 |
| Status check | Open the webpage | Successful connection status appears |
| Message transfer | Type a message and click Send message | Server returns the received message and time |
| Server logging | Observe Command Prompt | HTTP request logs appear |

**Record the actual result:** After running the application on your computer, insert screenshots showing the successful connection, a message and reply, and the server logs. Do not claim a test was completed until you have run it.

## 7. Conclusion
This project demonstrates the basic client–server model. The browser acts as the client and sends requests over HTTP to a Python server on localhost. The server processes the requests and returns JSON responses, showing communication between separate system components.

## 8. Project files
- `app.py` — server-side implementation.
- `index.html` — browser client interface.
- `README.md` — setup and execution instructions.
