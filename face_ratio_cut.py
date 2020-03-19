# 얼굴 정해진 비율대로 자르는 코드
# 눈 : 세로 - 얼굴 3등분 했을 때 0.5~1.7번째 -> 2등분 했을 때 첫번째
# 코 : 세로 - 얼굴 3등분 했을 때 두번째 , 가로 - 5등분 했을 때 2~4번째
# 입 : 세로 - 얼굴 3등분 했을 때 1.5~3.5번째 -> 2등분 했을 때 첫번째 , 가로 - 5등분 했을 때 1.5~4.5번째

# 이미지 불러오기
# 사진 크기 확인하기
# 비율대로 자르기
# 저장하기

import cv2
import glob
import numpy as np

#작업할 이미지 경로
img_dir = "C:\\Users\\Public\\facebook\\crop\\main_original\\*"
file_list = glob.glob(img_dir)
img_list = [file for file in file_list if file.endswith(".jpg")]
cnt_img = len(img_list)

for i in range(cnt_img):
    imgfile_name = img_list[i].split("\\")
    train = cv2.imread(img_list[i])
    tmp = train.copy()

    h, w, c = tmp.shape
    print('hight', h, 'width', w)
    facecut_h = int(round(h/3))
    facecut_w = int(round(w/5))

    print(facecut_h, facecut_h*2)
    print(facecut_w*2, facecut_w*3)


    eye_img = tmp[int(facecut_h - round(facecut_h/2)):int(facecut_h *2 - round(facecut_h/3))]
    nose_img = tmp[int(facecut_h):int(facecut_h * 2), int(facecut_w):int(facecut_w * 4)]
    mouth_img = tmp[int(facecut_h*2 - round(facecut_h/2)):int(facecut_h*3 + round(facecut_h/2)), int(facecut_w - round(facecut_w/2)):int(facecut_w*4 + round(facecut_w/2))]


#    cv2.imshow('face', train)
#    cv2.imshow('eye', eye_img)
#    cv2.imshow('nose', nose_img)
#    cv2.imshow('mouth', mouth_img)
#    cv2.waitKey()

    # 자른 이미지 저장
    eye_path = "C:\\Users\\Public\\facebook\\crop\\eye\\" + imgfile_name[-1]
    cv2.imwrite(eye_path,eye_img)

    nose_path = "C:\\Users\\Public\\facebook\\crop\\nose\\" + imgfile_name[-1]
    cv2.imwrite(nose_path, nose_img)

    mouth_path = "C:\\Users\\Public\\facebook\\crop\\mouth\\" + imgfile_name[-1]
    cv2.imwrite(mouth_path, mouth_img)
