import cv2 #okokok
import numpy as np
import os

cap = cv2.VideoCapture(0) #Chỉnh để chọn nguồn video
#cap.set(3, 320)
#cap.set(4, 180)

minW = 0.1 *cap.get(3)
minH = 0.1 *cap.get(4)
#thu thập data khuôn mặt của từng ng
face_id = input ("Nhập ho ten =>>")
print ("Đang khởi chạy camera, xin vui lòng đợi")
count = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
# Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Face", frame)

    key = cv2.waitKey(100)
# Lưu ảnh đã chụp
    if key == ord('c'):
        count += 1
        image_path = os.path.join("dataset")
        cv2.imwrite(f"dataset/{str(face_id)}_{str(count)}.jpg", frame)
        print("Đã chụp ảnh!")
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



