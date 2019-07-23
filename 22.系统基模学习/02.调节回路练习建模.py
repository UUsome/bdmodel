import numpy as np 
from matplotlib import pyplot as plt 
'''
建模：水温差-室温-温度变化
方程：
  假设：
	室温：30 
	初始水温：100
	温度变化速率：水温差/2 

观察：
多情况模拟：
'''

''' tiaojie(差值，变化速率,时长) ''' 
def tiaojie(sub,rate,numb):
	for i in range(1,numb):
		if numb == 1:
			sub = sub
		else:
			sub = sub-sub*rate
	return int(sub)

num = 50
sub = 100-30
rate = 0.25
x = np.arange(1,num+1)
y = [tiaojie(sub,rate,i) for i in x]

plt.title("工作能力模型") 
plt.xlabel("时间") 
plt.ylabel("工作负荷") 
print(x,y)
plt.plot(x,y)  

plt.show()