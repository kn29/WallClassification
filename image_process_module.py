import numpy as np
import cv2

import matplotlib.pyplot as plot


#【OPENCV】
BorderLine=4
rgb_b=0
rgb_r=255
rgb_g=0
#fontの種類:http://tatabox.hatenablog.com/entry/2014/10/06/003655
font = cv2.FONT_HERSHEY_SIMPLEX
font_bold=3

#クリックしたポジションを出力する関数
def print_position(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)

#画面にレクタングルを描画
def draw_rectangle(img,initial_x,initial_y,end_x,end_y):
    cv2.rectangle(img,(initial_x,initial_y),(end_x,end_y),(rgb_b,rgb_r,rgb_g),BorderLine)

#画面に円を描画
#円を塗りつぶす場合はBorderLine=-1
def draw_circle(img,point_x,point_y,radius):
    cv2.circle(img,(point_x,point_y),radius,(rgb_b,rgb_r,rgb_g),BorderLine)

#画像にテキストを挿入
def put_text_on_image(img,text,point_x,point_y):
    #1はスケール★
    cv2.putText(img,text,(point_x,point_y),font,1,(rgb_b,rgb_r,rgb_g),font_bold,cv2.LINE_AA)

#画像の2値化
def binarize_images(img, threshold):
    ret,img_th=cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)

    return img_th
