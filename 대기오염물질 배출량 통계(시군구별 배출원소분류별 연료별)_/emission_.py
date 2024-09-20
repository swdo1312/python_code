#-*- encoding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#경로 설정 (엑셀파일 위치)
path = 'D:/Users/KEI/Documents/Messenger Download/대기오염물질 배출량 통계(시군구별 배출원소분류별 연료별)/'



# 분석할 내용 설정 =============================================================
# 
year = 2021
jogen_1_name = '도로이동오염원'
jogen_2_name = 'NOx'


emisson_list = ['RV','버스','승용차','승합차','이륜차','택시','특수차','화물차']
emisson_list_data = np.full([len(emisson_list)],0)
# =============================================================================


# 파일 불러오기
df = pd.read_excel(path + str(year)+"년 대기오염물질 배출량 통계(시군구별 배출원소분류별 연료별).xlsx", sheet_name='ver.6.0',skiprows=2)

# 위에서 설정한 조건에 따라 맞게 데이터 값 불러오기 (여기선, 도로이동오염원, NOx 임.)
jogen_1 = df['배출원대분류'] == jogen_1_name
jogen_2 = df.iloc[:,np.where(df.iloc[0,:]==jogen_2_name)[0][0]]

# 조건1, 조건2에 맞는 데이터 값 위치
jogen_end = np.where(jogen_1 & jogen_2)[0]


for i in jogen_end:
    # print(i)
    
    value = df.iloc[i,:]['배출원중분류']
    if value in emisson_list:
        index = emisson_list.index(value)
        
        
        emisson_list_data[index] += df.iloc[i,np.where(df.iloc[0,:]==jogen_2_name)[0][0]]
        # emisson_list_data[index] += df.iloc[i,8]
    
    

# ===== 그래프 그리기 ==========================================================

# 한국어 지원
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


# 전체 데이터의 합
total = np.sum(emisson_list_data)

# 비율 계산 (퍼센트)
percentages = (emisson_list_data / total) * 100

# 막대 그래프 그리기
plt.figure(figsize=(10,6))
plt.bar(emisson_list, percentages, color='skyblue')

# 그래프 제목 및 라벨
plt.title(str(year)+'년',fontsize=15,fontweight='bold',loc='left')
plt.title(jogen_1_name+'('+jogen_2_name+')',fontsize=15,fontweight='bold',loc='right')

plt.ylabel('Percentage (%)',fontsize=15,fontweight='bold')

# 값이 표시되도록 막대 위에 텍스트 추가
for i, value in enumerate(percentages):
    plt.text(i, value + 0.5, f'{value:.2f}%', ha='center')

# 그래프 저장
plt.savefig(path + str(year) + '년_' + jogen_1_name + '_' + jogen_2_name + '.png'  , dpi=300, bbox_inches='tight')

# 그래프 출력
plt.show()
# =============================================================================


