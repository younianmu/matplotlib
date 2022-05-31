import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
contour(),contourf()参数
➢ X，Y：表示坐标点的网格数据。
➢ Z：表示坐标点对应的高度数据。
➢ levels：表示等高线的数量。若levels为n，则说明绘制n+1条等高线。
➢ colors：表示不同高度的等高线颜色。
➢ cmap：表示颜色映射表。
➢ linewidths：表示等高线的宽度。
➢ linestyles：表示等高线的线型。
'''

# 计算高度
def calcu_elevation(x1, y1):
    h = (1-x1/2 + x1 ** 5 + y1 ** 3) * np.exp(-x1** 2 - y1** 2)
    return h
n = 256
x = np.linspace(-2, 2, n)
y = np.linspace(-2, 2, n)
# 利用 meshgrid() 函数生成网格数据
x_grid, y_grid = np.meshgrid(x, y)
# 绘制等高线
con = plt.contour(x_grid, y_grid, calcu_elevation(x_grid, y_grid), 8,
colors='black')
# 填充等高线的颜色
plt.contourf(x_grid, y_grid, calcu_elevation(x_grid, y_grid), 8,
alpha=0.75, cmap=plt.cm.copper)
# 为等高线添加文字标签
plt.clabel(con, inline=True, fmt='%1.1f', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()







