import json
d=dict(name="tom",age=23,score=89)
print(d)
s=json.dumps(d)
print(s)
rebuil=json.loads(s)
print(rebuil)
with open("jsonTest.json","w") as fw:
	json.dump(d,fw)
	print("写入完成")

with open("jsonTest.json","r") as fr:
	dr=json.load(fr)
	print(dr)
	print(dr["name"])

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
	def test():
		return "ok"
print()
s=Student("tom",23,90)
#序列化
d=json.dumps(s,default=lambda object:object.__dict__)
print(d)
#反序列化
red=json.loads(d,object_hook=lambda d:Student(d["name"],d["age"],d["score"]))
print(red)