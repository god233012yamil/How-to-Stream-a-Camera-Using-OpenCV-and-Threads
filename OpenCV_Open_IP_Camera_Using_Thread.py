import cv2
import threading
from typing import Optional, Tuple

class RTSPCameraStream:
    """
    A class to handle RTSP camera streaming using OpenCV and threading.
    """

    def __init__(self, user: str, password: str, ip: str, port: int, stream_path: str):
        """
        Initialize the RTSPCameraStream object.

        Args:
            user (str): Username for RTSP authentication.
            password (str): Password for RTSP authentication.
            ip (str): IP address of the camera.
            port (int): Port number for the RTSP stream.
            stream_path (str): Path to the specific stream on the camera.
        """
        self.url = f"rtsp://{user}:{password}@{ip}:{port}/{stream_path}"
        self.cap = cv2.VideoCapture(self.url)
        self.is_running = False
        self.lock = threading.Lock()
        self.frame: Optional[Tuple[bool, cv2.Mat]] = None

    def start(self) -> None:
        """
        Start the camera stream in a separate thread.
        """
        self.is_running = True
        thread = threading.Thread(target=self._update_frame, args=())
        thread.start()

    def stop(self) -> None:
        """
        Stop the camera stream and release resources.
        """
        self.is_running = False
        if self.cap.isOpened():
            self.cap.release()

    def _update_frame(self) -> None:
        """
        Continuously update the current frame from the camera stream.
        This method runs in a separate thread.
        """
        while self.is_running:
            ret, frame = self.cap.read()
            with self.lock:
                self.frame = (ret, frame)

    def read(self) -> Tuple[bool, Optional[cv2.Mat]]:
        """
        Read the current frame from the camera stream.

        Returns:
            Tuple[bool, Optional[cv2.Mat]]: A tuple containing a boolean indicating
            if the frame was successfully read and the frame itself (if available).
        """
        with self.lock:
            if self.frame is not None:
                return self.frame
            return False, None

def main():
    """
    Main function to demonstrate the usage of RTSPCameraStream class.
    """
    # Replace these with your actual camera details
    user = "user"
    password = "password"
    ip = "192.168.1.60"
    port = 554  # Default RTSP port
    stream_path = "main"

    # Create and start the camera stream
    camera = RTSPCameraStream(user, password, ip, port, stream_path)
    camera.start()

    try:
        while True:
            ret, frame = camera.read()
            if ret:
                cv2.imshow("RTSP Camera Stream", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("Failed to get frame")
    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()