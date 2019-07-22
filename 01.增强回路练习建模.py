import numpy as np 
from matplotlib import pyplot as plt 

'''
建模：对工作负荷-处理能力-失误频率 建模
方程：
设：
	设 时间为X小时；
	设 处理能力为A = 10 个/H；
	设 新接工作为 N =7 个/H;
	设 负担极限为 L = 13 个/H；
	设 出错频率为v=0.2 ,即假设处理10个任务出错会两个出错
	那么 流入量为：待处理工作 =  N + 本小时出错任务
		 流出量为：10个
		 工作负荷为： 暂定位待处理工作个数
	则有以下方程

'''

#函数计算，貌似暂时不行
def jisuan(new,rate,long):
	for i in range(1,long):
		if long == 1:
			new = new
		else:
			new = new+new*rate
	return int(new)
	# print(int(new))

x = np.arange(1,7)
y = jisuan(7,0.2,x)
 
plt.title("工作能力模型") 
plt.xlabel("时间") 
plt.ylabel("工作负荷") 
print(x,y)
plt.plot(x,y)  #可以被格式化
# plt.plot(x,z,'g')  #可以被格式化
# plt.plot(x,t,'b')  #可以被格式化

plt.show()


	