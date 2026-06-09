import pandas as pd
import numpy as np

df_emp = pd.read_csv("D:\Gwangsu-AI-Academy-teacher\emp.csv")

df_emp.info()
print(df_emp.describe())
print(df_emp.head())

# 1번) 사원이름과 월급을 출력하시오.
print(df_emp[['ename','sal']])
print(df_emp.loc[  : ,  ['ename','sal'] ] )

# 2번) 사원번호(empno), 이름(ename), 월급(sal), 직업(job)을 출력하시오.
print(df_emp[['empno','ename','sal','job']])
print(df_emp.loc[   :   ,['empno','ename','sal','job']])

# 3번) 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오.
print(df_emp.loc[   df_emp['sal'] >= 3000  ,['ename','sal']])
print(df_emp[['empno','ename']][df_emp['sal'] >=3000]  )