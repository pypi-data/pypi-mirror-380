# PeerPyRTC

**A simple, modern Python library for building the backend of real-time WebRTC DataChannel applications.**

PeerPyRTC provides a high-level Python API to abstract away the complexities of WebRTC signaling, allowing you to build a robust backend for peer-to-peer data communication with ease. It's designed to be modular, flexible, and easy to integrate with any Python web framework.

This package contains the **backend library**. The corresponding frontend JavaScript library is available as `peerpyrtc-client` on npm.

## Features

-   **High-Level Abstraction**: A simple, intuitive API for managing WebRTC signaling.
-   **Framework-Agnostic**: Easily integrates with Flask, FastAPI, Django, or any other Python web framework.
-   **Automatic Message Relay**: Messages sent by one peer are automatically and efficiently broadcast to all other peers in the same room.
-   **Backend Message Handling**: An elegant decorator-based system (`@SignalingManager.message_handler`) allows your backend to process, persist, or moderate messages.
-   **Server-Sent Broadcasts**: Includes a `Broadcaster` utility for the backend to send messages to all clients in a room.
-   **Zero-Config TURN Servers**: Comes with default TURN servers pre-configured to help traverse restrictive firewalls.

## Installation

```bash
pip install peerpyrtc
```

## Quick Start

This example demonstrates how to set up a minimal WebRTC signaling server using Flask.

```python
from flask import Flask, request, jsonify
from peerpyrtc import SignalingManager

app = Flask(__name__)
signaling_manager = SignalingManager()

# Endpoint to handle the initial offer from a client
@app.route("/offer", methods=["POST"])
def offer():
    # The offer method takes the room, peer_id, and offer from the request
    # and returns the corresponding answer.
    return jsonify(signaling_manager.offer(**request.json))

# Endpoint to handle ICE candidates
@app.route("/candidate", methods=["POST"])
def candidate():
    signaling_manager.candidate(**request.json)
    return jsonify({"status": "ok"})

# Endpoint for a peer leaving a room
@app.route("/leave", methods=["POST"])
def leave():
    signaling_manager.leave(**request.json)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Backend API Reference

### `SignalingManager`

The main class for managing rooms and signaling on the backend.

`__init__(self, debug=False)`
:   Initializes the signaling manager. Set `debug=True` to enable detailed logging from the library.

`offer(self, room: str, peer_id: str, offer: dict) -> dict`
:   Processes a WebRTC offer from a client. Creates a room if it doesn't exist and returns an SDP answer to be sent back to the client.

`candidate(self, room: str, peer_id: str, candidate: dict)`
:   Processes an ICE candidate received from a client.

`leave(self, room: str, peer_id: str)`
:   Handles a peer leaving a room and performs cleanup. If a room becomes empty, it is automatically removed.

#### Backend Message Handling with `@message_handler`

While peers communicate directly (P2P), you often need the backend to be aware of messages for persistence (database), moderation, or analytics. The `@message_handler` decorator provides a "tap" into the message stream without interrupting the real-time P2P flow.

The decorated `async` function receives a copy of every message sent between peers.

**Example: Saving All Messages to a Database**
```python
import asyncio
from peerpyrtc import SignalingManager

# In a real app, this would be your actual database client
class MockDatabase:
    async def save_message(self, room, user, text):
        print(f"Saving to DB: Room({room}) | {user}: {text}")
        await asyncio.sleep(0.1) # Simulate async DB write

db = MockDatabase()
signaling_manager = SignalingManager()

@signaling_manager.message_handler
async def save_all_messages(room_name: str, sender_id: str, message: str):
    """
    This function is called for every message sent in any room.
    """
    await db.save_message(room_name, sender_id, message)

```

### `Broadcaster`

A helper class to broadcast messages from the backend to all clients in a room.

`__init__(self, signaling_manager: SignalingManager)`
:   Initializes the broadcaster, linking it to your `SignalingManager` instance.

`broadcast(self, room_name: str, message: str)`
:   Sends a message to all peers currently in the specified room.

## Full Examples

The official GitHub repository contains several full-stack examples that demonstrate how to use this backend library with its corresponding frontend JavaScript library. These examples are the best place to see the library in action.

-   **Chat**: A full-featured, multi-room chat application.
-   **Terminal Chat**: A unique example where the Python backend can act as a participant in the chat.
-   **Whiteboard**: A real-time collaborative whiteboard.
-   **Echo**: A simple echo client for testing connectivity.