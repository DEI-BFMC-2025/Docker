#!/usr/bin/env python3
import socket
import sys
from picamera2 import Picamera2

class DualSocketClient:
    # Define socket paths as class constants
    SOCKET_BRAIN = "/tmp/bfmc_socket.sock"
    SOCKET_DASHBOARD = "/tmp/bfmc_socket2.sock"

    def __init__(self, config):
        self.camera = self.initialize_camera(config)
        self.brain_sock = None
        self.dashboard_sock = None
        self.brain_connected = False
        self.dashboard_connected = False

    def initialize_camera(self, config):
        camera = Picamera2()
        print(camera.camera_properties["PixelArraySize"])
        config = camera.create_preview_configuration(config)
        camera.configure(config)
        camera.start()
        return camera

    def handle_connection(self, sock_obj, connected_flag, socket_path):
        """Manage connection state for a single socket"""
        try:
            if not connected_flag:
                if sock_obj:
                    sock_obj.close()
                new_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                new_sock.settimeout(5)  # Non-blocking connect attempt
                new_sock.connect(socket_path)
                new_sock.settimeout(None)
                print(f"Connected to {socket_path}")
                return new_sock, True
            return sock_obj, True
        except (socket.error, ConnectionRefusedError):
            return sock_obj, False

    def send_data(self, sock_obj, connected_flag, socket_path, data):
        """Send data to a single socket"""
        if not connected_flag:
            return False
        
        try:
            sock_obj.sendall(data)
            return True
        except (BrokenPipeError, socket.error):
            print(f"Connection lost on {socket_path}")
            sock_obj.close()
            return False

    def run(self):
        """Main application loop"""
        try:
            print("Starting frame streaming...")
            while True:
                # Capture single frame for both sockets
                frame_data = self.camera.capture_array("main").tobytes()

                # Handle brain socket
                self.brain_sock, self.brain_connected = self.handle_connection(
                    self.brain_sock, self.brain_connected, self.SOCKET_BRAIN
                )
                if self.brain_connected:
                    self.brain_connected = self.send_data(
                        self.brain_sock, self.brain_connected,
                        self.SOCKET_BRAIN, frame_data
                    )

                # Handle dashboard socket
                self.dashboard_sock, self.dashboard_connected = self.handle_connection(
                    self.dashboard_sock, self.dashboard_connected, self.SOCKET_DASHBOARD
                )
                if self.dashboard_connected:
                    self.dashboard_connected = self.send_data(
                        self.dashboard_sock, self.dashboard_connected,
                        self.SOCKET_DASHBOARD, frame_data
                    )

        except KeyboardInterrupt:
            print("\nInterrupted! Closing the client...")
        finally:
            if self.brain_sock: self.brain_sock.close()
            if self.dashboard_sock: self.dashboard_sock.close()
            print("All sockets closed")

if __name__ == "__main__":
    config = {
        "size": (320, 240),
        "format": "RGB888",
    }

    client = DualSocketClient(config)
    client.run()