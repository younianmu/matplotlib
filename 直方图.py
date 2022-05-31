import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
hist()参数
➢ x：表示x轴的数据。
➢ bins：表示矩形条的个数，默认为10。
➢ range：表示数据的范围，若未设置范围，默认数据范围为(x.min(), x.max())。
➢ cumulative：表示是否计算累计频数或频率。
➢ histtype：表示直方图的类型，支持'bar'、'barstacked'、'step'、'stepfilled‘四种取值
                              'bar'为默认值，代表传统的直方图；
                              'barstacked'代表堆积直方图；
                              'step'代表未填充的线条直方图；
                              'stepfilled'代表填充的线条直方图。
➢ align：表示矩形条边界的对齐方式，可设置为'left'、'mid'或'right'，默认为'mid'。
➢ orientation：表示矩形条的摆放方式，默认为'vertical'，即垂直方向。
➢ rwidth：表示矩形条宽度的百分比，默认为0。若histtype的值为'step'或'stepfilled'，则直接忽略rwidth参数的值。
➢ stacked：表示是否将多个矩形条以堆叠形式摆放。
'''

#绘制填充的线条直方图
# 准备50个随机测试数据
scores = np.random.randint(0,100,50)
# 绘制直方图
plt.hist(scores, bins=8, histtype='stepfilled')
plt.show()











