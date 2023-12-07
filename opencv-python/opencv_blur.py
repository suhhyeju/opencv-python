import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('picture1.png')
if img is None:
    print("Not photo")
    exit()
    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

v = 20
for (x, y, w, h) in faces:
    roi = img[y:y+h, x:x+w]
    roi = cv2.GaussianBlur(roi, (99, 99), 30)
    roi = cv2.flip(roi, 0)
    img[y:y+roi.shape[0], x:x+roi.shape[1]] = roi


cv2.imshow('Blur out', img)
cv2.waitKey()
cv2.destroyAllWindows()