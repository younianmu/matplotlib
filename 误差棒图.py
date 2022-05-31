import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
errorbar()参数
➢ x，y：表示数据点的位置。
➢ xerr，yerr：表示数据的误差范围。
➢ fmt：表示数据点的标记样式和数据点之间连接线的样式。
➢ elinewidth：表示误差棒的线条宽度。
➢ capsize：表示误差棒边界横杆的大小。
➢ capthick：表示误差棒边界横杆的厚度。
'''

x = np.arange(5)
y = (25, 32, 34, 20, 25)
y_offset = (3, 5, 2, 3, 3)
plt.errorbar(x, y, yerr=y_offset,
capsize=3, capthick=2)
plt.show()

x=np.arange(3)
y1 = np.array([2.04, 1.57, 1.63])
y2 = np.array([1.69, 1.61, 1.64])
y3 = np.array([4.65, 4.99, 4.94])
y4 = np.array([3.39, 2.33, 4.10])
error1 = [0.16, 0.08, 0.10]
error2 = [0.27, 0.14, 0.14]
error3 = [0.34, 0.32, 0.29]
error4 = [0.23, 0.23, 0.39]
bar_width = 0.2
plt.bar(x, y1,width=bar_width)
plt.bar(x + bar_width, y2, bar_width, align="center", tick_label=["春季", "夏季", "秋季"])
plt.bar(x + 2*bar_width, y3, bar_width)
plt.bar(x + 3*bar_width, y4, bar_width)
plt.errorbar(x, y1, yerr=error1, capsize=3, elinewidth=2, fmt=' k,')
plt.errorbar(x + bar_width, y2, yerr=error2, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 2*bar_width, y3, yerr=error3, capsize=3, elinewidth=2, fmt='k,')
plt.errorbar(x + 3*bar_width, y4, yerr=error4, capsize=3, elinewidth=2, fmt='k,')
plt.show()


















