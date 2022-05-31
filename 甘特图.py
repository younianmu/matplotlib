import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

ticks = np.array(['报告提交', '数据分析', '数据录入', '实地执行', '问卷确定', '试访', '问卷设计', '项目确定'])
y_data = np.arange(1, 9)
x_data = np.array([0.5, 1.5, 1, 3, 0.5, 1, 1, 2])
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.barh(y_data, x_data, tick_label=ticks, left=[7.5, 6,
5.5, 3, 3, 2, 1.5, 0], color='#CD5C5C')
[ax.spines[i].set_visible(False) for i in ['top', 'right']]
ax.set_title("任务甘特图")
ax.set_xlabel("日期")
ax.grid(alpha=0.5, axis='x')
plt.show()