from cProfile import label

import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

'''
xlabel,ylabel参数
➢ xlabel：表示x轴标签的文本。
➢ ylabel：表示y轴标签的文本。
➢ fontdict：表示控制标签文本样式的字典。
➢ labelpad：表示标签与x轴轴脊间的距离。
'''

x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
plt.ylabel("y轴")
plt.xlabel("x轴")
plt.show()

'''
使用pyplot模块的xlim()和ylim()函数分别可以设置或获取x轴和y轴的刻度范围。
即坐标轴的刻度范围取决于数据中的最大值和最小值。
使用pyplot模块的xticks()或yticks()函数可以设置x轴或y轴的刻度线位置和刻度标签。
'''

plt.plot(x,y)
#x,y都是1-10
plt.xlim(1,10)
plt.ylim(1,10)
plt.show()

plt.plot(x,y)
#x只显示4,5,6 y只显示1,2,3
plt.yticks(ticks=[1,2,3],labels=['','',''])
plt.xticks(ticks=[4,5,6],labels=['','',''])
plt.show()

'''
title()参数
➢ label:表示标题的文本。
➢ fontdict:表示控制标题文本样式的字典。
➢ loc:表示标题的对齐样式。
➢ pad:表示标题与图表顶部的距离，默认为None。
'''

plt.plot(x,y)
plt.title("test")
plt.show()

'''
添加图例
legend()参数
➢ handles:表示由图形标识构成的列表。
➢ labels:表示由图例项构成的列表。
➢ loc:用于控制图例在图表中的位置。
➢ ncol:表示图例的列数，默认值为1。
➢ title：表示图例的标题，默认值为None。
➢ shadow ：表示是否在图例后面显示阴影，默认值为None。
➢ fancybox：表示是否为图例设置圆角边框，默认值为None

• 在使用pyplot的绘图函数绘图时，若已经预先通过label参数指定了显示于图例的标签，则后续可以直接调用legend()函数添加图例。
• 若未预先指定应用于图例的标签，则后续在调用legend()函数时为handles和labels参数传值即可。
'''

plt.plot([1,2,3],label='test')
plt.legend()
plt.show()


lines = plt.plot([1,2,3],[1,2,3],
                 [1,2,3],[4,5,6],
                 [1,2,3],[7,8,9])
plt.legend(('label1', 'label2', 'label3'),loc='center')
plt.show()

'''
显示网格
grid()参数
➢ b：表示是否显示网格。
➢ which：表示显示网格的类型，默认为major。
➢ axis：表示显示哪个方向的网格，默认为both。
➢ linewidth 或 lw：网格线的宽度。
'''

plt.plot([1,2,3],[1,2,3])
plt.grid(b=True)
plt.show()

'''
添加水平参考线
axhline()参数
➢ y:表示水平参考线的纵坐标。
➢ xmin:表示水平参考线的起始位置，默认为0。
➢ xmax:表示水平参考线的终止位置，默认为1。
➢ linestyle:表示水平参考线的类型，默认为实线。

添加垂直参考线
axvline()参数
➢ x:表示水平参考线的纵坐标。
➢ ymin:表示水平参考线的起始位置，默认为0。
➢ ymax:表示水平参考线的终止位置，默认为1。
➢ linestyle:表示水平参考线的类型，默认为实线。
'''
plt.plot([1,2,3],[1,2,3])
plt.axvline(x=2, linestyle='--')
plt.axhline(y=2, linestyle='--')
plt.show()

'''
添加水平参考区域
axhspan()参数
➢ ymin:表示水平跨度的下限，以数据为单位。
➢ ymax:表示水平跨度的上限，以数据为单位。
➢ xmin:表示垂直跨度的下限，以轴为单位，默认为0。
➢ xmax:表示垂直跨度的上限，以轴为单位，默认为1。
➢ alpha:表示区域透明度

添加垂直参考区域
axvspan()参数
➢ xmin:表示水平跨度的下限，以数据为单位。
➢ xmax:表示水平跨度的上限，以数据为单位。
➢ ymin:表示垂直跨度的下限，以轴为单位，默认为0。
➢ ymax:表示垂直跨度的上限，以轴为单位，默认为1。
➢ alpha:表示区域透明度
'''

