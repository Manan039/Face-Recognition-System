import cv2
import os
import numpy as np
import FaceDetection as t

test_img=cv2.imread('Test/m.jpg')
faces_detected,gray_img=t.faceDetection(test_img)
print("faces_detected:",faces_detected)

faces,faceID=t.labels_for_training_data('trainingimages')
face_recognizer=t.train_classifier(faces,faceID)
name={0:"Bill Gates",1:"Mark"}
cap=cv2.VideoCapture(0)

for face in  faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("label",label)
    t.draw_rect(test_img,face)
    predicted_name=name[label]
    t.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(700,500))
cv2.imshow("face detection ",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

