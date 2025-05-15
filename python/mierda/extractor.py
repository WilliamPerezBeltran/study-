import cv2

img = cv2.imread("./1.png")
print(img)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)

print ("Threshold selected : ", ret)
cv2.imwrite("./debug.png", thresh)
