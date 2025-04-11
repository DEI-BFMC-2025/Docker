import socket
import time

def stream_to_socket(socket_path: str, shared_frame):
    sock = None
    connected = False

    while True:
        try:
            if not connected:
                if sock:
                    sock.close()
                sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect(socket_path)
                sock.settimeout(None)
                print(f"[{socket_path}] Connected.")
                connected = True

            frame = shared_frame.read()
            if frame:
                try:
                    sock.sendall(frame)
                except (BrokenPipeError, socket.error):
                    print(f"[{socket_path}] Disconnected while sending.")
                    sock.close()
                    connected = False

        except (ConnectionRefusedError, FileNotFoundError, socket.error):
            print(f"[{socket_path}] Unable to connect. Retrying...")
            time.sleep(0.01)
            connected = False
