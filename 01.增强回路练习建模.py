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

结果：指数增长 、复利效应
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

# 初始化参数：
imput = 17 # input("请输入流入量：") 
output = 5 # input("请输入流出量：") 
v = 0.3 # input("请输入速率：")  
num = 82 # input("请输入单位长度：")
fl = 2


x = np.arange(1,num+1)
# y = [fuli(imput,v,i) for i in x]
y = [fuli(imput,output,fl,v,i) for i in x]



plt.title("工作能力模型") 
plt.xlabel("时间") 
plt.ylabel("工作负荷") 
print(x,y)
plt.plot(x,y)  

plt.show()

'''
观察：
若：
	output/imput>v 指数增长 否则 归0 ；换言之，增强回路的增强前提是输入量大于输出量（貌似是废话，但看清废话很重要）

曾与朋友玩笑，真理都是废话，也以为虽是如此，但颇感好笑与失落，总觉有有疑问，却不知从何而起；而今似证，从底层证实事实，而白话表述，即所谓真理无须证明，悖之。佛家说众生无名，或许就是指所大家所依凭的判断都会限于自身，这一辩证看法。	



'''
	