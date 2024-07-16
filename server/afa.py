import cv2
#face_cascade = cv2.CascadeClassifier('D:\\Code\\SporcuYuzTanımaModeli\\server\\opencv\\haarcascades\\haarcascade_frontalface_default.xml')
# veya
face_cascade = cv2.CascadeClassifier(r'D:\Code\CelebrityFaceRegognition\server\opencv\haarcascades\haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error loading cascade file")
