import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# x = np.arange(4, 19) x=4-18
x=[1,2,3]
y=[4,5,6]

'''
plot()参数
➢ x：表示x轴的数据，默认值为range(len(y))。
➢ y：表示y轴的数据。
➢ color：表示折线的颜色。
➢ marker：表示这线上数据点处的类型。
➢ linestyle：表示折线的类型。
➢ label：表示应用于图例的标签文本。
'''
plt.figure(1)
plt.plot(x,y,marker='^',color='red')

#创建两张画布，显示两张图
plt.figure(2)

#使用pyplot的plot()函数还可以绘制具有多个线条的折线图
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10,11,12]])
plt.plot(arr[0], arr[1:])
plt.show()

