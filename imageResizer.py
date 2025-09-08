import cv2 as cv

image = cv.imread("Ahnuf Mir.jpg")
cv.imshow("title", image)

scale_percent = 50

new_width = int(image.shape[1] * scale_percent/100)
new_height = int(image.shape[0] * scale_percent/100)

new_size = (new_width,new_height)

output = cv.resize(image, new_size)

cv.imwrite("Resized Pic.png", output)



cv.waitKey(0)
