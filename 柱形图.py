import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
bar()参数
➢ x:表示柱形的x坐标值。
➢ height:表示柱形的高度。
➢ width:表示柱形的宽度，默认为0.8。
➢ bottom:表示柱形底部的y值，默认为0。
➢ tick_label：表示柱形对应的刻度标签。
➢ xerr，yerr :若未设为None，则需要为柱形图添加水平/垂直误差棒。
'''

#两组柱形的柱形图
x=np.arange(5) # x=0-4
y1 = np.array([10, 8, 7, 11, 13])
y2 = np.array([9, 6, 5, 10, 12])
# 柱形的宽度
bar_width = 0.3
# 根据多组数据绘制柱形图
plt.bar(x, y1, tick_label=['a', 'b', 'c', 'd', 'e'], width=bar_width)
plt.bar(x+bar_width, y2, width=bar_width)
plt.show()

'''
在使用bar()函数绘制图表时，可以通过给该函数的bottom参数传值的方式控制柱形的y值，使后绘制的柱形位于先绘制的柱形的上方。
还可以通过给xerr、yerr参数传值的方式为柱形添加误差棒。
'''
# 偏差数据
error = [2, 1, 2.5, 2, 1.5]
# 绘制堆积柱形图
plt.bar(x, y1, tick_label=['a', 'b', 'c', 'd', 'e'], width=bar_width)
plt.bar(x, y2, bottom=y1,width=bar_width,yerr=error)
plt.show()








