import cv2
import time
import os

def capture_webcam_image(device="/dev/video0"):
    cap = cv2.VideoCapture(device)
    if not cap.isOpened():
        print(f"Error: cannot open webcam device at {device}")
        return
    
    # sleep for camera warm-up
    time.sleep(0.5)
    
    # cap one frame
    ret, frame = cap.read()
    if not ret:
        print("Error: failed to capture image")
        cap.release()
        return
    
    # save image
    output_filename = device.split('/')[-1] + '-capture.jpg'
    camera_id = int(device.split('/')[-1].split('video')[-1])
    cv2.imwrite(output_filename, frame)
    print(f"Image saved as {output_filename}")

    # release webcam
    cap.release()
    return camera_id
    
if __name__  == "__main__":
    os.system("rm -r video*.jpg")
    cam_list = []
    for i in range(18):
        id_ = capture_webcam_image(device=f"/dev/video{i}")
        if type(id_) == int:
            cam_list.append(id_)
    print(f"Cameras found on video:{cam_list}")
