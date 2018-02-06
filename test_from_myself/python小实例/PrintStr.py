#PrintStr.py
#在盒子里打印一个句子
#知识点：序列的乘法和加法
def printStr(string):
	sentence=string
	screen_width=80
	text_width=len(sentence)
	box_width=text_width+6
	left_margin=(screen_width-box_width)//2

	print()
	print(" "*left_margin+"+"+"-"*(box_width-2)+"+")
	print(" "*left_margin+"|  "+" "*text_width+"  |")
	print(" "*left_margin+"|  "+   sentence   +"  |")
	print(" "*left_margin+"|  "+" "*text_width+"  |")
	print(" "*left_margin+"+"+"-"*(box_width-2)+"+")
	print()

def main():
	printStr("hello world!")

if __name__ == '__main__':
	main()
