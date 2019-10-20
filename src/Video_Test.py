#coding: utf-8
#视频流的输入输出测试,为了连接网页与视频处理的连贯性,做的接口测试
import cv2
import time
import numpy as np

#读取视频,并设置输出视频格式为.mp4,720p
cap = cv2.VideoCapture('./HTML/video1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'avc1')
out = cv2.VideoWriter('./HTML/output1.mp4', fourcc, 20, (1280, 720))

#图像处理函数,测试用
def Process_Image(Image):
    return cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

#视频处理
num = 0
#输入流
while cap.isOpened():
    #获取视频流数据
    rval, frame = cap.read()
    #如果有效,则进行帧处理
    if rval == True:
        #frame = cv2.flip(frame,0)
        start = time.time()
        New_Image = Process_Image(frame)
        end = time.time()
        seconds = end - start + 0.0001
        print("Time taken : {0} seconds".format(seconds))
        fps = 1 / seconds;
        print("Estimated frames per second : {0}".format(fps));
        out.write(New_Image)
        num = num + 1
        print(num)
        fps = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    else:
        break
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#关闭流
cap.release()
out.release()
cv2.destroyAllWindows()

