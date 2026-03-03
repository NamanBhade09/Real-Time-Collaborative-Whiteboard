# Real-Time Collaborative Whiteboard

A real-time collaborative whiteboard application built with Flask and Flask-SocketIO. Multiple users can draw simultaneously on a shared canvas, with all drawings synchronized in real-time across all connected clients.

## Features

- **Real-Time Collaboration**: Multiple users can draw on the same board simultaneously with instant synchronization
- **Drawing Tools**:
  - Freehand (Pen) drawing
  - Line
  - Rectangle
  - Circle
- **Customization**:
  - Color picker for choosing drawing colors
  - Line width slider (1-20px)
- **Board Controls**:
  - Undo: Remove the last drawing action
  - Clear Board: Clear all drawings from the board

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Real-Time Communication**: Flask-SocketIO (WebSocket)
- **Frontend**: HTML5 Canvas, JavaScript
- **Protocol**: WebSocket for real-time bidirectional communication

## Installation

1. Make sure you have Python installed (Python 3.7+ recommended)

2. Install the required dependencies:

```
bash
pip install flask flask-socketio
```

## Running the Application

1. Navigate to the project directory

2. Run the application

4. Open your web browser and visit:

```
http://localhost:5000
```

4. To test collaboration, open multiple browser tabs or windows pointing to the same URL

## Project Structure

```
.
├── app.py                 # Main Flask application with SocketIO handlers
├── templates/
│   └── index.html         # Frontend HTML with Canvas and JavaScript

```

## How It Works

### Backend (app.py)

- **Flask Server**: Serves the HTML frontend
- **SocketIO Events**:
  - `draw`: Receives drawing data and broadcasts to all clients
  - `undo`: Removes last drawing and updates all clients
  - `clear`: Clears the board for all clients
  - `request_redraw`: Sends full drawing history to requester

### Frontend (index.html)

- **HTML5 Canvas**: The drawing surface (800x600 pixels)
- **JavaScript**:
  - Handles mouse events (mousedown, mousemove, mouseup)
  - Draws shapes based on selected tool
  - Communicates with server via SocketIO
  - Maintains local copy of drawing data for redraws
)

<img width="923" height="592" alt="Screenshot 2026-03-01 194730" src="https://github.com/user-attachments/assets/61db8b94-f970-47ff-b7ab-41937558f434" />
