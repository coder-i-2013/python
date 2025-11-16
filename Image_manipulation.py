import cv2 
import numpy as np
import matplotlib.pyplot as plt

image= cv2.imread("C:/Users/symbi/Downloads/sunset.jpg")
choice=int(input("Enter a number 1-5: "))

if choice==1:
    # turning BGR to RGB
    image_rgb= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.show()

elif choice==2:
    # Gray scaling the image 
    gray_image =cv2.cvtColor(image, cv2.COlOR_BGR2GRAY)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.show()
elif choice==3:
    # Cropping the image 
    cropped_image= image[100:300 ,200:400]
    cropped_rgb = cv2.cvtColor(cropped_image,COLOR_BGR2RGB)
    plt.imshow(cropped_rgb)
    plt.title("Cropped Reigon")
    plt.show()

elif choice==4:
    # Rotating the image 
    (h,w)- image.shape[:2]
    center=( w //2, h//2)
    M=cv2.getRotationMatrix2D(center,45,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))
    rotated_rgb =cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
    plt.imshow(rotated_rgb)
    plt.title("Rotated Image")
    plt.show()

elif choice==5:
    # Increasing Bightness 
    brightness_matrix=np.ones(image.shape,dtype="unit8")*50
    brighter= CV2.add(image,brightness_matrix)
    brighter_rgb=cv2.CvtColor(brigter,cv2.COLOR_BGR2RGB)
    plt.imshow(brighter_rgb)
    plt.title("Brighter Image")
    plt.show()
    

print('If you want to go again:')
choice=int(input("Enter a number 1-5: ")) 



