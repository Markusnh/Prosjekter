This is a project about differentiating between textures in an image using 
GLCM-matrices. First I look at the pictures and try to detrermine which angles
and distances would be most efficient whne making the GLCM's. This is done in Test1.py

Then we take a sliding window, making very many GLCM-matrices for an image, and then
I make features from them, that is apply functions to all of the GLCM's to convert it back¨
to an image where the features of the image I want are lighter, and the features of the image
I am not interested in becomes black or darker. This is what is done in Test2.py

When we have images of darker and lighter patches, we need to threshold them to make masks
that is saying that we are only interested in the pixels with a pixel value of over 190 for instance. 
This is what is done in Test3.py

The result fo this project is the mask-images we have in this directory. They are the final
product of the differentiation, and they should if they were perfect only contain
one feature/texture per white patch, but some of textures was difficoult to differentiate
so the masks aren't perfect.