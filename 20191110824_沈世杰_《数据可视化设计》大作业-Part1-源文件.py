# 任务1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

x=np.arange(6) # x=0-4
y_man = np.array([175.44,175.32,175.24,174.88,174.58,174.49])
y_woman = np.array([169.45,167.33,165.25,164.88,164.58,164.50])
bar_width = 0.3
plt.table(cellText=[[175.44,175.32,175.24,174.88,174.58,174.49], [169.45,167.33,165.25,164.88,164.58,164.50]], rowLabels=['男', '女'], colLabels=['山东', '北京', '黑龙江', '辽宁', '内蒙','河北']
          , loc='center right')
rects1=plt.bar(x, y_man,width=bar_width,alpha=0.5)
rects2=plt.bar(x+bar_width, y_woman, width=bar_width,alpha=0.5)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()  # 获取每个矩形条的高度
        plt.text(rect.get_x() + rect.get_width() / 2, height, s='{}'.format(height),ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.xticks(ticks=x+0.15,labels=['山东', '北京', '黑龙江', '辽宁', '内蒙','河北'])
plt.ylabel("平均身高（cm）")
plt.title("Top6省男生,女生平均身高")
plt.legend(('男', '女'),loc='lower left')
plt.show()

# Top6省男生平均身高在174.49以上，最高为175.44，相差不道2cm,女生平均身高在164.5以上，最高为169.45，相差5cm

#任务2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('fivethirtyeight')
x=np.arange(12)
y2018=[96.4,67.7	,95.7,	35.6	,84.6	,171.6	,57.2,	122.8,	249.4,	193.3,	97.8,	156.7]
y2019=[62.9,	20.6,	75.7,	93.3	,72.8,	158.3,	37.6,	319.5,	351.5,	96.9	,79.5	,20.2]
plt.xticks(ticks=x,labels=['1月', '2月', '3月', '4月', '5月','6月','7月','8月','9月','10月','11月','12月'])
plt.plot(x,y2018,color='#8B0000',marker='^',linestyle='--',linewidth=1.5)
plt.plot(x,y2019,color='#006374',marker='d',linestyle='-',linewidth=1.5)
plt.ylabel('降水量（mm）')
plt.show()

# 2018年降雨量最多的在8，9月，最低在2,12月；2019年降雨量最多的在9,10月，最低在4,7月

#任务3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
dim_num = 8
data = np.array([[3.6,4.43,4.31], [3.11,2.95,2.44], [4.49,4.48,3.75],
[3.72,4.33,4.63], [2.54,2.65,1.75], [4.35,4.43,2.5],[4.28,4.28,3.5],[1.75,2.05,3.13]])
angles = np.linspace(0, 2 * np.pi, dim_num, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
data = np.concatenate((data, [data[0]]))
# 维度标签
radar_labels = ['易抽取性', '粉尘量', '分层情况', '平整性', '厚度', '细腻度','柔软度','韧性']
radar_labels = np.concatenate((radar_labels, [radar_labels[0]]))
# 绘制雷达图
plt.polar(angles, data)
# 设置极坐标的标签
plt.thetagrids(angles * 180/np.pi, labels=radar_labels)
# 填充多边形
plt.fill(angles, data,alpha=0.25)
plt.legend(('产品A', '产品B','产品C'),loc='lower right')
plt.show()

# 产品A和B在分层情况，细腻度和柔软度方面做的最好，产品C则在平整性和易抽取性上做的最好

#任务4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 画第1个图：圆环图
plt.subplot(221)
data = np.array([59219,55466,47544,36443,35917])
pie_labels = np.array(['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java'])
# 绘制圆环图
plt.pie(data, radius=1.5, wedgeprops={'width': 0.7},labels=pie_labels, autopct='%3.1f%%',pctdistance=0.75)



# 画第2个图：散点图
plt.subplot(222)
plt.xlabel('价格（元）')
plt.ylabel('销量（万件')
plt.scatter([2.50,1.23,4.02,3.25,5.00,4.40], [34,62,49,22,13,19])



# 画第3个图：箱型图
plt.subplot(223)
plt.boxplot([6.2,9.8,9.8,7.8,7.2,6.4,9.8,7.8,7,9.8,10,7.5],vert=False , meanline=True, widths=0.3, patch_artist=True, showfliers=False)



# 画第4个图：直方图
plt.subplot(224)
data=[131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136]
plt.hist(data, bins=8, histtype='stepfilled')
plt.show()

#JavaScript的用户量最多，占比25.2%；Java的用户量最少，占比15.3%
#价格与销量成反比，但在价格为4.2元时销量却比2到3元要高
# 中位线靠近8，接近下四分位，说明一年中大部分月份的销售额都较高
# 在100到110之间数值最低，在130到140之间数值最高










