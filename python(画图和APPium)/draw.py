# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

import random
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def drawMemoryReport(MemoryList = [], pos = 121, key = 150):
	def getRandomList(feed, length):
		list = []

		for i in range(length):
			feed = random.randint(feed-1, feed+1)
			list.append(feed)

		return list

	font_xy_labal = {'family' : 'serif',
			'color'  : 'slategrey',
			'weight' : 'normal',
			'size'   : 10,
			}

	font_xy_title = {'family' : 'calibri',
			'color'  : 'black',
			'weight' : 'normal',
			'size'   : 15,
			}

	#设置画板大小和分辨率
	plt.figure(figsize=(8,4), dpi=180)

	#设置x,y轴个性化刻度
	key = math.floor(key/10)*10-5
	k1 = key
	y_ = []
	for i in range(11):
		if i == 0:
			y_.append("")

		y_.append(str(k1) + ' MB')
		k1 += 5

	x_ = ['','0 min','20 min','40 min','60 min','80 min','100 min','120 min']
	plt.xticks(range(7), x_)
	plt.yticks(range(11), y_)

	#设置x,y轴标签
	plt.xlabel('Time (Minute)', fontdict=font_xy_labal)
	plt.ylabel('Memory Usage (MB)', fontdict=font_xy_labal)
	plt.title('IRIS Hub Memory Leak Monitor', fontdict=font_xy_title)
	plt.xticks(fontproperties='calibri', fontweight='light', fontsize=8)
	plt.yticks(fontproperties='calibri', fontweight='light', fontsize=6.3)

	#设置刻度范围
	plt.axis([0, 120, key, key+50])

	#设置主副刻度
	ax = plt.axes()
	ax.xaxis.set_major_locator(MultipleLocator(20))
	ax.yaxis.set_major_locator(MultipleLocator(5))
	ax.xaxis.set_minor_locator(MultipleLocator(1))
	ax.yaxis.set_minor_locator(MultipleLocator(0.5))

	plt.tick_params(axis='x', which='major', width=1, colors='black')
	plt.tick_params(axis='x', which='minor', width=0.4, colors='slategrey')
	plt.tick_params(axis='y', which='major', width=0.7, colors='black')
	plt.tick_params(axis='y', which='minor', width=0.3, colors='slategrey')

	#设置边框宽度
	ax.spines['left'].set_linewidth(0.5)
	ax.spines['right'].set_linewidth(0.5)
	ax.spines['top'].set_linewidth(0.3)
	ax.spines['bottom'].set_linewidth(0.3)

	#设置背景虚线
	plt.grid(True,color='gainsboro', linestyle='--', linewidth=0.25)


	#设置点的范围
	x = range(pos)
	y = MemoryList
	#y = getRandomList(150,121)

	#画图，设置Legend标签
	plt.plot(x, y, linewidth = '0.75', label = '2 Hours\' Line', color='orangered')
	plt.legend(loc='upper left', fontsize=6.4)

	#这段要写在show前面 不然一片白。 安装pillow才可以画jpg
	plt.savefig("easyplot.png")
	#plt.show()

	ax.remove()
	plt.close()




#drawMemoryReport([], 121, 138)