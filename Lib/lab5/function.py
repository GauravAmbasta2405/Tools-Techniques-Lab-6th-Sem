import cv2

path = r'C:\Users\KIIT\OneDrive\Desktop\T&T lab\Image1.jpeg'

image = cv2.imread(path)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()