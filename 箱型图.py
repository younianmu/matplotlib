import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
boxplot()参数
➢ x：绘制箱形图的数据。
➢ sym：表示异常值对应的符号，默认为空心圆圈。
➢ vert：表示是否将箱形图垂直摆放，默认为垂直摆放。
➢ whis：表示箱形图上下须与上下四分位的距离，默认为1.5倍的四分位差。
➢ positions：表示箱体的位置。
➢ widths：表示箱体的宽度，默认为0.5。
➢ patch_artist：表示是否填充箱体的颜色，默认不填充。
➢ meanline：是否用横跨箱体的线条标出中位数，默认不使用。
➢ showcaps：表示是否显示箱体顶部和底部的横线，默认显示。
➢ showbox：表示是否显示箱形图的箱体，默认显示。
➢ showfliers：表示是否显示异常值，默认显示。
➢ labels：表示箱形图的标签。
➢ boxprops：表示控制箱体属性的字典。
'''

data = np.random.randn(100)
plt.boxplot(data,vert=False , meanline=True, widths=0.3, patch_artist=True, showfliers=False)
plt.show()











