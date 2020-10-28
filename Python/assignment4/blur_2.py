import cv2
import numpy as np
import time

def blur(image):
    """
    This function takes in an image, finds its dimensions, and finds a blurred version of the image, and takes the time for how long the operation takes.
    It finds the blurred image by setting all the pixel values in the image to be the average pixel value of the surrounding pixels. It does this with vector
    operation adding shifted versions of the image with each other to set the pixels to the average value of the surrounding pixel values.

    #args
    #image - an array of numbers that can be interpreted as an image by openCV, or as an Numpy matrix


    #returns
    The blurred version of the image sent to the function as argument
    The time the operation takes
    """
    #makes an empty matrix for the blurred pixel values to be stashed in
    image2=np.zeros(image.shape, np.uint32)

    #convets the image ints to be 32 bit instead of 8 as it originally is
    image=image.astype(np.uint32)


    #finds out the shape/dimensions of the image
    xlen=image.shape[0]
    ylen=image.shape[1]
    zlen=image.shape[2]

    #padding the image, so that we can just add the different images togheter shifted by one pixel at a time
    image=np.pad(image,pad_width=((1,1),(1,1),(0,0)), mode="edge")

    #takes time before calculation
    t1=time.time()

    #shifting the image by one pixel at a time, and adding them all togheter
    image2+=image[0:xlen,0:ylen,:]
    image2+=image[0:xlen,1:ylen+1,:]
    image2+=image[0:xlen,2:ylen+2,:]
    image2+=image[1:xlen+1,0:ylen,:]
    image2+=image[1:xlen+1,1:ylen+1,:]
    image2+=image[1:xlen+1,2:ylen+2,:]
    image2+=image[2:xlen+2,0:ylen,:]
    image2+=image[2:xlen+2,1:ylen+1,:]
    image2+=image[2:xlen+2,2:ylen+2,:]
    image2=image2/9

    #endtime
    t2=time.time()

    #converts it back to 8 bit integers
    image2=image2.astype(np.uint8)
    return image2, t2-t1

if __name__=="__main__":

    #reads the image from file and calls the blur function on it, and prints out how long time it takes
    image=cv2.imread("beatles.jpg")
    image2, t=blur(image)
    print(t)

    #shows the original picture
    image=image.astype(np.uint8)
    cv2.imshow("Heyao", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #shows the blurred image
    cv2.imshow("Heyao", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
