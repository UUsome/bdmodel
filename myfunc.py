def jisuan(new,rate,long):
	for i in range(1,long):
		if long == 1:
			new = new
		else:
			new = new+new*rate
	print(int(new))