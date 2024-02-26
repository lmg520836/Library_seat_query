



import os
import time
import cv2
from ultralytics import YOLO

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=True, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        print(predictions)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=True, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            print(predictions)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()













import os
import time
import cv2
from ultralytics import YOLO
from collections import Counter

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        
        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            
            # 计数每种类别的数量
            counter = Counter([pred['name'] for pred in predictions])
            print(counter)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()







# 网页版

import os
import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 文件夹路径
folder = 'D:/Library_seat _query/Ntrain'
output_folder = '/home/pi/Desktop/yoloruns'

# 文件跟踪
files = set(os.listdir(folder))
no_new_files_counter = 0

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 生成图片文件名
        img_name = os.path.join(folder, "opencv_frame_{}.png".format(len(files)))
        # 将图片保存为文件
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        # 进行推理
        predictions = model.predict(img_name, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
        
        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)

        # 将结果转换为 JSON 格式
        data = json.dumps(counter)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)

        # 更新文件集
        files.add(img_name)
    else:
        print("无法获取摄像头画面")

    # 检查新文件
    new_files = set(os.listdir(folder)) - files

    if new_files:
        # 重置计数器
        no_new_files_counter = 0

        # 遍历新文件
        for filename in new_files:
            file = os.path.join(folder, filename)
            output_file = os.path.join(output_folder, filename)
            predictions = model.predict(file, save=False, imgsz=640, conf=0.5, save_dir=output_folder, save_txt=True)
            
            # 计数每种类别的数量
            counter = Counter([pred['name'] for pred in predictions])
            print(counter)

            # 将结果转换为 JSON 格式
            data = json.dumps(counter)

            # 发送 HTTP 请求
            response = requests.post('http://your-server.com/api/path', data=data)

        # 更新文件集
        files.update(new_files)
    else:
        # 增加计数器
        no_new_files_counter += 1

        # 检查计数器是否达到100
        if no_new_files_counter >= 100:
            break

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()
















import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 进行推理
        predictions = model.predict(frame, save=False, imgsz=640, conf=0.5)

        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)

        # 将结果转换为 JSON 格式
        data = json.dumps(counter)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()






import time
import cv2
from ultralytics import YOLO
from collections import Counter

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 进行推理
        predictions = model.predict(frame, save=False, imgsz=640, conf=0.5)

        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])
        print(counter)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()



# id
import time
import cv2
from ultralytics import YOLO
from collections import Counter
import requests
import json

# YOLO模型
model = YOLO('D:/Library_seat _query/library/detect/train/weights/best.pt')

# 设备ID
device_id = 'device_1'

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 检查摄像头是否正确打开
    if not cap.isOpened():
        print("无法打开摄像头")
        break

    # 读取摄像头的画面
    ret, frame = cap.read()
    if ret:
        # 进行推理
        predictions = model.predict(frame, save=False, imgsz=640, conf=0.5)

        # 计数每种类别的数量
        counter = Counter([pred['name'] for pred in predictions])

        # 创建要发送的数据
        data = {
            'device_id': device_id,
            'counts': dict(counter)
        }

        # 将数据转换为 JSON 格式
        data = json.dumps(data)

        # 发送 HTTP 请求
        response = requests.post('http://your-server.com/api/path', data=data)
    else:
        print("无法获取摄像头画面")

    # 暂停一段时间
    time.sleep(60)

# 释放摄像头
cap.release()