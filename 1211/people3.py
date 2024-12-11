#특정지역 연령별 남성 인구 및 여성인구 비교

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

#한글폰트 설정 : 파일경로>
path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\AppleSDGothicNeoL.ttf'
font=font_manager.FontProperties(fname=path).get_name()
plt.rc("font",family=font)
#인구데이터 불러오기
#숫자 변환
#데이터 추출