import numpy as np 
from matplotlib import pyplot as plt 

'''
基模：
	增强回路 

建模：对工作负荷-处理能力-失误频率 建模
流量存量图： 流入   | 存量  | 流出0  | 关系
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
	if flag ==1:  #计算速率
		for i in range(1,numb):
			if numb == 1:
				inp = inp
			else:
				inp = inp+inp*rate
		return int(inp)
	elif flag ==2:    #计算累计
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
'''
# 初始化参数：
imput = 20 # input("请输入流入量：") 
output = 0 # input("请输入流出量：") 
v = 0.2 # input("请输入速率：")  
num = 100 # input("请输入单位长度：")
fl = 2


x = np.arange(1,num+1)
y = [fuli(imput,output,fl,v,i) for i in x]
z = [fuli(imput,output,2,v,i) for i in x]


plt.figure()       #定义一个图集
plt.subplot(211)  #第一个子图

plt.title("增强回路-1") 
plt.xlabel("时间") 
plt.ylabel("复利展示") 
plt.plot(x,y) 

plt.subplot(212) #第一个子图

plt.title("增强回路-2") 
plt.xlabel("时间") 
plt.ylabel("复利展示") 
plt.plot(x,z) 

plt.show()






# plt.legend(loc='upper right', shadow=False, fontsize='large')
 
 



 


 