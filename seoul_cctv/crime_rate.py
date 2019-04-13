import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from sklearn import preprocessing

ctx = '../data/'
df_crime_police = pd.read_csv(ctx+'crime_police.csv',
                              sep=',',
                              encoding='utf-8')
print(df_crime_police.columns)
"""
['Unnamed: 0', '관서명', '살인 발생',
 '살인 검거', '강도 발생', '강도 검거', 
 '강간 발생',
       '강간 검거', '절도 발생', '절도 검거',
        '폭력 발생', '폭력 검거', '구별']
"""
df_police = pd.pivot_table(df_crime_police,
                           index='구별',
                           aggfunc=np.sum)
print(df_police.columns)
"""
['Unnamed: 0', '강간 검거', '강간 발생', 
'강도 검거', '강도 발생', '살인 검거',
 '살인 발생',
       '절도 검거', '절도 발생', 
       '폭력 검거', '폭력 발생']
"""
# aggfunc 는 평균값 리턴

df_police['강간검거율'] = df_police['강간 검거'] / df_police['강간 발생'] * 100
df_police['강도검거율'] = df_police['강도 검거'] / df_police['강도 발생'] * 100
df_police['살인검거율'] = df_police['살인 검거'] / df_police['살인 발생'] * 100
df_police['절도검거율'] = df_police['절도 검거'] / df_police['절도 발생'] * 100
df_police['폭력검거율'] = df_police['폭력 검거'] / df_police['폭력 발생'] * 100


df_police.drop()
