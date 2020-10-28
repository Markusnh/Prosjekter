from imageio import imread, imwrite
import matplotlib.pyplot as plt
# from matplotlib.image import imread
import matplotlib.cm as cm
import numpy as np
import sys


def make_histograms():
	"""
    This function is not needed to solve the problem, it is only needed to get out the histogram so that we can see that the histogram is not much of help in differentiating
	and that histogram transforms will not help much here
    """
	# making histograms
	fig, axs = plt.subplots(len(images))
	for i in range(len(images)):
		axs[i].hist(images[i])
	axs[len(images) - 1].set(xlabel='pixel value', ylabel='number of occurences')
	plt.show()

	# computing mean, variance, skewness, kurtosis
	meanlist = []
	variancelist = []
	skewnesslist = []
	kurtosislist = []
	for i in range(len(images)):
		image = images[i].ravel()
		mean = sum(image) / len(image)
		variance = sum((image - mean) ** 2) / len(image)
		skewness = sum((image - mean) ** 3) / (len(image) * np.sqrt(variance) ** 3)
		kurtosis = sum((image - mean) ** 4) / (len(image) * np.sqrt(variance) ** 4)

		meanlist.append(mean)
		variancelist.append(variance)
		skewnesslist.append(skewness)
		kurtosislist.append(kurtosis)
	print(meanlist, "mean")
	print(variancelist, "variance")
	print(skewnesslist, "skewness")
	print(kurtosislist, "kurtosis")
	print(1 - (1 / (1 + np.asarray(variancelist))), "smoothness")


def find_loop_indexes(image, theta_in):
	"""
    This is a method that will return the correct indexes to be used in the for loop to calcualte the GLCM according to which theta-value one use
    """
	theta = (theta_in / 360) * 2 * np.pi
	if theta_in >= 0 and theta_in <= 90:
		startindexi = 0
		endindexi = image.shape[0] - int(np.cos(theta) * d)
		startindexj = 0
		endindexj = image.shape[1] - int(np.sin(theta) * d)
	elif theta_in > 90 and theta_in <= 180:
		startindexi = abs(int(np.cos(theta) * d))
		endindexi = image.shape[0]
		startindexj = 0
		endindexj = image.shape[1] - int(np.sin(theta) * d)
	elif theta_in > 180 and theta_in <= 270:
		startindexi = abs(int(np.cos(theta) * d))
		endindexi = image.shape[0]
		startindexj = abs(int(np.sin(theta) * d))
		endindexj = image.shape[1]
	elif theta_in > 270 and theta_in <= 360:
		startindexi = 0
		endindexi = image.shape[0] - int(np.cos(theta) * d)
		startindexj = abs(int(np.sin(theta) * d))
		endindexj = image.shape[1]

	return startindexi, endindexi, startindexj, endindexj


def calculate_and_save_GLCM(image, d, theta, plot=False, write=False, filename=None):
	"""
    This method calculates the GLCM with the given parameters
    """
	theta_in = theta
	theta = (theta_in / 360) * 2 * np.pi
	GLCM_matrix = np.zeros((num_pixval, num_pixval))
	# find the correct indexes in the for-loop according to the angle and distance given
	startindexi, endindexi, startindexj, endindexj = find_loop_indexes(image, theta_in)
	for i in range(startindexi, endindexi):
		for j in range(startindexj, endindexj):
			# find the value of the two chosen pixels and put them into the GLCM matrix
			pixel1 = image[i, j]
			pixel2 = image[i + int(np.cos(theta) * d), j + int(np.sin(theta) * d)]
			GLCM_matrix[pixel1, pixel2] += 1

	# make it symmetrical
	GLCM_matrix = (GLCM_matrix + GLCM_matrix.T)
	summ = np.sum(GLCM_matrix)
	# normalize it
	GLCM_matrix = GLCM_matrix / float(summ)

	maxi = np.max(GLCM_matrix)
	mini = np.min(GLCM_matrix)
	# made closer to the 0-255 value to make converting it to image more secure(less lossy)
	if write:
		GLCM_matrix_bits = ((GLCM_matrix - mini) / (maxi - mini)) * 255
		streng = filename
		imwrite(streng, GLCM_matrix_bits)

	if plot:
		plt.imshow(GLCM_matrix)
		plt.show()  # show the plot of all the different GLCM matrices

	return GLCM_matrix


if __name__ == "__main__":
	num_images = 2
	num_textures = 4  # per picture
	num = int(num_textures / 2)
	pixels = 512

	# reads in the images
	image1 = imread("mosaic1.png")
	image2 = imread("mosaic2.png")

	# puts the images into list
	imagelist = [image1, image2]

	# images will contain images of only one texture per image
	images = []

	# divide the original images into the different textures and put them into images list
	for i in range(num_images):
		image = imagelist[i]
		for j in range(num):
			for k in range(num):
				images.append(image[int((pixels / num) * k):int((pixels / num) * (k + 1)),
							  int((pixels / num) * j):int((pixels / num) * (j + 1))])

	# rescale so that the images only contains 16 different values
	for i in range(len(images)):
		for j in range(images[i].shape[0]):
			for k in range(images[i].shape[1]):
				images[i][j][k] = int(images[i][j][k] / 16)

	# setting some parameters
	num_pixval = 16

	make_histograms()

	# taking in the parameters from user
	d = int(sys.argv[1])
	theta = int(sys.argv[2])
	write = bool(int(sys.argv[3]))
	plot = bool(int(sys.argv[4]))
	filename = sys.argv[5]

	fig, axs = plt.subplots(3, 3)
	# used to get the subplots at different positions in the main plot
	in_i = 0
	in_j = 0
	for i in range(len(images)):
		image = images[i]
		GLCM_matrix = calculate_and_save_GLCM(image, d, theta, plot=plot, write=write,
											  filename=filename + str(i) + ".png")
		axs[in_i, in_j].imshow(GLCM_matrix)
		if in_i >= 2:
			in_i = 0
			in_j += 1
		else:
			in_i += 1
	# save to file and show the plot of all the subplots
	streng = str(d) + str(theta) + ".png"
	fig.colorbar(cm.ScalarMappable())
	plt.savefig(streng)
	plt.show()
