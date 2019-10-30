import cv2 as cv
import os
# img1 = cv.imread("images/first.jpg")
# img1 = img1[0:200,0:200]
# img2 = cv.imread("images/second.jpg")
# img2 = img2[0:200,0:200]
# img3 = cv.imread("images/third.jpg")
# img3 = img3[0:200,0:200]
# img4 = cv.imread("images/four.jpg")
# img4 = img4[0:200,0:200]
# img5 = cv.imread("images/five.jpg")
# img5 = img5[0:200,0:200]

# l = [img1,img2,img3,img4,img5]

def get_all_images(folder):
	images = []
	l = os.listdir(folder)
	print(l)
	for i in l :
		img = cv.imread("images/"+str(i))
		images.append(img)
	return images
folder = "/home/adarsh/Desktop/SlideShow/images"
l = get_all_images(folder)
for i in range(len(l)-1):
	img=cv.addWeighted(l[i],0.9,l[i+1],0.1,0)
	cv.imshow("frame",img)
	cv.waitKey(2000)

