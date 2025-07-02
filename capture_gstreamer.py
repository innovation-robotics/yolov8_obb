# ...existing code...
import cv2

def main():
    cap = cv2.VideoCapture('tcpclientsrc host=192.168.1.245 port=7001 ! decodebin ! queue ! videoconvert ! videoscale ! video/x-raw,width=1280,height=720 ! appsink drop=1', cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    img_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('s'):
            filename = f"data_for_training/image_{img_count}.png"
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            img_count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
#