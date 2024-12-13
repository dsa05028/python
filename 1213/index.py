import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Black.otf'
font=font_manager.FontProperties(fname=path).get_name()
plt.rc("font",family=font)

# #이미지 읽기
# image=cv2.imread("./1213/test_image.jpg")

# #opencv BGR->RGB
# image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# """
# # cv2.imshow("title",image_rgb)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# """
# plt.figure(figsize=(10,10))

# #원본
# plt.subplot(2,2,1)
# plt.imshow(image_rgb)
# plt.title("원본")
# plt.axis('off') #x축,y축 생략략

# # #평균 블러
# # blurred=cv2.blur(image_rgb,(5,5))
# # plt.subplot(1,2,2)
# # plt.imshow(blurred)
# # plt.title("평균블러") 
# # plt.axis('off')


# # #가우시안 블러
# # gaussian=cv2.GaussianBlur(image_rgb,(5,5),0)
# # plt.subplot(2,2,3)
# # plt.imshow(gaussian)
# # plt.title("가우시안블러")
# # plt.axis('off')

# # #미디언 블러
# # median=cv2.medianBlur(image_rgb,5)
# # plt.subplot(2,2,4)
# # plt.imshow(median)
# # plt.title("미디언블러")
# # plt.axis('off')

# # #샤프닝 커널
# # kernel=np.array([[0,-1,0],
# #                  [-1,7,-1],
# #                  [0,-1,0]])
# # #필터 적용
# # sharped=cv2.filter2D(image_rgb,-1,kernel)
# # plt.subplot(2,2,2)
# # plt.imshow(sharped)
# # plt.title("엣지강조")
# # plt.axis('off')

# #----엣지 검출
# img=cv2.imread("./1213/test_image.jpg",cv2.IMREAD_GRAYSCALE)

# #sobel
# sobel_x=cv2.Sobel(image_rgb,cv2.CV_64F,1,0,ksize=3) #x방향 미분
# sobel_y=cv2.Sobel(image_rgb,cv2.CV_64F,0,1,ksize=3) #y방향 미분
# #CV_32F
# #CV_8U
# sobel_comvbined=cv2.magnitude(sobel_x,sobel_y)

# #laplacian
# laplacian=cv2.Laplacian(img,cv2.CV_64F)

# #canny

# #원본
# plt.subplot(2,2,1)
# plt.imshow(img,cmap='gray')
# plt.title("원본")
# plt.axis('off')
# #sobel
# plt.subplot(2,2,2)
# plt.imshow(sobel_comvbined,cmap='gray')
# plt.title("sobel")
# plt.axis('off')
# #laplacian
# plt.subplot(2,2,3)
# plt.imshow(laplacian,cmap='gray')
# plt.title("laplacian")
# plt.axis('off')
# #canny
# plt.subplot(2,2,4)
# plt.imshow(laplacian,cmap='gray')
# plt.title("laplacian")
# plt.axis('off')

# plt.show()

#----------웹캠 연결
# cap=cv2.VideoCapture(0)

# # codec=cv2.VideoWriter_fourcc(*'XVID')
# # out=cv2.VideoWriter('output.avi',codec,20.0,(640,480))
# plt.ion() #인터렉티드 모드:코드를 실행하면서 창을 표시
# while cap.isOpened():
#     ret, frame=cap.read()
#     if not ret:
#         print("프레임을 읽지 못했습니다.")
#         break

#     # out.write(frame)
#     # cv2.imshow('video',frame)

#     #원본
#     original=frame.copy()
#     #가우시안 블러
#     gaussian=cv2.GaussianBlur(frame,(5,5),0)

#     plt.subplot(2,2,1)
#     plt.imshow(cv2.cvtColor(original,cv2.COLOR_BGR2RGB))
#     plt.title("원본")
#     plt.axis('off')

#     plt.subplot(2,2,1)
#     plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
#     plt.title("가우시안 블러")
#     plt.axis('off')

