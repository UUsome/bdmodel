import numpy as np 
from matplotlib import pyplot as plt 

'''
基模：
	增强回路 

建模：对工作负荷-处理能力-失误频率 建模
流量存量图： 流入   | 存量  | 流出  | 关系
分析：
	设 时间为X小时；
	设 处理能力为A = 10 个/H；
	设 新接工作为 N =7 个/H;
	设 负担极限为 L = 13 个/H；
	设 出错频率为v=0.2 ,即假设处理10个任务出错会两个出错
	那么 流入量为：待处理工作 =  N + 本小时出错任务
		 流出量为：10个
		 工作负荷为： 暂定位待处理工作个数
	则有以下方程


方程： 

多情况模拟&定量观察：
	指数增长 、复利效应
	观察：
若：
	output/imput>v 指数增长 否则 归0 ；换言之，增强回路的增强前提是输入量大于输出量（貌似是废话，但看清废话很重要）

'''

#函数计算，复利函数
''' fuli(流入量inp,流出量,速率rate,单位数量numb,标记flag) 
	flag==1 计算累计流入量；flag==2 计算实际存量   '''
def fuli(inp,outp,flag,rate,numb):
	if flag ==1:
		for i in range(1,numb):
			if numb == 1:
				inp = inp
			else:
				inp = inp+inp*rate
		return int(inp)
	elif flag ==2:
		for i in range(1,numb):
			if numb == 1:
				if inp >= outp:
					inp = inp-outp
				else:
					inp = 0
			else:
				if inp+inp*rate >= outp:
					inp = inp+inp*rate-outp
				else:
					inp = 0	
		return int(inp)	
	# print(int(new))

def logistic(n,r,k,t,f):
  for i in range(1,t):
    n = n + n*r*(1-n/k)
    r = r*(1-n/k)
    if f==1:
      return r
    else:
      return n

'''

# 初始化参数：
imput = 20 # input("请输入流入量：") 
output = 15 # input("请输入流出量：") 
v = 0.2 # input("请输入速率：")  
num = 82 # input("请输入单位长度：")
fl = 2

x = np.arange(1,num+1)
y = [fuli(imput,output,fl,v,i) for i in x]

plt.title("增强回路") 
plt.xlabel("时间") 
plt.ylabel("复利展示") 
# print(x,y)
plt.plot(x,y)  
plt.show()
'''



#测试

x = np.arange(1,10)

y3 = [fuli(20,15,2,0.3,i) for i in x]
y4 = [fuli(20,15,2,0.4,i) for i in x]
y5 = [fuli(20,15,2,0.5,i) for i in x]
y6 = [fuli(20,15,2,0.6,i) for i in x]
y7 = [fuli(20,15,2,0.7,i) for i in x]
y8 = [fuli(20,15,2,0.8,i) for i in x]
y9 = [fuli(20,15,2,0.9,i) for i in x]


plt.title("增强回路") 
plt.xlabel("时间") 
plt.ylabel("复利展示") 

 

plt.plot(x,y3,label="0.3")
plt.plot(x,y3,label="0.3")
plt.plot(x,y4,label='0.4')
plt.plot(x,y5,label='0.5')
plt.plot(x,y6,label='0.6')
plt.plot(x,y7,label='0.7')
plt.plot(x,y8,label='0.8')
plt.plot(x,y9,label='0.9')

plt.legend(loc='upper right', shadow=False, fontsize='large')

plt.show()