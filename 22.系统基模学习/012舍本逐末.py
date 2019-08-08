import numpy as np 
from matplotlib import pyplot as plt 


'''
#舍本逐末(Shifting the Burden) https://wiki.mbalib.com/wiki/%E8%88%8D%E6%9C%AC%E9%80%90%E6%9C%AB
因果回路图：
  此处研究对象是问题的临时方案和永久方案对问题的影响。所以边界即为成长相关因素：促进因素，抑制因素，限制因素
建模（因果回路图）： [问题症状]增强[症状解]，且延迟增强[根本解]， [症状解]和[根本解]减弱[问题症状]，[症状解]对[根本解]有副作用。
流量存量图： 流入   | 存量  | 流出  | 关系
流量存量图： 流入 | 问题大小 | 流出 || 流出 = 永久解 - 临时解&副作用   延迟 = delay

临时解/永久解 -- 临时解减弱永久解  




分析：
  存量： 问题大小程度（问题症状）ProLever，
  流量：
  	流入量：  
  	流出量： 临时解决方案力度，tmpdo | 永久解决 foreverdo 
  常量： 问题症状，延迟，副作用（side effect）
  因变量： 时间
  辅助变量：  

方程： ProLever = ProLever - tmpdo - foreverdo | foreverdo = foreverdo - tmpdo*side_effect

多情况模拟&定量观察：

'''
# 舍本逐末func(问题存量，临时解，永久解，副作用，延时，时间)
def shebenzhumo(ProLever,tmpdo,foreverdo,side_effect,delay,t):
    for i in range(1,t):
      if i <= delay:
        ProLever = ProLever #- tmpdo
      else:
        #这里边[(foreverdo - tmpdo*side_effect)]表示当前时间-delay时刻的永久解。因为这里假设都是常量，所以都一样
        ProLever=ProLever - (foreverdo - delay*tmpdo*side_effect)   # - tmpdo 
    return ProLever

#初始化参数
PL = 100
TD = 10
FD = 5
SE = 0.15
DL = 10

x = np.arange(1,20,1) 

y = [shebenzhumo(PL,TD,FD,SE,DL,i) for i in x]


plt.plot(x,y,label='sdfs') 

plt.title("标题") 
plt.xlabel("x轴名称") 
plt.ylabel("y轴名称") 
# print(x,y,z)
plt.show()

