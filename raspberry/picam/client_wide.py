#!/usr/bin/env python3
import socket
import numpy as np
import time
import sys
from picamera2 import Picamera2
from libcamera import Transform

class UnixSocketClient:
    def __init__(self, socket_addr, retry_interval=1):
        self.socket_addr = socket_addr
        self.retry_interval = retry_interval
        self.camera = self.initialize_camera()
        self.sock = None

    def initialize_camera(self):
        camera = Picamera2()
        # Use sensor mode 2 for full resolution
        mode = camera.sensor_modes[2]
        q_w = mode['size'][0] 
        q_h = mode['size'][1] 
        q_size = (q_w, q_h)
        print("DIMENSIONSSSSSSSSSSSSSSSSSSSSSSS")
        print(q_w, q_h)
        # Create still configuration with sensor settings and transform
        config = camera.create_preview_configuration(
            #transform=Transform(hflip=0, vflip=0),
            sensor={
                'output_size': q_size,
                'bit_depth': mode['bit_depth']
            }
        )
        #camera.align_configuration(config)
        camera.configure(config)
        camera.start()
        return camera

    def wait_for_server(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.connect(self.socket_addr)
                print("Connected to server.")
                break
            except socket.error:
                print(f"Camera ready to send frames, waiting for communication on the socket. Retrying in {self.retry_interval} second(s)...")
                time.sleep(self.retry_interval)

    def reconnect_on_broken_pipe(self):
        print("Broken pipe detected, attempting to reconnect...")
        if self.sock:
            self.sock.close()
        self.wait_for_server()

    def send_frames(self):
        try:
            while True:
                array = self.camera.capture_array("main")
                arr2_pack = array.tobytes()

                try:
                    self.sock.sendall(arr2_pack)
                except (BrokenPipeError, socket.error):
                    self.reconnect_on_broken_pipe()
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    time.sleep(2)
                    
        except KeyboardInterrupt:
            print("\nInterrupted! Closing the client...")
        finally:
            self.close_socket()

    def close_socket(self):
        if self.sock:
            self.sock.close()
            print("Socket closed!")

if __name__ == "__main__":
    socket_addr = "/tmp/bfmc_socket.sock"
    client = UnixSocketClient(socket_addr, retry_interval=2)

    try:
        client.wait_for_server()
        client.send_frames()
    except KeyboardInterrupt:
        print("\n Exiting ...")
        client.close_socket()
        sys.exit(0)