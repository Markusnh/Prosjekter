from numba import jit
import numpy as np
import time
import cv2



@jit
def blur(image):
    """
    This function takes in an image, finds its dimensions, and finds a blurred version of the image, and takes the time for how long the operation takes.
    It finds the blurred image by setting all the pixel values in the image to be the average pixel value of the surrounding pixels. It does this with the
    standard python implementation sped up with Numba's jit decorator.

    #args
    #image - an array of numbers that can be interpreted as an image by openCV, or as an Numpy matrix


    #returns
    The blurred version of the image sent to the function as argument
    The time the operation takes
    """
    

    #makes an empty matrix for the blurred pixel values to be stashed
    image2=np.zeros(image.shape, np.uint32)

    #doing the actual blurring of the pictures, by finding out the average pixel value of all the surrounding pixels, and then setting this pixels value to the average
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            for k in range(image.shape[2]):
                #finds the average of all the surrounding pixels(including the pixel itself)
                average=(image[i,j,k]+image[i-1,j,k]+image[i+1,j,k]+image[i,j-1,k]+image[i,j+1,k]+image[i-1,j-1,k]+image[i-1,j+1,k]+image[i+1,j-1,k]+image[i+1,j+1,k])/9
                #setting the blurred image-matrix's value to the average
                image2[i,j,k]=average

    return image2


if __name__=="__main__":
    #reads the image from file, converts it to 32 bit integers and padding it
    image=cv2.imread("beatles.jpg")
    image=image.astype(np.uint32)
    image=np.pad(image,pad_width=((1,1),(1,1),(0,0)), mode="edge")

    #tcalls the blur function and taking the time for how long it takes to blur it
    t1=time.time()
    image2=blur(image)
    t2=time.time()

    #prints out the time it takes to blur the image
    print(t2-t1)

    #shows the original picture
    image=image.astype(np.uint8)
    cv2.imshow("Heyao", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #shows the blurred image
    image2=image2.astype(np.uint8)
    cv2.imshow("Heyao", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