plt.plot([1,2,3],[1,2,3])
plt.axvspan(xmin=0.5, xmax=2.0, alpha=0.3)
plt.axhspan(ymin=0.5, ymax=1.0, alpha=0.3)
plt.show()

'''
添加指向性注释文本
annotate()参数
➢ s：表示注释文本的内容。
➢ xy：表示被注释的点的坐标位置，接收元组（x,y）。
➢ xytext ：表示注释文本所在的坐标位置，接收元组（x,y）。
➢ arrowprops ：表示指示箭头的属性字典。详细见箭头类型.png
➢ bbox：表示注释文本的边框属性字典。
'''

plt.plot([1,2,3],[1,2,3])
plt.annotate("test",xy=(1,1),xytext=(1,2),arrowprops=dict(arrowstyle='->'))
plt.show()

'''
添加无指向性注释文本
text()参数
➢ x, y:表示注释文本的位置。
➢ s:表示注释文本的内容。
➢ fontdict：表示控制字体的字典。
➢ bbox：表示注释文本的边框属性字典。
➢ horizontalalignment或ha：表示水平对齐的方式，可以取值为'center'、'right'或 'left'。
➢ verticalalignment或va：表示垂直对齐的方式，可以取值为'center'、'top'、'bottom'、'baseline'或'center_baseline'
'''

import matplotlib.pyplot as plt
plt.plot([1,2,3],[1,2,3])
plt.text(2,1,'wtf',5,5,'test')
plt.show()

'''
添加表格
table()参数
➢ cellText：表示表格单元格中的数据，可以是一个二维列表。
➢ cellColours：表示单元格的背景颜色。
➢ cellLoc：表示单元格文本的对齐方式，支持'left'、'center'、'right'三种取值，默认值为'right'。
➢ colWidths：表示每列的宽度。
➢ rowLabels：表示行标题的文本。
➢ rowLoc：表示行标题的对齐方式。
➢ colLabels：表示列标题的文本。
➢ colColours：表示列标题所在单元格的背景颜色。
➢ colLoc：表示列标题的对齐方式。
➢ loc：表示表格对于绘图区域的对齐方式。
'''

import matplotlib.pyplot as plt
plt.plot([1,2,3],[1,2,3])
plt.table(cellText=[[6, 6, 6], [8, 8, 8]], colWidths=[0.1] * 3, rowLabels=['第1行', '第2行'], colLabels=['第1列', '第2列', '第3列'], loc='lower right')
plt.show()

'''
填充区域
fill()
➢ *args：表示x坐标、y坐标或颜色的序列。
➢ facecolor：表示填充的背景颜色。
➢ edgecolor：表示边框的颜色。
➢ linewidth：表示边框的宽度。

fill_between()
➢ x：表示x轴坐标的序列。
➢ y1：表示第一条曲线的y轴坐标。
➢ y2：表示第二条曲线的y轴坐标。
➢ where：布尔值，表示要填充区域的条件。y1>y2说明第一条曲线位于第二条曲线上方时填
充；y1<y2说明第二条曲线位于第一条曲线上方时填充。

fill_betweenx()
➢ y：表示y轴坐标的序列。
➢ x1：表示第一条曲线的x轴坐标。
➢ x2：表示第二条曲线的x轴坐标。
➢ where：布尔值，表示要填充区域的条件。x1>x2说明第一条曲线位于第二条曲线右方时填
充；y1<y2说明第二条曲线位于第一条曲线右方时填充。
'''

x = [0, 0, 5, 10, 15, 15, 10, 5 ]
y = [5, 10, 15, 15, 10, 5, 0, 0]
list = np.arange(0, 16, 5)
plt.fill(x, y, color="red")
plt.xticks(list)
plt.yticks(list)
plt.show()

x = np.linspace(0, 8 * np.pi, 1000)
sin_y = np.sin(x)
cos_y = np.cos(1.5 * x / np.pi) / 2
plt.plot(x, sin_y)
plt.plot(x, cos_y)
plt.fill_between(x, cos_y, sin_y, cos_y < sin_y, color='dodgerblue', alpha=0.5)
plt.fill_between(x, cos_y, sin_y, cos_y > sin_y, color='orangered', alpha=0.5)
plt.show()











