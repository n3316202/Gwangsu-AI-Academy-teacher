# 텐서플로 라이브러리 안에 있는 케라스 API에서 필요한 함수들을 불러옵니다.
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Dense   

# 데이터를 다루는 데 필요한 라이브러리를 불러옵니다.
import numpy as np
import pandas as pd

df = pd.read_csv(r"D:\Gwangsu-AI-Academy-teacher\08.딥러닝\04.실전_데이타_예제\pima-indians-diabetes3.csv")
print(df)

# | 컬럼                       | 의미         |
# | ------------------------ | ---------- |
# | Pregnancies              | 임신 횟수      |
# | Glucose                  | 혈당 수치      |
# | BloodPressure            | 혈압         |
# | SkinThickness            | 피부 두께      |
# | Insulin                  | 인슐린 수치     |
# | BMI                      | 체질량지수      |
# | DiabetesPedigreeFunction | 당뇨 유전 지수   |
# | Age                      | 나이         |
# | Outcome                  | 당뇨병 여부(정답) |

df.info()

# 정상과 당뇨 환자가 각각 몇 명씩인지 조사
print(df["diabetes"].value_counts())

print(df.describe())
print(df.corr())

#필요한 라이브러리를 불러옵니다.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 간의 상관 관계를 그래프로 표현해 봅니다.
# colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다.
# plt.figure(figsize=(12,12))   #그래프의 크기를 정합니다.

# # 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울수록 밝은색으로 표시되게 합니다.
# sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)
# plt.show()

# 데이타 나누기
# 세부 정보를 X로 지정합니다.
x = df.iloc[  : ,   0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[  : ,  8]

print(x)
print(y)

from keras.models import Sequential
from keras.layers import Dense, Input

# 모델링
# 데이터 크기 => 768 기준
# 데이타 천개 이하 => 1 또는 2개
# 만개 이하 => 2-3개
# 10만개 이상 3-5 까지.

# 뉴런갯수 
# 컬럼수 4~10 => 8 ~ 32
# 10~50개	16~64개
# 50개 이상	32~256개

# 히든레이어는 = 총 데이터수 고려
# 뉴런은 = 총컬럼수 고려
model = Sequential([
    Input(shape=(8,)), # 총 컬럼수    
    Dense(12,activation="relu"),
    Dense(8,activation="relu"),    
    Dense(1,activation="sigmoid"),

])