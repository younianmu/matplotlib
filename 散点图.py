import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
scatter()参数
➢ x，y：表示数据点的位置。
➢ s：表示数据点的大小。
➢ c：表示数据点的颜色。
➢ marker：表示数据点的样式，默认为圆形。
➢ alpha：表示透明度，可以取值为0~1。
➢ linewidths：表示数据点的描边宽度。
➢ edgecolors：表示数据点的描边颜色。
'''

#绘制散点图
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter (x, y)
plt.show()

#绘制气泡图
x = np.random.rand(50)
y = np.random.rand(50)
area = (30 * np.random.rand(50))**2
plt.scatter(x, y, s=area)
plt.show()












