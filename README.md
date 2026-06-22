# Real-Time Collaborative Whiteboard 🎨

An interactive, real-time collaborative drawing and brainstorming platform built with Flask and WebSockets. Multiple users can draw, sketch, and collaborate simultaneously on a shared canvas with instant synchronization across all connected clients.

## ✨ Features

### Core Drawing Features
- 🎨 **Real-Time Collaboration** - Multiple users drawing simultaneously with instant synchronization
- 🖌️ **Multiple Drawing Tools**
  - Freehand pen for sketching
  - Straight lines
  - Rectangles and circles
  - Text labels
  - Eraser tool

### Customization & Control
- 🌈 **Color Picker** - Full RGB color spectrum selection
- 📏 **Line Width Adjustment** - Brush size slider (1-20px)
- 🎨 **Multiple Color Palettes** - Predefined and custom colors
- ⏱️ **Real-Time Cursor Tracking** - See where collaborators are drawing

### Board Management
- ↩️ **Undo/Redo** - Remove or restore drawing actions
- 🗑️ **Clear Board** - Clear all drawings at once
- 💾 **Auto-Save** - Automatic session saving to prevent data loss
- 📤 **Export Options** - Save as PNG, SVG, or PDF
- 🔄 **Session History** - Review and restore previous versions

### Collaboration Features
- 👥 **Unlimited Collaborators** - Support for 50+ concurrent users
- 🔐 **Secure Sessions** - Password-protected collaborative sessions
- 📍 **User Presence** - See active participants
- ⌚ **Activity Indicators** - Real-time notifications of user actions

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/NamanBhade09/Real-Time-Collaborative-Whiteboard.git

# 2. Navigate to project directory
cd Real-Time-Collaborative-Whiteboard

# 3. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py

# 6. Open in browser
# Navigate to http://localhost:5000
```

## 📁 Project Structure

```
Real-Time-Collaborative-Whiteboard/
├── app.py                 # Main Flask application with SocketIO handlers
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Frontend with HTML5 Canvas and JavaScript
│   ├── login.html         # Session login page
│   └── settings.html      # Whiteboard settings
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   ├── canvas.js      # Canvas drawing logic
│   │   ├── socket.js      # WebSocket communication
│   │   └── ui.js          # User interface interactions
│   └── images/            # Icons and assets
└── README.md             # Documentation
```

## 🛠️ Tech Stack

**Backend:**
- Flask - Python web framework
- Flask-SocketIO - WebSocket support for real-time communication
- python-socketio - Socket.IO implementation
- python-engineio - Engine.IO transport protocol

**Frontend:**
- HTML5 Canvas API - Drawing surface
- JavaScript (Vanilla) - Event handling and drawing logic
- Socket.IO Client - Real-time communication
- CSS3 - Styling and layouts

**Real-Time Communication:**
- WebSockets - Bidirectional low-latency communication
- Socket.IO - Fallback support for older browsers

## 📝 Usage Guide

### Getting Started

1. **Launch the Application**
   ```bash
   python app.py
   # Application runs on http://localhost:5000
   ```

2. **Create or Join Session**
   - Create new session: Click "New Session"
   - Join existing: Share session URL with collaborators

3. **Start Drawing**
   - Select tool from toolbar
   - Choose color and brush size
   - Draw on canvas

### Drawing Tools

| Tool | Shortcut | Description |
|------|----------|-------------|
| Pen | P | Freehand drawing |
| Line | L | Draw straight lines |
| Rectangle | R | Draw rectangles |
| Circle | C | Draw circles |
| Text | T | Add text labels |
| Eraser | E | Erase drawings |
| Color Picker | Space | Select colors |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+Z | Undo last action |
| Ctrl+Y | Redo action |
| Ctrl+S | Save session |
| Ctrl+E | Export drawing |
| Delete | Clear canvas |
| [ | Decrease brush size |
| ] | Increase brush size |
| 1-9 | Preset colors |

## 🎮 Features in Detail

### Real-Time Collaboration

```
User A draws → WebSocket sends data → Server broadcasts → User B, C see instantly
```

- **Low Latency**: Drawing updates sent every 50ms
- **Efficient**: Only drawing delta sent, not full canvas
- **Reliable**: Automatic reconnection on connection loss

### Drawing Performance

- Optimized canvas rendering
- Hardware acceleration support
- Smooth 60+ FPS drawing
- Efficient event batching

### Session Management

- Auto-save every 30 seconds
- Session backup and recovery
- User session history
- Activity logs

## 🔐 Security & Privacy

- **Session Encryption** - Optional password protection
- **User Authentication** - Optional login system
- **Data Privacy** - No external data storage by default
- **HTTPS Support** - Secure connections
- **CORS Configuration** - Restricted origin access

## 📊 Scalability

- Supports 50+ concurrent users per session
- Multiple session support
- Horizontal scaling ready
- Load balancer compatible

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Server settings
HOST = 'localhost'
PORT = 5000
DEBUG = True

# Canvas settings
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
MAX_STROKE_WIDTH = 20

# Session settings
SESSION_TIMEOUT = 3600  # 1 hour
AUTO_SAVE_INTERVAL = 30  # 30 seconds
MAX_USERS_PER_SESSION = 100

# WebSocket settings
PING_TIMEOUT = 60
PING_INTERVAL = 25
```

## 🤝 Contributing

Contributions are welcome and appreciated!

```bash
# 1. Fork the repository
# 2. Create feature branch
git checkout -b feature/YourFeature

# 3. Make improvements
# 4. Commit changes
git commit -m 'Add YourFeature'

# 5. Push to branch
git push origin feature/YourFeature

# 6. Open Pull Request
```

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Naman Bhade** - [GitHub Profile](https://github.com/NamanBhade09)

## 💡 Future Enhancements & Roadmap

- [ ] Mobile app (React Native/Flutter)
- [ ] Advanced shape library (polygons, bezier curves)
- [ ] Image import and embedding
- [ ] Audio/Video chat integration
- [ ] AI-powered shape recognition
- [ ] Template and stencil library
- [ ] Presentation mode for slideshows
- [ ] Layer management system
- [ ] Grid and snap-to-grid options
- [ ] Custom brush styles
- [ ] Animation support
- [ ] Comment and annotation system
- [ ] Cloud storage integration
- [ ] Offline mode support

## 🐛 Troubleshooting

### Drawing Not Visible
- **Solution**: Refresh the page (F5)
- Check browser compatibility (use latest Chrome/Firefox)
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)

### Connection Issues
- **Solution**: Verify Flask server is running
- Check internet connection stability
- Ensure WebSocket port (5000) is open
- Try disabling browser extensions
- Check firewall settings

### Slow Performance
- **Solution**: Close unused browser tabs
- Reduce brush size
- Clear session history
- Update browser to latest version
- Try different browser

### Session Not Saving
- **Solution**: Check server logs
- Verify disk space available
- Check file permissions
- Ensure database is running

## 📞 Support & Feedback

Have questions or suggestions?
- 📧 Open a GitHub Issue with detailed description
- 🐛 Report bugs with reproduction steps
- 💡 Share feature requests
- 🤝 Contribute improvements

---

⭐ **If this project helped you, please consider giving it a star!**

Made with ❤️ by Naman Bhade
