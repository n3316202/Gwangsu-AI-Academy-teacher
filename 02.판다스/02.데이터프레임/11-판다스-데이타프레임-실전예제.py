# 대응표본이란 같은 대상에 대해 두 번의 측정을 한 후 두 측정치의 평균이 차이가 있는지 비교하는 통계적 방법

# 대응표본 t-검정 10명의 환자를 대상으로 수면영양제를 복용하기 전과 후의 수면시간을 측정하여 영양제의 효과가 있는지를 판단하고자 한다.
# 표본이 정규성을 만족한다는 가정하에 단측검정을 수행한다.

from scipy import stats
import pandas as pd
import pandas as pd

before = [7,3,4,5,2,1,6,6,5,4]
after = [8,4,5,6,2,3,6,8,6,5]

# 정규성 검사
normal_before = stats.shapiro(before)
normal_after = stats.shapiro(after)

#모두 p-value가 0.05보다 커서 정규성을 만족한다
print(normal_before)  #pvalue=np.float64(0.8352703969642297))
print(normal_after) #pvalue=np.float64(0.6177986322207938))

result = stats.ttest_rel(before,after)

print(result)

#결론)
# p-value 가 0.05 보다 작으므로 대립가설 채택
# 수면 영양제를 복용하기 전과 후의(통계적으로 유의미한),평균 체온은 차이가 있다


# 카이제곱 검정 (Chi-square)
# 범주형 변수 관계 확인


# 성별과 합격은 관련이 있을까?

# |   | 합격 | 불합격 |
# | - | -: | --: |
# | 남 | 40 |  10 |
# | 여 | 20 |  30 |

# 눈으로 보면:

# 남성 합격률 = 40/50 = 80%
# 여성 합격률 = 20/50 = 40%

# 이미 차이가 커 보입니다.
# 하지만 우연인지 진짜 차이인지 통계 검정을 합니다.

from scipy.stats import chi2_contingency

table = [
    [40,10],
    [20,30]
]

# 귀무: 성별과 합격여부는 관련이 없다.
# 대립: 성별과 한격여부는 관련이 있다.

print(chi2_contingency(table))

chi2,p,_,_ = chi2_contingency(table)

# pvalue=np.float64(0.00010516355403363114),
# p < 0.05 => 대립가설 채택
# 남성과 여성의 합격 비율차이는 우연이라고 보기 어려우며, 성별이 합격 여부에 관련되어 있다고 볼수 있다.

###======================================================================================

# 5. F 검정 (ANOVA)
# F 검정(ANOVA: 일원분산분석)
# 3개 이상 집단 평균 비교


# A/B/C 반 평균이 다를까?

# A 70 72 74
# B 80 82 85
# C 90 88 91

# F 검정 (ANOVA)
# 목적: 3개 이상 집단 평균 비교

from scipy import stats
import numpy as np

# 데이터
A = [70, 72, 74]
B = [80, 82, 85]
C = [90, 88, 91]

# 평균 확인
print("A 평균:", np.mean(A))
print("B 평균:", np.mean(B))
print("C 평균:", np.mean(C))

# 귀무가설 : 모든 반 평균이 동일하다
# 대립: 적어도 하나의 평균이 다르다.

# ANOVA 수행

f_stat, p_value =  stats.f_oneway(A,B,C)

print(f_stat, p_value)

# 결론
# p_value = 0.00013164033669208722
# 대립가설 채택
# 최소한 집단의 평균이 다른다.


# tips 통계적 분석 예제
# 1. total_bill 은 정규분포인가? (Shapiro)
import scipy.stats as stats
import seaborn as sns

tips = sns.load_dataset("tips")

st,p = stats.shapiro(tips["total_bill"])

print(st,p) # 3.324539186809091e-10
# 결론
# 0.05 보다 훨씬 작기 때문에 정규성을 만족 하지 않음
#  

# 시간대별 점심/저녁 팁 차이 (t-test)

# 귀무: 점심과 저녁에 팁차이가 없다.
# 대립: 점심과 저녁에 팁차이가 있다.

print(tips.head(5))
lunch = tips[tips["time"]=="Lunch"]["tip"]
dinner = tips[tips["time"]=="Dinner"]["tip"]

print(lunch)
print(dinner)

result = stats.ttest_ind(lunch,dinner)
print(result)

#  pvalue=np.float64(0.057801534751715615)
# 0.05 이상이므로 귀무가설유지 => 점삼과 평균의 팁차이가 통계적으로 유의 하의하다고 보기 어렴다.


# tips 예제
# 남성과 여성의 팁 금액 평균은 다를까? (t-test)
