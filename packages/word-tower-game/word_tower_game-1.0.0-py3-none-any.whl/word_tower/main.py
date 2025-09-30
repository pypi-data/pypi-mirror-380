#!/usr/bin/env python3
"""
Word Tower Game - Main Entry Point
==================================

This module provides the main entry point for the Word Tower game.
It starts both the backend server and serves the frontend static files.
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from pathlib import Path


def find_free_port(start_port=8000):
    """Find a free port starting from start_port."""
    import socket
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return start_port


def run_backend():
    """Run the backend server."""
    # Add current directory to Python path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    # Import and run the game manager
    try:
        from .app.ws.game_manager import sio, app
        import uvicorn
        
        # Add static file serving for frontend
        from fastapi import FastAPI
        from fastapi.staticfiles import StaticFiles
        from fastapi.responses import FileResponse
        
        # Create FastAPI app to serve static files
        web_app = FastAPI()
        
        # Serve static files
        static_path = current_dir / "static"
        if static_path.exists():
            web_app.mount("/assets", StaticFiles(directory=static_path / "assets"), name="assets")
            
            @web_app.get("/")
            async def serve_index():
                return FileResponse(static_path / "index.html")
            
            @web_app.get("/{path:path}")
            async def serve_static(path: str):
                file_path = static_path / path
                if file_path.exists() and file_path.is_file():
                    return FileResponse(file_path)
                return FileResponse(static_path / "index.html")
        
        # Mount Socket.IO app
        import socketio
        combined_app = socketio.ASGIApp(sio, web_app)
        
        port = find_free_port(8000)
        print(f"🚀 Starting Word Tower on http://localhost:{port}")
        print(f"🎮 Open your browser and visit: http://localhost:{port}")
        
        # Auto-open browser after 1 second
        threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{port}")).start()
        
        uvicorn.run(combined_app, host="0.0.0.0", port=port, log_level="info")
    except ImportError as e:
        print(f"❌ Error importing backend modules: {e}")
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)


def run_game():
    """
    Main entry point for the Word Tower game.
    This function is called when user runs: word-tower
    """
    print("🏗️  Word Tower - Multiplayer Word Game")
    print("=" * 40)
    print("🎮 Starting game server...")
    
    try:
        run_backend()
    except KeyboardInterrupt:
        print("\n👋 Game server stopped. Thanks for playing!")
    except Exception as e:
        print(f"❌ Error starting game: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_game()