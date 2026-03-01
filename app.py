import os
from flask import Flask, render_template
import base64
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates')
app.secret_key = base64.urlsafe_b64encode(os.urandom(24)).decode('utf-8')
socketio = SocketIO(app)

# This list will store the drawn lines and points.
# In a real application, you would use a database.
drawing_data = []

@app.route('/')
def index():
    """Serve the HTML front-end."""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Send existing drawing data to a new client upon connection."""
    emit('drawing_data', drawing_data)
    print('Client connected!')

@socketio.on('disconnect')
def handle_disconnect():
    """Log when a client disconnects."""
    print('Client disconnected!')

@socketio.on('draw')
def handle_draw(data):
    """
    Receive drawing data from a client and broadcast it to all others.
    Data is a dictionary with 'x', 'y', 'prev_x', 'prev_y', 'color', 'lineWidth', and 'shape'.
    """
    drawing_data.append(data)
    emit('drawing_update', data, broadcast=True, include_self=False)

@socketio.on('undo')
def handle_undo():
    """Remove the last drawing and update all clients."""
    global drawing_data
    if len(drawing_data) > 0:
        drawing_data.pop()
        emit('undo_board', drawing_data, broadcast=True)

@socketio.on('clear')
def handle_clear():
    """Clear the drawing board for all clients."""
    global drawing_data
    drawing_data = []
    emit('clear_board', broadcast=True)

@socketio.on('request_redraw')
def handle_request_redraw():
    """Send existing drawing data to the requester for redraw."""
    emit('drawing_data', drawing_data)

if __name__ == '__main__':
    # Use 'debug=True' for development, but remove in production
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
