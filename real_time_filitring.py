import cv2
import numpy as np

def apply_color_filter(cap,filter_type):
    img=cap.copy()
    if filter_type=='original':
        return img
    elif filter_type == 'red_tint':
        # Remove blue and green channels for red tint
        img[:, :, 1] = 0 # Green channel
        img[:, :, 0] = 0 # Blue channel  
    elif filter_type == 'blue_tint':
        img[:, :, 1] = 0 # Green channel
        img[:, :, 2] = 0 # Red channel
    elif filter_type == 'green_tint':
        img[:, :, 0] = 0 # Blue channel  
        img[:, :, 2] = 0 # Red channel  
    elif filter_type == 'increase_red':
        # Increase the intensity of the red channel
        img[:, :, 2] = cv2.add(img[:, :, 2], 50) 
    elif filter_type == 'decrease_blue':
        # Increase the intensity of the red channel
        img[:, :, 0] = cv2.subtract(img[:, :, 0], 50) 
    elif filter_type == "sobel":
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.bitwise_or(sx.astype('uint8'), sy.astype('uint8'))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)
    
    elif filter_type == "cartoon":
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color=cv2.bilateralFilter(cap, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img  
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    filter_type = "original"
    print("Keys: r=Red, g=Green, b=Blue, s=Sobel, c=Canny, t=Cartoon, q=Quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break
        out = apply_color_filter(frame, filter_type)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('s'):
            filter_type = "sobel"
        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('t'):
            filter_type = "cartoon"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
     main()
            


        


