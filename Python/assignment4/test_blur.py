#from blur.blur import blur_image
import numpy as np
import blur_2 as b2

def test_maxvalue():
    """
    This is a test function for testing that the maximum pixel value after blurring is lower than the maximum pixel value in the original image

    #args
    #no args


    #returns
    no return value
    """
    #making random image and blurring it
    image=np.random.rand(480,640,3)*255
    image=image.astype(np.uint32)
    image2,t=b2.blur(image)

    #Testing that the max value is smaller in the blurred image than in the original image
    max1=np.amax(image)
    max2=np.amax(image2)
    assert max2<max1

def test_pixelaverage():
    """
    This is a test function for asserting that a chosen pixel's value after blurring actually is the same as the average pixel value of the
    surrounding pixel values of the chosen pixel

    #args
    no args


    #returns
    no return value
    """
    #making random image and blurring it
    image=np.random.rand(480,640,3)*255
    image=image.astype(np.uint32)
    image2,t=b2.blur(image)

    #picking a random pixel and checking that the value is equal to the average value of the surrounding pixel values
    pixel_value=image2[250,350,:]
    i=250
    j=350
    for k in range(3):
        average=(image[i,j,k]+image[i-1,j,k]+image[i+1,j,k]+image[i,j-1,k]+image[i,j+1,k]+image[i-1,j-1,k]+image[i-1,j+1,k]+image[i+1,j-1,k]+image[i+1,j+1,k])/9

        #have to do this to avoid floating point numbers
        average=average.astype(np.uint32)
        assert pixel_value[k]==average
