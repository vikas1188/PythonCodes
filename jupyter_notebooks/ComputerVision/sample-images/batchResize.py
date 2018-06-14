import cv2
import glob

images = glob.glob("*.jpg")
for image in images:
    print(image)
    img = cv2.imread(image,0)
    resized_im = cv2.resize(img,(100,100))
    cv2.imshow("Hey",resized_im)
    cv2.imwrite("resized_"+image,resized_im)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
