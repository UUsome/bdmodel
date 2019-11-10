from eweb_spider import getsuburl,getcode
import sqlite3


conn = sqlite3.connect(r'E:\sqlite\tuijian.db')

r_code=[]
for i in range(1,7):
	url='http://www.eweb.net.cn/article-112772-{}.html'.format(i)
	t,r = getcode(url)
	# print(r)
	for j in range(len(r)):
		insr_str = "insert into tuijian (riqi,code) VALUES ({},'{}')".format(t,str(r[j]))
		#print(insr_str)
		conn.execute(insr_str)
	# r_code += r
# print(t,r_code)

conn.commit()
conn.close()
