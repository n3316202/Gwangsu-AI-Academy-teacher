import numpy as np

# NumPy 배열 생성
# 인덱싱
# 슬라이싱
# 벡터연산
# 통계
# 행렬연산
# 데이터 전처리

# 넘파이 특징
# 1. 모든 원소가 같은 자료형이어야 한다.
# 2. 원소의 갯수를 바꿀수 없다.

import numpy as np

# 넘파이 생성
#리스트에서 배열(numpy) 만들기
arr = np.array([1,2,3,4,5])
# print(type(arr))
# print(arr)
# print(dir(arr))

# 모든 원소가 같은 자료형으로 통일 시킴
arr = np.array([3.14 , "안녕" , 2 , 4 , 3])
print(arr) # ['3.14' '안녕' '2' '4' '3']
print(type(arr)) 

# 모든 원소가 같은 자료형으로 통일 시킴
arr = np.array([3.14 , 3 , 2 , 4 , 3])
print(arr) # 
print(type(arr)) 

# 넘파이에서는 데이타 타입을 지정해 줄수 있음
# 1. 정수형 (Integer)
# 타입	크기	범위
# int8	1 byte	-128 ~ 127
# uint8	1 byte	0 ~ 255
# int16	2 byte	-32,768 ~ 32,767
# uint16	2 byte	0 ~ 65,535
# int32	4 byte	-2,147,483,648 ~ 2,147,483,647
# uint32	4 byte	0 ~ 4,294,967,295
# int64	8 byte	-9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
# uint64	8 byte	0 ~ 18,446,744,073,709,551,615

# 2. 실수형 (Float)
# 타입	크기	대략적인 범위	정밀도
# float16	2 byte	±6.5 × 10⁴	약 3자리
# float32	4 byte	±3.4 × 10³⁸	약 7자리
# float64	8 byte	±1.8 × 10³⁰⁸	약 15~16자리

# 일반 숫자 → int32
# 큰 정수 → int64
# 딥러닝 → float32
# 과학 계산 → float64
# 메모리 절약 → float16
# arr = np.array( [2147483648 , 4 , 3], dtype='int32')
# print(arr)
# print(type(arr))

# 함수를 통한 배열 생성
# 0 으로 채운 배열 생성
arr = np.zeros(20)
print(arr)


arr = np.ones((3,5),dtype=int)
print(arr)
# [
#   [1 1 1 1 1]
#   [1 1 1 1 1]
#   [1 1 1 1 1]
# ]

arr = np.full( (3,5,2) , 3.14)
print(arr)
# [[[3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]]

#  [[3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]]

#  [[3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]
#   [3.14 3.14]]]


# 선형대수
# NumPy는 스칼라, 벡터, 매트릭스(행렬) 개념을 다룸

# 1. 스칼라 (Scalar)
# 하나의 숫자(크기만 있음)
# 3
# -1.5
# π
# 0
# 100

# 2. 벡터 (Vector)
#여러 개 숫자가 한 줄로 나열된 것 (1차원)
# [10, 20, 30]

# 3. 매트릭스 (Matrix, 행렬)
#행과 열로 이루어진 2차원 배열
# [
#  [1 2 3]
#  [4 5 6]
# ]

# 그럼 3차원 이상은?
# 3차원 이상은 보통 텐서(Tensor) 라고 부릅니다.

# 0에서 시작해 2씩 더해 20까지 채우는 배열 생성
#[ 0  2  4  6  8 10 12 14 16 18]
arr = np.arange(0,20,2)
print(arr)

# 랜덤함수로 배열생성
# 0 과 1 사이의 숫자중에 실수 난수
# [[0.46467712 0.94382138 0.80403385]
#  [0.24817824 0.60784263 0.13621165]
#  [0.11025444 0.78639582 0.36466975]]
arr = np.random.random((3,3))
print(arr)

# 1부터 10사이
arr = np.random.randint(1,10,(3,3))
print(arr)

# 로또 번호 6개를 넘파이 배열로 뽑아내시오.
# replace=False 
# 중복 없이
lotto = np.random.choice(np.arange(1,46),size=6,replace=False)
print(lotto)

arr =  np.array([10, 20, 30, 40, 50])
print(arr)

# 30보다 큰 값만 뽑아 내시오.
# for value in arr:
    
#     if value > 30:
#         print(value)

# 그런데 넘파이 배열 에서는 for문을 돌리면 왕따 당함 
# for 문 안돌리려고 numpy 배열 쓰는 거임 ㅋㅋㅋ
  

print(dir(arr))


# 엑셀 다루기

import pandas as pd

data = {
    "이름": ["홍길동", "김영희", "이철수"],
    "나이": [30, 25, 28],
    "직업": ["개발자", "디자이너", "기획자"]
}

df = pd.DataFrame(data)

df

df.to_excel("데이터.xlsx",index=False)

# 엑셀 파일 읽기
df_excel = pd.read_excel("데이터.xlsx")

df_excel.info()

print(df_excel.head())

# 데이터 베이스_판다스 연동
import pymysql
import pandas as pd
import numpy as np

conn = pymysql.connect(
    host="localhost",
    user="scott",
    password="tiger",
    database="scott",charset="utf8")

sql = "select * from emp"
df_emp = pd.read_sql(sql, conn)
print(df_emp)

df_emp.to_csv("emp.csv")
df_emp.to_excel("emp.xlsx")




