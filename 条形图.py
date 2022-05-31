import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
barh()参数
➢ y：表示条形的y值。
➢ width：表示条形的宽度。
➢ height：表示条形的高度，默认值为0.8。
➢ left：条形左侧的x坐标值，默认值为0。
➢ align：表示条形的对齐方式，默认值为“center”,即条形与刻度线居中对齐。
➢ tick_label：表示条形对应的刻度标签。
➢ xerr，yerr：若未设为None，则需要为条形图添加水平/垂直误差棒。
'''

#绘制有一组条形的条形图
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
# 条形的粗细
bar_height = 0.3
# 绘制条形图
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
plt.show()

#绘制有两组条形的条形图
y = np.arange(5)
x1 = np.array([10, 8, 7, 11, 13])
x2 = np.array([9, 6, 5, 10, 12])
bar_height = 0.3
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
plt.barh(y+bar_height, x2,height=bar_height)
plt.show()

#绘制堆积条形图
#在使用barh()函数绘制图表时，可以通过给left参数传值的方式控制条形的x值，使后绘制的条形位于先绘制的条形右方。
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
plt.barh(y, x2, left=x1, height=bar_height)
plt.show()

#绘制有误差棒的条形图
#可以通过给xerr、yerr参数传值的方式为条形添加误差棒。
# 偏差数据
error = [2, 1, 2.5, 2, 1.5]
plt.barh(y, x1, tick_label=['a', 'b', 'c', 'd', 'e'], height=bar_height)
plt.barh(y, x2, left=x1, height=bar_height, xerr=error)
plt.show()



