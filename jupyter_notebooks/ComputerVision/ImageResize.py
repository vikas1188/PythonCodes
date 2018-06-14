import cv2


img = cv2.imread("galaxy.jpg",0) # 0 means grey scale, -1 means RGB band and +1 also means something

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


resized_im = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # width, height

cv2.imshow("Galaxy", resized_im)
cv2.imwrite("Galaxy_resized.jpg", resized_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
