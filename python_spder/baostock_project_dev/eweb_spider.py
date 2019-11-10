#获取目的URL
import requests
from urllib import parse
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
# 格式化成2016-03-20 11:45:39形式
now=time.strftime("%Y%m%d", time.localtime())


# 参数： url
# 返回： suburl_list
# ~~~~~~~~~~~获取了对应的url ~~~~~~~~~
def getsuburl(url):
	L_suburl=[]
	# url = 'http://www.eweb.net.cn/jiangu/index.php?page=20'
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"lxml")
	def not_lacie(href):
	        return href and re.compile("http://www.eweb.net.cn/article").search(href)
	b=soup.find_all(href=not_lacie)




	for i in range(len(b)):
		if i%3 ==1:
			L_suburl.append(b[i].get('href'))
			# print(b[i])
			# print(b[i].get('href'))
	return L_suburl

b=getsuburl('http://www.eweb.net.cn/jiangu/index.php?page=19')
for i in range(len(b)):
    # print(b[i])
    for x in range(1,9):
        a = b[i][0:38] +'{}'.format(x)+ b[i][39:50]
        print(a)
# 参数：url
# 返回：L_gupiaocode
# # ~~~~~~~~~~~从URL里获取股票code ~~~~~~~~~
def getcode(url):
	L_code=[]
	paragraphs = []
	# url = 'http://www.eweb.net.cn/article-112772-1.html'
	r = requests.get(url)
	s = BeautifulSoup(r.text,"html5lib")
	st_str=str(s.find_all('title'))
	st_list = re.findall(r'(\d+)',str(st_str))
	st=''
	for i in range(len(st_list)):
		st += st_list[i]
	st=datetime.strptime(st, "%Y%m%d").strftime("%Y%m%d")
    # st=str(st)
	# st=datetime.strptime(st, '%Y%m%d')
	# st=time.strptime(st,fmt='%Y%m%d')
	
	s2=s.find_all('table')
	for x in s2:
		paragraphs.append(str(x))
		L_code += re.findall(r'\((\d{6})',str(paragraphs))
	return st,L_code

 
# t,c =getcode('http://www.eweb.net.cn/article-112772-1.html')
# print(t,c)

# r_code=[]
# for i in range(1,7):
# 	url='http://www.eweb.net.cn/article-112772-{}.html'.format(i)
# 	r = getcode(url)
# 	r_code += r
# print(now,r_code)


 

