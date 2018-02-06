#函数值传递和引用传递.py
def addOne(n):
	n+=1
	return n

def listAddOneByReference(lst):
	lst[0]+=1

def listAddOneByValue(lst):
	newList=lst[:]
	newList[0]+=1

def main():
	n=1
	addOne(n)
	print(n)  # 1

	lst=[1,1]
	listAddOneByValue(lst)
	print(lst)  # [1, 1]
	listAddOneByReference(lst)
	print(lst)  # [2, 1]
	

main()