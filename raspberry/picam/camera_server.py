from multiprocessing import Process
from shared_frame import SharedFrame
from picamera2 import Picamera2
import socket_streamer
import time

def start_camera(shared_frame: SharedFrame):
    cam = Picamera2()
    config = cam.create_preview_configuration({
        "size": (320, 240),
        "format": "RGB888"
    })
    cam.configure(config)
    cam.start()

    while True:
        try:
            frame = cam.capture_array("main").tobytes()
            shared_frame.write(frame)
        except Exception as e:
            print(f"Camera error: {e}")

if __name__ == "__main__":
    max_frame_size = 320 * 240 * 3  # RGB888 format
    shared_frame = SharedFrame(max_frame_size)

    camera_proc = Process(target=start_camera, args=(shared_frame,))
    brain_proc = Process(target=socket_streamer.stream_to_socket, args=("/tmp/bfmc_camera_brain.sock", shared_frame))
    dash_proc = Process(target=socket_streamer.stream_to_socket, args=("/tmp/bfmc_camera_dashboard.sock", shared_frame))

    camera_proc.start()
    brain_proc.start()
    dash_proc.start()

    try:
        camera_proc.join()
        brain_proc.join()
        dash_proc.join()
    except KeyboardInterrupt:
        print("Shutting down...")
        camera_proc.terminate()
        brain_proc.terminate()
        dash_proc.terminate()
