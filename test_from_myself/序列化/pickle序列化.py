import pickle
d=dict(name="bob",age=23,score=88)
d2={"name":"tom","age":23,"score":88}
mystr=pickle.dumps(d)
print(mystr)

with open("test.json","wb") as f:
	pickle.dump(d,f)
	print("写入成功")

with open("test.json","rb") as rf:
	dt=pickle.load(rf)
	print(dt)