import argparse
import cv2
import blur_1 as b1
import blur_2 as b2
import blur_3 as b3


def blur_image(input_filename, output_filename=None):
    image=cv2.imread(input_filename)
    image2,t=blur.blur(image)
    if output_filename!=None:
        cv2.imwrite(output_filename,image2)
    return image2


#initializing things
if __name__=="__main":
    #initializing argumentparser
    parser = argparse.ArgumentParser()

    #infilename must here be given, since there is not a default filename one can blur, thus to get the image file, one has to give the filename
    parser.add_argument('infilename', help='The filename of the image you want to have blurred')

    #outfilename is optional, if given the blurred picture will be saved as outfilename in folder
    parser.add_argument('--outfilename', help='The filename of saved blurred image')

    #This is not an optioanl argument, since there is no set default algorithm. Could have set the numpy implementation as the default, but haven't done it
    #thus algorithm must also be given as command line argument
    parser.add_argument('algorithm', help='[classical] - for (almost) pure python code [Numpy] - for the faster numpy implementation [Numba] - For the classical solution but sped up with the use of Numba')

    #all the arguments are in the object args
    args = parser.parse_args()

    #loads the image and sets the integerers as 32 bit
    image=cv2.imread(args.infilename)
    image=image.astype(np.uint32)

    #this if-statement checks what algorithm is to be used to blur the image, and does the necessary initializing for the chosen algorithm to be called.
    if args.algorithm=="classical" or args.algorithm=="Classical":
        image2, t=b1.blur(image)
    elif args.algorithm=="Numpy" or args.algorithm=="numpy":
        image2, t=b2.blur(image)
    elif args.algorithm=="Numba" or args.algorithm=="numba":
        image2=np.zeros(image.shape, np.uint32)
        image=image.astype(np.uint32)

        image=np.pad(image,pad_width=((1,1),(1,1),(0,0)), mode="edge")
        image2=b3.blur(image)

#if this script is called from terminal show the blurred image
if __name__=='__main__':
    if args.outfilename is not None:
        cv2.imwrite(args.outfilename, image2)
    image2=image2.astype(np.uint8)

    cv2.imshow("Heyao", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
