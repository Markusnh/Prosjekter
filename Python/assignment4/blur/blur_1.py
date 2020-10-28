import cv2
import numpy as np
import time


def blur(image):

    #Finding out the dimensions of the image used in the for-loop below
    xlen=image.shape[0]
    ylen=image.shape[1]
    zlen=image.shape[2]

    #converts the image to uint32 just to make sure there is no overflow
    image2=np.zeros(image.shape, np.uint32)

    #padding it so that we can blur the edge-pixels as well
    image=np.pad(image,pad_width=((1,1),(1,1),(0,0)), mode="edge")

    #takes the time before the actual calculation
    t1=time.time()


    for i in range(1,xlen):
        for j in range(1,ylen):
            for k in range(zlen):
                #finds the average of the 8 surrounding pixels and the pixel itself
                #by adding all the pixel values(of the pixels surrounding) and dividing by 9
                average=(image[i,j,k]+image[i-1,j,k]+image[i+1,j,k]+image[i,j-1,k]+image[i,j+1,k]+image[i-1,j-1,k]+image[i-1,j+1,k]+image[i+1,j-1,k]+image[i+1,j+1,k])/9
                #sets the pixel of image2 to the calculated average
                image2[i,j,k]=average
    #takes the time after calculation
    t2=time.time()
    #returns image and time taken to do the calculation
    return image2, t2-t1



if __name__=="__main__":
    #loading in the picture
    image=cv2.imread("beatles.jpg")
    image=image.astype(np.uint32)

    #calls the blur function
    image2,t=blur(image)
    print(t)


    #Shows the original picture
    image=image.astype(np.uint8)
    cv2.imshow("Heyao", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Shows the blurred picture
    image2=image2.astype(np.uint8)
    cv2.imshow("Heyao", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
