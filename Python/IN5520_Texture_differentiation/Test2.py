from imageio import imread, imwrite
import matplotlib.pyplot as plt
#from matplotlib.image import imread
import matplotlib.cm as cm
import numpy as np
import sys

def calculate_GLCM(window, d, theta):
    """
    This method calculates the GLCM with the given parameters
    """

    theta_in=theta
    theta=(theta/360)*2*np.pi
    GLCM_matrix=np.zeros((16,16))

    #find the correct indexes in the for-loop according to the angle and distance given
    if theta_in>=0 and theta_in<=90:
        startindexi=0
        endindexi=window.shape[0]-int(np.cos(theta)*d)
        startindexj=0
        endindexj=window.shape[1]-int(np.sin(theta)*d)
    elif theta_in>90 and theta_in<=180:
        startindexi=abs(int(np.cos(theta)*d))
        endindexi=window.shape[0]
        startindexj=0
        endindexj=window.shape[1]-int(np.sin(theta)*d)
    elif theta_in>180 and theta_in<=270:
        startindexi=abs(int(np.cos(theta)*d))
        endindexi=window.shape[0]
        startindexj=abs(int(np.sin(theta)*d))
        endindexj=window.shape[1]
    elif theta_in>270 and theta_in<=360:
        startindexi=0
        endindexi=window.shape[0]-int(np.cos(theta)*d)
        startindexj=abs(int(np.sin(theta)*d))
        endindexj=window.shape[1]


    for i in range(startindexi, endindexi):
        for j in range(startindexj, endindexj):
            #find the value of the two chosen pixels and put them into the GLCM matrix
            pixel1=window[i,j]
            pixel2=window[i+int(np.cos(theta)*d),j+int(np.sin(theta)*d)]
            GLCM_matrix[pixel1,pixel2]+=1
    #make it symmetrical
    GLCM_matrix=(GLCM_matrix+GLCM_matrix.T)
    summ=np.sum(GLCM_matrix)
    #normalize it
    GLCM_matrix=GLCM_matrix/float(summ)
    return GLCM_matrix

def create_feature_map(image, window_size, d, theta):
    #this matrix will be filled with the feature-scalars
    feature_map=np.zeros((image.shape[0], image.shape[1]))

    #have to remove half of the window size at the edges of the image
    index=int(window_size/2)


    for i in range(index, image.shape[0]-index):
        for j in range(index, image.shape[1]-index):
            #create the window according to the window size
            window=image[i-index:i+index, j-index:j+index]
            #calcualte the GLCM
            GLCM=calculate_GLCM(window, d, theta)
            #set in the values to the feature-map
            feature_map[i,j]=IDM(GLCM)

    return feature_map


#implementing the IDM algorithm from a GLCM matrix
def IDM(GLCM):
    s=0
    for i in range(GLCM.shape[0]):
        for j in range(GLCM.shape[1]):
            s=s+(1.0/(1+(i-j)**2))*GLCM[i,j]
    s=s/(GLCM.shape[0]*GLCM.shape[1])
    return s

#implementing the inertia feature function from a GLCM-matrix
def inertia(GLCM):
    s=0
    for i in range(GLCM.shape[0]):
        for j in range(GLCM.shape[1]):
            s=s+((i-j)**2*GLCM[i,j])
    s=s/(GLCM.shape[0]*GLCM.shape[1])
    return s

#implementing the SHD algorithm from a GLCM-matrix
def SHD(GLCM):
    mux=0
    muy=0
    for i in range(GLCM.shape[0]):
        for j in range(GLCM.shape[1]):
            mux=mux+i*GLCM[i,j]
            muy=muy+j*GLCM[i,j]
    mux=mux/(GLCM.shape[0]*GLCM.shape[1])
    muy=muy/(GLCM.shape[0]*GLCM.shape[1])

    s=0
    for i in range(GLCM.shape[0]):
        for j in range(GLCM.shape[1]):
            s+=((i+j-mux-muy)**3)*GLCM[i,j]
    s=s/(GLCM.shape[0]*GLCM.shape[1])
    return s




if __name__=="__main__":
    #take in parameters from user
    filename=sys.argv[1]
    d=int(sys.argv[1])
    theta=int(sys.argv[2])
    filename=sys.argv[3]
    #read an image to do texture analysis
    image=imread("mosaic2.png")

    #convert the image it to 16 gray-values
    for j in range(image.shape[0]):
        for k in range(image.shape[1]):
            image[j][k]=int(image[j][k]/16)

    window_size=41

    feature_map=create_feature_map(image, window_size, d, theta)

    #scale the feature-map
    mini=np.min(feature_map)
    maxi=np.max(feature_map)
    feature_map=((feature_map-mini)/maxi)*255
    feature_map=feature_map.astype(np.uint8)

    #write the feature-map to file
    imwrite(filename, feature_map)
    """
    from playsound import playsound

    #takes very long to create the GLCM-features, so play thus tune to know that it is done
    playsound("in5520\\Daft Punk - Instant Crush.mp3")
    """
    plt.imshow(feature_map)
    plt.show()
    """
    plt.hist(feature_map)
    plt.show()
    """
