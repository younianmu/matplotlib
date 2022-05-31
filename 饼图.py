import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
pie()参数
➢ x：表示扇形或楔形的数据。
➢ explode：表示扇形或楔形离开圆心的距离。
➢ labels：表示扇形或楔形对应的标签文本。
➢ autopct：表示控制扇形或楔形的数值显示的字符串，可通过格式字符串指定小数点后的位数。
➢ pctdistance：表示扇形或楔形对应的数值标签距离圆心的比例，默认为0.6。
➢ shadow：表示是否显示阴影。
➢ labeldistance：表示标签文本的绘制位置（相对于半径的比例），默认为1.1。
➢ startangle：表示起始绘制角度，默认从x轴的正方向逆时针绘制。
➢ radius：表示扇形或楔形围成的圆形半径。
➢ wedgeprops：表示控制扇形或楔形属性的字典。例如，通过wedgeprops = {'width': 0.7} 将楔形的宽度设为0.7。
➢ textprops：表示控制图表中文本属性的字典。
➢ center：表示图表的中心点位置，默认为（0,0）。
➢ frame：表示是否显示图框。
'''

#绘制饼图
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制饼图：半径为0.5，数值保留1位小数
plt.pie(data, radius=1.5, labels=pie_labels, autopct='%3.1f%%')
plt.show()

#绘制圆环图
data = np.array([20, 50, 10, 15, 30, 55])
pie_labels = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
# 绘制圆环图
plt.pie(data, radius=1.5, wedgeprops={'width': 0.7},labels=pie_labels, autopct='%3.1f%%',pctdistance=0.75)
plt.show()





