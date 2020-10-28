This is a project that takes in an image and blurs the faces in that image. Blur_1, Blur_2
and Blur_3 does the exact same thing, but with different methods, showing how the operations
can be done faster. Blur_1 solves it with regular for loops, Blur_2 solves it using numpy
arrays, and Blur_3 uses @jit to speed up regular python for-loops

Blur_faces.py takes in an image, uses an algorithm to dtect faces and blurs the faces
until it can not recognize any more faces


To run the scripts you have to be in the directory assignment4. To run the scripts simply run the following in the terminal

...assignment4>python blur_1.py

...assignment4>python blur_2.py

...assignment4>python blur_3.py

...assignment4>python blur.py infilename algorithm --outfilname

...assignment4>python blur_faces.py

to run the tests with pytest simply write in the terminal

...assignment4>pytest