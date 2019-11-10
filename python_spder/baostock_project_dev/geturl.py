# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:52:14 2019

@author: UU

首先从第一页 http://www.eweb.net.cn/jiangu/
中读取三类中的一类信息的url{周一2019年11月11日最具有爆发力的十大金股(名单)
，2019年11月11日周一券商评级可大胆加仓抢筹9股
，机构强推2019年11月11日号称摇钱树的六股（附股）}



"""
import requests
from urllib import parse
from bs4 import BeautifulSoup
import re

from datetime import datetime

# 
# 参数： 
	# n {1:2019年11月11日周一券商评级可大胆加仓抢筹9股
		# ,2: 周一2019年11月11日最具有爆发力的十大金股(名单) 默认值
		# ,3:机构强推2019年11月11日号称摇钱树的六股（附股）}
# url: 股票推荐主页面
# 返回：每日推荐股票的url第一页
def get_suburl(url):
	#url = 'http://www.eweb.net.cn/jiangu/index.php?page=20'
	L_suburl=[]
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html5lib")
	def not_lacie(href):
		return href and re.compile("http://www.eweb.net.cn/article").search(href)
	b=soup.find_all(href=not_lacie)
	for x in range(len(b)):
		if re.search("十大金股\(名单\)</a>$", str(b[x])):  # 以\(名单\)</a>
			# print(b[x])
			L_suburl.append(b[x].get('href'))
	return L_suburl
							


# 参数： url
# 返回： 日期 & code
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

s = get_suburl('http://www.eweb.net.cn/jiangu/index.php?page=3')
for m in range(len(s)):
	f =getcode(s[m])
	print(f)


# f =getcode('http://www.eweb.net.cn/article-104700-1.html')
# print(f)
