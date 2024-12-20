#myCamera.py
import os
import io
import time
import picamera
import cv2
import numpy as np
# 전역 변수 선언 및 초기화
fileName = ""
stream = io.BytesIO()
haar = cv2.CascadeClassifier('./haarCascades/haar-cascade-filesmaster/haarcascade_frontalface_default.xml')
camera = picamera.PiCamera()
camera.resolution = (320, 240)
time.sleep(1) # 카메라 워밍업

def takePicture() :
    global fileName
    global stream
    global camera
    # 이전에 만들어둔 사진 파일이 있으면 삭제
    if len(fileName) != 0:
        os.unlink(fileName)
        
    stream.seek(0) # 파일 포인터를 스트림 맨 앞으로 위치시킴. 이곳에서부터 이미지 데이터 저장
    stream.truncate()
    camera.start_preview() # 연결된 모니터에 보이도록 하기 위함
    time.sleep(0.1) # 실시간으로 찍어야하기 떄문에 아주 짧은 시간을 줌
    camera.capture(stream, format='jpeg', use_video_port=True)
    camera.stop_preview()
    data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(image_gray,1.1,3)

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        takeTime = time.time()
        fileName = "./static/%d.jpg" % (takeTime * 10)
        cv2.imwrite(fileName, image)

    return fileName
 
if __name__ == '__main__' :
    takePicture()