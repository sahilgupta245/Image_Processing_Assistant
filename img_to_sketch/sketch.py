import cv2
from main import imagepath
print(cv2.__version__)
#imagepath="bg.png"
# imagepath = open("somefile.txt", mode='r', encoding='utf-8')
# path=imagepath.read()
# imagepath.close()
# print(path)
image = cv2.imread(imagepath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(gray_image)
blur=cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)

pencil_sketch = cv2.divide(gray_image, invertedblur,scale=225.0)
resized_image = cv2.resize(pencil_sketch, (500, 500))
cv2.imwrite("output.png",resized_image)
cv2.imshow("original image", image)
#cv2.waitKey()
cv2.imshow("pencil sketch", resized_image)
cv2.waitKey()
