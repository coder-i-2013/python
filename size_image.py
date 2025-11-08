import cv2
def main():
    image_path = "input_image.jpg"
    cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return
    print("Original image loaded sucsessfully")

    sizes= {
        'small': (200,200)
        'medium': (400,400)
        'large': (600,600)
    }

    for size name,dimensions in sizes.items():
        resized = cv2.resize(image,dimensions) 
        cv2.imshow(f"{size_name.capitalize}")
        cv2.imwrite(f"input_image_{size_name}.jpg",resized_)
        print(f"image resized to" )
        print(f"Resized image saved as {dimensions[0]}x{dimensions[1]} pixels ({size_name}).")

        print("Opening resized images. Press any key in the image window to close.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image windows closed. Process completed successfully.")

if __name__ == "__main__":
    main()

