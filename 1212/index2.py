#실습.이미지처리
import cv2

#1.이미지를 읽어서 크기를 출력하세요. 크기 출력
image=cv2.imread("./1212/strawberrycake.jpg")

print(image.shape)
cv2.imshow("strawberrycake",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2.이미지를 흑백으로 변환하고 화면에 표시하세요.
image=cv2.imread("./1212/strawberrycake.jpg")
gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

cv2.imshow("strawberrycake",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#3.이미지를 50%크기로 축소하고 새로운 창에 표시하새요.
image=cv2.imread("./1212/strawberrycake.jpg")

resized=cv2.resize(image,None,fx=0.5,fy=0.5)
cv2.imshow("strawberrycake",image)
cv2.imshow("strawberrycake*0.5",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#4.이미지를 90도 회전하여 저장하세요.
image=cv2.imread("./1212/strawberrycake.jpg")

#중심좌표
(h,w)=image.shape[:2]
center=(w//2,h//2)

matrix=cv2.getRotationMatrix2D(center,90,1.0)
rotated=cv2.warpAffine(image,matrix,(w,h))

cv2.imshow("strawberrycake",rotated)
cv2.waitKey(0)

cv2.imwrite("./1212/output-rotated.jpg",rotated)

cv2.destroyAllWindows()