import cv2
import numpy as np

def apply_color_filter(image,filter_type):
    filtered_image=image.copy()

    if filter_type=='original':
        return filtered_image
    elif filter_type == 'red_tint':
        # Remove blue and green channels for red tint
        filtered_image[:, :, 1] = 0 # Green channel
        filtered_image[:, :, 0] = 0 # Blue channel  
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0 # Green channel
        filtered_image[:, :, 2] = 0 # Red channel
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0 # Blue channel  
        filtered_image[:, :, 2] = 0 # Red channel  
    elif filter_type == 'increase_red':
        # Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50) 
    elif filter_type == 'decrease_blue':
        # Increase the intensity of the red channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50) 
    return filtered_image

image= cv2.imread("C:/Users/symbi/Downloads/sunset.jpg")
if image is None:
    print("Not found")
else:
    filter_type='original'
    image=cv2.resize(image,(1200,800))
    print("o - Original")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")
    filter_name=input("Press the following keys to apply filters: ")
    while True:
        filtered_image= apply_color_filter(image,filter_type)
        cv2.imshow("filtered image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        if filter_name == 'o':
            filter_type="original"
        elif filter_name == 'r':
            filter_type='red_tint'
        elif filter_name == 'b':
            filter_type='blue_tint'
        elif filter_name == 'g':
            filter_type='green_tint'
        elif filter_name == 'i':
            filter_type='increase_red'
        elif filter_name == 'b':
            filter_type='decrease_blue'
        elif filter_name == 'q':
            print("Exiting..")
            break
        else:
            print("Error\n")
            print("Press the following keys to apply filters:")
            print("o - Original")
            print("r - Red Tint")
            print("b - Blue Tint")
            print("g - Green Tint")
            print("i - Increase Red Intensity")
            print("d - Decrease Blue Intensity")
            print("q - Quit")
    cv2.destroyAllWindows()
            


        


