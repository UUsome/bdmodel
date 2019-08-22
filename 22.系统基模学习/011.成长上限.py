import numpy as np 
from matplotlib import pyplot as plt 


'''
#成长上限(Limits to Growth)  经济学中的边际效应递减模式   logistic模型
因果回路图：
  此处研究对象是成长，所以边界即为成长相关因素：促进因素，抑制因素，限制因素
建模：促进因素-成长情况-抑制因素 （限制因素外部因素变量也叫悬摆）
流量存量图： 流入   | 存量  | 流出  | 关系
分析：
  存量：成长速度状态-- GrowthState=20 
  流量： 自然增长率 = 促进因素 - 抑制因素
  	流入量：促进因素  
  	流出量：抑制因素  
    流入速率： a时刻自然增长率 = 初始自然增长率*（1 - a时刻整体存量/成长极限K ）

  常量：成长极限 K -- 600 ;
  因变量：时间 time
  辅助变量： （这个词是瞎扯的）--  
  			damping = if GrowthState in (0,50) then 0
  						 GrowthState in (50,100) then 0.05
  						 GrowthState in (100,200) then 0.45

方程：
	成长速度 = 成长速度 + 促进因素 - 抑制因素
  成长极限 <  累计（成长速度）
  抑制因素 = 成长极限-

多情况模拟&定量观察：
    物极必反的实例 
    到某一临界 越努力反作用越大 (S型，或者 前期指数，后期震荡)
'''
 
#  logistic(初始数量，初始自然增长率，成长极限，时间，标志): f=1显示速度，2显示累计
def logistic(n,r,k,t,f):
    for i in range(1,t):
        if r<=0:
          n = n
          r = 0.1
        else:
          n = n + n*r*(1-n/k)
          r = r*(1-n/k)

    if f==1:
        return r
    else:
        return n

# 定义时间区间
x = np.arange(1,20,1) 

#初始化参数
n = 1
r = 0.1
k = 10


#subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True,subplot_kw=None, gridspec_kw=None, **fig_kw)
fig, axs = plt.subplots(2, 1 )   #两行，一列 。两个图像

'''
# 初步完成模型
y = [logistic(n,r*0.1,k,i,1) for i in x]
z = [logistic(n,r*0.1,k,i,2) for i in x]
axs[0].plot(x,y,label='y') 
axs[1].plot(x,z,label='显示累计') 
axs[1].legend(loc='upper right', shadow=False)
'''

plt.title("成长上线")

 
#多个对比 1, K定，r变
y = [logistic(n,r*200.0,k,i,1) for i in x]

z = [logistic(n,r*200.0,k,i,2) for i in x]


axs[0].plot(x,y,label='y0') 
axs[0].set_title("数量")
axs[0].legend(loc='upper right', shadow=False)


axs[1].plot(x,z,label='z0') 


axs[1].set_title('增长率')
axs[1].legend(loc='upper right', shadow=False)
 


plt.show()

