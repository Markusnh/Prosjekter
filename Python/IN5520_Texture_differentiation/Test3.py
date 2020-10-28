from imageio import imread, imwrite
import matplotlib.pyplot as plt
#from matplotlib.image import imread
import matplotlib.cm as cm
import numpy as np
import sys




"""
below in comments are filenames for feature-maps and the tested threshold to give the best mask for the problem
"""
#mosaic 1
"""
threshold=182
filename="d2t20_feature_map_IDM.png"      #downer left
"""
"""
threshold=145
filename="d4t60_feature_map.png"         #upper right
"""
"""
threshold=95
filename="d4t50_SHD_ws_51.png"               #ish lower right and upper left
"""


#mosaic 2
"""
threshold=95    #
filename="d15t120_SHD_41_mosaic2.png"   #upper right
"""
"""
threshold=115
filename="d15t120_inertia_41_mosaic2.png"        #upper left and downer right
"""
"""
threshold1=70
threshold2=125
filename="d3t240_inertia_41_mosaic2.png"  #upper left
"""
"""
threshold=50
filename="d3t240_SHD_41_mosaic2.png"      #ish lower left corner
"""

feature_map=imread(filename)

#loop through the whole feature-map and find pixels  that have a pixel value below threshold and set them to 0, and pixels above to 255
mask=np.zeros((feature_map.shape))
for i in range(feature_map.shape[0]):
    for j in range(feature_map.shape[1]):
        if feature_map[i,j]>threshold:
            mask[i,j]=255
        else:
            mask[i,j]=0
#show the mask
plt.imshow(mask, cmap=cm.gray)
#and save it to file
filename=filename[:-4]+"mask.png"
plt.savefig(filename)
plt.show()
