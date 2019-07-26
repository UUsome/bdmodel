import numpy as np 
from matplotlib import pyplot as plt 
 

'''
#舍本逐末(Shifting the Burden) https://wiki.mbalib.com/wiki/%E8%88%8D%E6%9C%AC%E9%80%90%E6%9C%AB

建模（因果回路图）： [问题症状]增强[症状解]，且延迟增强[根本解]， [症状解]和[根本解]减弱[问题症状]，[症状解]对[根本解]有副作用。
流量存量图： 流入0 ； 问题大小 ； 流出：临时解/永久解 -- 临时解减弱永久解  流量存量图： 流入   | 存量  | 流出  | 关系
分析：
  存量： 问题大小程度（问题症状），
  流量：
  	流入量： 临时解决方案力度，
  	流出量： 
    流入速率： 
  常量：
  因变量：
  辅助变量： 

方程：

多情况模拟&定量观察：

'''
# func(参数说明)
def func(para,t):
    for i in range(1,t):
      n =  
      r =  
    if f==1:
        return r
    else:
        return n

#初始化参数
x = np.arange(1,100,1) 
p = 

#定义显示
#subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True,subplot_kw=None, gridspec_kw=None, **fig_kw)
fig, axs = plt.subplots(2, 1)   #两行，一列 。两个图像

y1 = [func(p1,...,i) for i in x]
y2 = [func(p2,...,i) for i in x]

z1 = [func(p1,...,i) for i in x]
z2 = [func(p2,...,i) for i in x]


axs[0].plot(x,y1,label='y1') 
axs[0].plot(x,y2,label='y2') 

axs[0].legend(loc='upper right', shadow=False)


axs[1].plot(x,z1,label='z1') 
axs[1].plot(x,z2,label='z2') 

axs[1].legend(loc='upper right', shadow=False)


plt.title("标题") 
plt.xlabel("x轴名称") 
plt.ylabel("y轴名称") 
# print(x,y,z)
plt.show()

