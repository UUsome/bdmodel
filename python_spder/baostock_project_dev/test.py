
import re

str ='<a class="xi2" href="http://www.eweb.net.cn/article-101657-1.html" style="" target="_blank">周一2019年6月10日最具有爆发力的十大金股(名单)</a>'

# b = re.match("[十大金股]", str)
# b = re.match("</a>$", str)
if re.search("\(名单\)</a>$", str):
	print(str)
else:
	print('err')


# print(b)
