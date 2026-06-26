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