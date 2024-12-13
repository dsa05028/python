import cv2

# #이미지 파일 불러오기

# # image=cv2.imread("./1212/chrismas.jpg")
# image=cv2.imread("./1212/chrismas.jpg",cv2.IMREAD_GRAYSCALE)
# image_color=cv2.imread("./1212/chrismas.jpg")

# print(image.shape)
# print(image_color.shape)

# cv2.imshow("Gray Image",image)
# cv2.imshow("Color Image",image_color)

# # key=cv2.waitKey(0)
# # if key==ord("q"):
# #     print(chr(key)) #chr:아스키코드 획득

# cv2.waitKey(2000)

# #이미지 파일 저장
# # cv2.imwrite("./1212/output-image.jpg",image)

# cv2.destroyAllWindows()
#-----------------------------------------
# image_color=cv2.imread("./1212/chrismas.jpg")

# gray=cv2.cvtColor(image_color,cv2.COLOR_RGB2GRAY)
# hsv=cv2.cvtColor(image_color,cv2.COLOR_BGR2HSV)

# resized=cv2.resize(image_color,(300,200))
# scale=0.5
# resized=cv2.resize(image_color,None,fx=0.5,fy=0.5)

# roi=image_color[100:300,100:300].copy() #y,x순서

# cv2.imshow("Color Image",image_color)
# cv2.imshow("Color Image",roi)

#-----------------------------------------
#x값, y값 찾기
# def mouse_click(e,x,y,flag,param):
#     if e==cv2.EVENT_LBUTTONDOWN:
#         print(f"마우스 위치:x={x},y={y}")

# image_color=cv2.imread("./1212/chrismas.jpg")

# cv2.imshow("image",image_color)
# #마우스 콜백함수
# cv2.setMouseCallback("image",mouse_click)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-----------------------------------------
#roi만 표시
#글로벌함수
# start=None
# end=None
# def mousse_select(e,x,y,flg,param): #argument 5개가 필요함, flag와 param은 쓰지 않지만 넣어줌
#     global start,end
#     if e==cv2.EVENT_LBUTTONDOWN: #클릭을 누르는 상태
#         start=(x,y)
#     elif e==cv2.EVENT_LBUTTONUP: #클릭을 뗀 상태
#         end=(x,y)
#         #영역표시
#         roi=image_color[start[1]:end[1],start[0]:end[0]] #y축,x축 순서에 맞춰 1,0
#         cv2.imshow("select",roi)

# image_color=cv2.imread("./1212/chrismas.jpg")

# cv2.imshow("image",image_color)

# #마우스 콜백함수
# cv2.setMouseCallback("image",mousse_select)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#-----------------------------------------
#중심좌표
import numpy as np

image_color=cv2.imread("./1212/chrismas.jpg")
(h,w)=image_color.shape[:2]
center=(w//2,h//2)

#회전
# matrix=cv2.getRotationMatrix2D(center,180,1.0)
# rotated=cv2.warpAffine(image_color,matrix,(w,h))

#이동
matrix=np.float32([[1,0,100],[0,1,50]])
move=cv2.warpAffine(image_color,matrix,(w,h))
cv2.imshow("image",move)
cv2.waitKey(0)
cv2.destroyAllWindows()