#     plt.pause(0.001) #키 입력 대기(1ms)
#     plt.clf() #현재 플롯창에 띄어진것을 초기화 
    
#     key=cv2.waitKey(1)
#     if key==ord('q'): #'q'키가 입력되었는지 확인
#         break

# cap.release()
# # out.release()
# cv2.destroyAllWindows()
# plt.close()

#실습. 손 윤곽선을 감지하고 필터를 추가

#웹캠에서 실시간 영상 읽기
# cap=cv2.VideoCapture(0) #0:웹캠

# while cap.isOpened():
#     ret,frame=cap.read()
#     if not ret:
#         break

#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     blurred=cv2.GaussianBlur(gray,(5,5),0)

#     edges=cv2.Canny(blurred,50,150)

#     contours,_=cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#     frame_with_countours=frame.copy()
#     cv2.drawContours(frame_with_countours,contours,-1,(0,255,0),2)
    
#     #프레임 표시
#     cv2.imshow('orignal',frame)
#     cv2.imshow("Edges", edges)
#     cv2.imshow("Contours", frame_with_countours)

#     if cv2.waitKey(1)==ord('c'):
#         img_captured=cv2.imwrite("./1213/capturedc.png",frame)
#     #'q'를 누르면 종료
#     if cv2.waitKey(1)&0xFF==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# #손 윤곽선 감지:그레이스케일 변환>임계값 처리>컨투어 탐지>컨투어 그리기

# #샤프닝 필터 추가

#실습. 손 윤곽선을 감지하고 필터를 추가

kernel=np.array([[0,-1,0],
                 [-1,7,-1],
                 [0,-1,0]])
cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("영상이 열리지 않습니다")
    exit()

plt.ion() #인터렉티브 모드 활성화
fig,axes=plt.subplots(2,2,figsize=(10,10))

while True:
    ret, frame=cap.read()
    if not ret:
        print("프레임을 열 수 없습니다")
        break

    frame_blurred=cv2.GaussianBlur(frame,(5,5),0)

    #그레이스케일로 변환
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #이진화 처리
    _ , binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    #컨투어 감지
    contours , _=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #컨투어 그리기
    contour_frame=frame.copy()
    contour_frame_blurred=cv2.GaussianBlur(contour_frame,(5,5),0)
    cv2.drawContours(contour_frame_blurred,contours,-1,(0,255,0),2)

    #샤프닝 필터
    sharp=cv2.filter2D(contour_frame_blurred,-1,kernel)
    
    #원본
    axes[0,0].imshow(cv2.cvtColor(frame_blurred,cv2.COLOR_BGR2RGB))
    axes[0,0].set_title("원본")
    axes[0,0].axis('off')

    # 컨투어
    axes[0,1].imshow(cv2.cvtColor(contour_frame_blurred,cv2.COLOR_BGR2RGB))
    axes[0,1].set_title("컨투어")
    axes[0,1].axis('off')

    #샤프닝 필터
    axes[1,0].imshow(cv2.cvtColor(sharp,cv2.COLOR_BGR2RGB))
    axes[1,0].set_title("샤프닝")
    axes[1,0].axis('off')

    # #원본
    # plt.subplot(2,2,1)
    # plt.imshow(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    # plt.title("원본")
    # plt.axis('off')

    # #컨투어
    # plt.subplot(2,2,2)
    # plt.imshow(cv2.cvtColor(contour_frame,cv2.COLOR_BGR2RGB))
    # plt.title("컨투어")
    # plt.axis('off')

    # #샤프닝 필터
    # plt.subplot(2,2,2)
    # plt.imshow(cv2.cvtColor(sharp,cv2.COLOR_BGR2RGB))
    # plt.title("샤프닝")
    # plt.axis('off')

    plt.pause(0.001)
    # plt.clf()

    key=cv2.waitKey(1)
    if key==ord('q'):
        break

#리소스 해제
cap.release()
cv2.destroyAllWindows()
plt.ioff() #인터렉티브 모드 종료