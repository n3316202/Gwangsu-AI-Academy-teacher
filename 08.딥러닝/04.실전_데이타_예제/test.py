# 텐서플로 라이브러리 안에 있는 케라스 API에서 필요한 함수들을 불러옵니다.
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Dense   

# 데이터를 다루는 데 필요한 라이브러리를 불러옵니다.
import numpy as np
import pandas as pd

# =====================================
# 1. 데이터 불러오기
# =====================================

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

# =====================================
# 2. X, y 분리
# =====================================
# 데이타 나누기
# 세부 정보를 X로 지정합니다.
x = df.iloc[  : , 0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[  : ,  8]

# print(x)
# print(y)

# 학습용 / 테스트용 데이터 분리
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 정상 : 980명
# 암환자 : 20명

# 정상 : 200명
# 암환자 : 0명
# =====================================
# 3. 학습용 / 테스트용 분리
# =====================================
x_train,x_test, y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify = y # 같은 비율로 들어 갈수 있도록 #분류 모델에서는 stratify=y 로 할것 
)

# =====================================
# 4. 정규화
# =====================================
# 정규화
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from keras.models import Sequential
from keras.layers import Dense, Input

# 모델링
# 데이터 크기 => 768 기준
# 데이타 천개 이하 => 1 또는 2개
# 만개 이하 => 2-3개
# 10만개 이상 3-5 까지.

# 뉴런갯수 
# 컬럼수 4~10 => 8 ~ 32
# 컬럼수 10~50개 =>	16~64개
# 컬럼수 50개 이상 => 32~256개

# 히든레이어는 = 총 데이터수 고려
# 뉴런은 = 총컬럼수 고려
# =====================================
# 5. 모델 생성
# =====================================
model = Sequential([
    Input(shape=(8,)), # 총 컬럼수    
    Dense(12,activation="relu"),
    Dense(8,activation="relu"),    
    Dense(1,activation="sigmoid"),
])

model.summary()

# =====================================
# 6. 컴파일
# =====================================
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# 학습
# =====================================
# 7. 학습
# =====================================
# 99/99 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8330 - loss: 0.3676 - val_accuracy: 0.8130 - val_loss: 0.4356
history = model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=5,# 5개 학습하고 가중치 수정
    validation_split=0.2,
    verbose=1
)

# 평가 
loss, acc = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

# 테스트 Loss : 0.5363  # 평균오차 or 모델이 틀린 정도를 나타내는 값
# 테스트 Accuracy : 0.7468

print()
print("테스트 Loss :", round(loss, 4))
print("테스트 Accuracy :", round(acc, 4))

# 시각화 
# 정확도
plt.figure(figsize=(8, 4))

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend([
    "Train",
    "Validation"
])

plt.show()

# Loss 그래프

plt.figure(figsize=(8, 4))

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])

plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend([
    "Train",
    "Validation"
])

plt.show()

# 예측

pred = model.predict(x_test)
print(pred)

# 새로운 환자 예측

new_patient = np.array([
    [2, 120, 70, 20, 85, 25.0, 0.3, 35]
])

new_patient = scaler.transform(new_patient)
result = model.predict(new_patient)

print()
print("당뇨병 확률 :", round(result[0][0] * 100, 2), "%")

if result[0][0] >= 0.5:
    print("예측 : 당뇨병")
else:
    print("예측 : 정상")
