import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('population.xlsx')
df_male = df.groupby(by='Gender').get_group('Male')
list_male = df_male['Number'].values.tolist() # 将ndarray 转换为 list
df_female = df.groupby(by='Gender').get_group('Female')
list_female = df_female['Number'].values.tolist() # 将ndarray 转换为 list
df_age = df.groupby('AgeGroup').sum()
count = df_age.shape[0]
y = np.arange(1, 11)
labels = []
for i in range(count):
    age = df_age.index[i]
    labels.append(age)
plt.barh(y, list_male, tick_label=labels, label=' 男', color='#6699FF')
plt.barh(y, list_female, tick_label=labels, label=' 女', color='#CC6699')
plt.ylabel("年龄段（岁）")
plt.xticks([-100000, -75000, -50000, -25000, 0, 25000, 50000, 75000, 100000],labels=['100000', '75000', '50000', '25000',
'0', '25000', '50000', '75000', '100000'])
plt.xlabel("人数（个）")
plt.title('某城市人口金字塔')
plt.legend()
plt.show()