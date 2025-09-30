# PeerPyRTC

**A serverless, Socket.io-compatible WebRTC library for building real-time peer-to-peer applications.**

PeerPyRTC is a revolutionary WebRTC DataChannel library that **replaces WebSockets** with true peer-to-peer communication. Build chat apps, games, collaborative tools, and real-time dashboards without persistent server connections.

## 🚀 Key Features

-   **🔄 Socket.io Replacement**: Drop-in replacement with `emit()`, `broadcast()`, and event-driven architecture
-   **⚡ Serverless Architecture**: True P2P after initial signaling - no persistent server needed
-   **🎯 Real-time Peer Management**: Automatic join/leave detection, host election, room state sync
-   **🛡️ Production Ready**: Built-in TURN servers, reconnection, error handling, and failover
-   **🔧 Framework Agnostic**: Works with Flask, FastAPI, Django, Express.js, or any web framework
-   **📡 Event-Driven**: Comprehensive callback system for peer events and room management
-   **🎮 Multi-Purpose**: Perfect for chat, gaming, collaboration, IoT, trading, video conferencing

## 📦 Installation

```bash
pip install peerpyrtc
```

## 🚀 Quick Start

```python
from flask import Flask, request, jsonify
from peerpyrtc import SignalingManager

app = Flask(__name__)
signaling_manager = SignalingManager(debug=True)

# Handle all messages
@signaling_manager.message_handler
async def on_message(room: str, peer_id: str, message: str):
    print(f"Message in {room} from {peer_id}: {message}")

# Handle peer events
@signaling_manager.peer_joined_handler
async def on_peer_joined(room: str, peer_id: str, peer_info: dict):
    print(f"🟢 {peer_id} joined {room}")

@signaling_manager.peer_left_handler
async def on_peer_left(room: str, peer_id: str, peer_info: dict):
    print(f"🔴 {peer_id} left {room}")

# Standard WebRTC signaling endpoints
@app.route("/offer", methods=["POST"])
def offer():
    return jsonify(signaling_manager.offer(**request.json))

@app.route("/candidate", methods=["POST"])
def candidate():
    signaling_manager.candidate(**request.json)
    return jsonify({"status": "ok"})

@app.route("/leave", methods=["POST"])
def leave():
    signaling_manager.leave(**request.json)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## 📚 API Reference

### SignalingManager

```python
from peerpyrtc import SignalingManager

# Initialize
signaling_manager = SignalingManager(debug=True)

# Core signaling methods
signaling_manager.offer(room, peer_id, offer)      # Handle WebRTC offer
signaling_manager.candidate(room, peer_id, candidate) # Handle ICE candidate
signaling_manager.leave(room, peer_id)              # Handle peer leaving

# Room information
signaling_manager.rooms_info()                     # Get all rooms info
signaling_manager.get_room_peers(room_name)        # Get peers in specific room
```

### Event Handlers (Decorators)

```python
# Message handling
@signaling_manager.message_handler
async def on_message(room_name: str, sender_id: str, message: str):
    # Process every message sent in any room
    await database.save_message(room_name, sender_id, message)

# Peer lifecycle events
@signaling_manager.peer_joined_handler
async def on_peer_joined(room_name: str, peer_id: str, peer_info: dict):
    # Handle peer joining (real-time, no polling needed)
    print(f"New peer {peer_id} joined {room_name}")
    await notify_other_services(peer_id, 'joined')

@signaling_manager.peer_left_handler
async def on_peer_left(room_name: str, peer_id: str, peer_info: dict):
    # Handle peer leaving (automatic detection)
    print(f"Peer {peer_id} left {room_name}")
    await cleanup_user_data(peer_id)
```

**Built with ❤️ for developers who want WebSocket performance without WebSocket complexity.**