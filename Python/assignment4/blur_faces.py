import cv2
import numpy as np
from blur_2 import blur



def blur_face(image):
    """
    This function takes in an image as argument, runs a facial recognintion algorithm on the image and detects faces in it.
    If no faces are recognized this function doesnt do anything to the original picture. If faces are recognized, the faces that are recognized gets blurred
    and the blurred versions of the faces are put into the original picture and the original picture with the blurred faces are returned, together with the Boolean.
    If faces are recognized the end-variable is False, else it returns is as True.
    #args
    -image - an array of numbers that can be interpreted as an image by openCV, or as an Numpy matrix


    #returns
    -The version of the image where allt he detected faces are blurred to the point that the face-recognintion algorithm cant recognize the faces anymore

    -A boolean value for determining wheter or not the algorithm managed to recognize any faces in the picture
    """

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #all the recognized faces end up in this variable/object
    faces = faceCascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5)#, minSize=(30, 30))

    #this is used to check if there are any faces that are recognized
    #if faces is a tuple, means there are no elements in faces
    #the return value end is used to stop more calls to this function in the for loop below this function (inside the if statement)
    if type(faces) is tuple:
        return image, True

    #I made a empty list, where the images of the faces will be put. We will loop through these images and blur them later
    images=[]
    for (x, y, w, h) in faces:
        images.append(image[y:y+h+1,x:x+w+1,:])

    #this can be used to have a green rectangle around the faces, so that one can see what the algorithm has recognized
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #this list is used to store the blurred images of the faces
    blurred_images=[]

    #looping through the list of images of the faces
    for i in images:
        #
        #i=i.astype(np.uint8)
        for j in range(10):
            #blur the image of the face
            i,t=blur(i)

        #add the blurred image of the face to the blurred_images list
        blurred_images.append(i)

    #here we insert the blurred faces into the original image.The way we do this is by setting the pixel values
    #where the faces are to the pixel values of the blurred faces.
    #we have to use a counter to access the different elements of the list blurred_images
    counter=0
    for (x, y, w, h) in faces:
        image[y:y+h+1,x:x+w+1,:]=blurred_images[counter]
        counter+=1
    #here we return the image where the faces are blurred, and end=False. When end becomes True, the function is not called anymore
    #since then there are noe more faces that are detected
    return image, False


if __name__=='__main__':
    #load image from file
    image=cv2.imread("beatles.jpg")

    #we blur the image once, to get a value for end. Coul have set it to True manually, but might as well just call the blur function
    blurred, end=blur_face(image)

    #we have a counter here to see how many times the faces have to be blurred before the facial recognition algorithm doesnt recognize them anymore
    counter=0

    #here we blur the faces until end becomes True, then hte while loop stops
    while end==False:
        blurred, end=blur_face(blurred)
        counter+=1

    #print out how many times we had to blur the images
    print(counter)

    #show the image with the blurred faces
    cv2.imwrite("Blurred_faces.jpg",blurred)
    cv2.imshow("Heyao", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
