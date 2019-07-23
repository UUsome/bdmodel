import numpy as np 
from matplotlib import pyplot as plt 

#成长上限(Limits to Growth) 
    # 物极必反的实例 
    # 到某一临界 越努力反作用越大 (S型，或者 前期指数，后期震荡)

'''
建模：促进因素-成长情况-抑制因素 （限制因素外部因素变量也叫悬摆）
分析：
  存量：成长速度状态-- GrowthState=20 
  流量：
  	流入量：促进因素 -- stimulus = GrowthState*0.2
  	流出量：抑制因素 -- disincentive = GrowthState*
  常量：成长极限 -- 600 ;
  因变量：时间 time
  辅助变量： 抑制阻尼（这个词是瞎扯的）-- 
  			damping = if GrowthState in (0,50) then 0
  						 GrowthState in (50,100) then 0.05
  						 GrowthState in (100,200) then 0.45

方程：
	成长速度 = GrowthState + stimulus - GrowthState*damping
结果： 
'''

def Limits2Growth(GrowthState,stimulus,time):
	for i in range(1,time):
		if GrowthState<=50:
			GrowthState = GrowthState + GrowthState*stimulus
		elif GrowthState > 50 and GrowthState<=100:
			GrowthState = GrowthState + GrowthState*stimulus - GrowthState*0.01
		elif GrowthState > 100 :
			GrowthState = GrowthState + GrowthState*stimulus - GrowthState*0.06
	return GrowthState

GrowthState =20
stimulus =0.03
x = np.arange(1,600) 
y = [Limits2Growth(GrowthState,stimulus,i) for i in x]

plt.title("工作能力模型") 
plt.xlabel("时间") 
plt.ylabel("工作负荷") 
# print(x,y)
plt.plot(x,y)  
plt.show()






