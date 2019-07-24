import numpy as np 
from matplotlib import pyplot as plt 

'''
# 调节回路

建模：水温差-室温-温度变化
分析：
  假设：
	室温：30 
	初始水温：100
	温度变化速度：水温差/2 


	存量：水温差 -- sub
	流量：
		流入量： (当前温度-目标温度)*温度变化速度 | 当 当前温度 > 目标温度
		流出量： (目标温度-当前温度)*温度变化速度 | 当 目标温度 > 当前温度
	常量： 目标温度
	因变量： 时间
	辅助变量： 温度变化速度

方程： 温差 = 温差 - 温差 * 温度变化速度
     当前温度 = abs(目标温度-当前温度(t-1))

多情况模拟&定量观察：

'''


''' tiaojie(差值，变化速率,时长) ''' 
def tiaojie(sub,rate,numb):
	for i in range(1,numb):
		if numb == 1:
			sub = sub
		else:
			sub = sub-sub*rate
	return int(sub)

num = 20
sub = 100-30
# rate = 1/2
x = np.arange(1,num+1)
y = [tiaojie(sub,0.5,i) for i in x]
y1 = [tiaojie(sub,0.25,i) for i in x]
y2 = [tiaojie(sub,0.1,i) for i in x]
y3 = [tiaojie(sub,0.01,i) for i in x]


plt.title("调节回路演示 ") 
plt.xlabel("时间 ") 
plt.ylabel("目标-现实差") 


# plt.plot(x,y,x,y1,x,y2,x,y3)  
plt.plot(x,y,label='速度0.5')
plt.plot(x,y1,label='速度0.25')  
plt.plot(x,y2,label='速度0.1')  
plt.plot(x,y3,label='速度0.01')  

plt.legend(loc='upper right', shadow=False)

plt.show()
 