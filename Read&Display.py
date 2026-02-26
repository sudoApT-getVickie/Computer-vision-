#kiti submission , reading and displaying the image 
import cv2

# Loading the image
img = cv2.imread('image.jpg')

# Checking if the image was loaded successfully (good practice)
if img is None:
    print("Error: Could not read 'image.jpg'. Make sure it's in the same folder.")
else:
    #Displaying the image in a window
    cv2.imshow('Original Image', img)

    #for any key press, then close the window properly
    cv2.waitKey(0) 
    cv2.destroyAllWindows()