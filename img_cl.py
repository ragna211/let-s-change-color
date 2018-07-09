#what are we doing?
#we are converting our image to different colors and that too by changing the values in the matrix formed from the image 




from scipy import misc
from skimage import img_as_float

from PIL import Image  #this library is used for display of image                                                                              
import numpy as np    #to convert array back to image

image = misc.imread(r"C:\Users\HP\Desktop\green-red-yellow apples\haha.jpeg")      #image converted to array
print(image.shape)         #image in matrix form
img = Image.open('haha.jpeg')
img.show() 
red, yellow =   image.copy(), image.copy()     #images can be copied even without using deepcopy
red[:,:,(1,2)] = 0                             #array of image converted to a red dominant one
yellow[:,:,2]=0                                #array of image converted to a yellow dominant one


#show_images(images=[red,yellow], titles=['Red Intensity','Yellow Intensity'])

img = Image.fromarray(red, 'RGB')        #image formed back from the array,numpy used here
img.save('red_apple.jpeg')
img = Image.open('red_apple.jpeg')
img.show()


img = Image.fromarray(yellow, 'RGB')
img.save('yellow_apple.jpeg')
img = Image.open('yellow_apple.jpeg')
img.show()

from skimage.color import rgb2gray
gray = rgb2gray(image)
#show_images(images=[image,gray_image],titles=["Color","Grayscale"])
img = Image.fromarray(gray, 'RGB')
img.save('gray_apple.jpeg')
img = Image.open('gray_apple.jpeg')
img.show()
print ("Colored image shape:", image.shape)
print ("Grayscale image shape:", gray_image.shape)