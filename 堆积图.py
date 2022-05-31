import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
stackplot()参数
➢ x：表示x轴的数据，可以是一维数组。
➢ y：表示y轴的数据，可以是二维数组或一维数组序列。
➢ labels：表示每个填充区域的标签。
➢ baseline：表示计算基线的方法，包括zero、sym、wiggle和
weighted_wiggle。其中zero表示恒定零基线，即简单的叠加图；
sym表示对称于零基线；wiggle表示最小化平方斜率之和；
weighted_wiggle表示执行相同的操作，但权重用于说明每层的大小。
'''

#绘制有三个填充区域堆叠的堆积面积图
x = np.arange(6)
y1 = np.array([1,4,3,5,6,7])
y2 = np.array([1,3,4,2,7,6])
y3 = np.array([3,4,3,6,5,5])
# 绘制堆积面积图
plt.stackplot(x, y1, y2, y3)
plt.show()