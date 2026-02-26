#kiti submission, combining the Read&Display and Grayscale code
import cv2
# Loading the image
img = cv2.imread('image.jpg')

if img is None:
    print("Error: Could not read 'image.jpg'.")
else:
    # Displaying the original image
    cv2.imshow('Original Image', img)
    
    #  press any key to move to the next step
    print("Press any key on the image window to continue to Grayscale...")
    cv2.waitKey(0) 

    # Converting the loaded image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Displaying the grayscale image
    cv2.imshow('Grayscale Image', gray_img)

    # for any key press the windows are closed 
    print("Press any key on the image window to exit...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()