#kiti submission, converting the image to grayscale
import cv2

img = cv2.imread('image.jpg')

# Verifying the image loaded successfully to prevent errors
if img is not None:
    
    # Converting the loaded image from BGR (color) to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Displaying the new grayscale image in a window
    cv2.imshow('Grayscale Image', gray_img)

    # Waiting for any key press, then close the window properly
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Error: Could not find 'image.jpg'. Make sure it is in the same folder as this script.")