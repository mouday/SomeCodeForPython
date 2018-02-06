path=r"C:\Users\PSY\Desktop\020-03\P2017-08-17-000002.MCA"
with open(path,"r") as f:
	for line in f.readlines():
		print(line.strip())