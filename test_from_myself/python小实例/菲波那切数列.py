#菲波那切数列.py
#后一个数是前两个数之和
def getFibs(num):
	'文档字符串'
	fibs=[0,1]
	for i in range(num):
		fibs.append(fibs[-2]+fibs[-1])
	return fibs

def main():
	fibs=getFibs(8)
	print(fibs)
	print(getFibs.__doc__)

main()