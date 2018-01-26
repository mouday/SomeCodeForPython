import json
import pickle

data={"k1":123,"k2":"abc"}
print('data', type(data), data)
# data <class 'dict'> {'k2': 'abc', 'k1': 123}

# json
string=json.dumps(data) #序列化
print('string',type(string), string) 
# string <class 'str'> {"k2": "abc", "k1": 123}

restring=json.loads(string) #反序列化
print('restring',type(restring) , restring)
# restring <class 'dict'> {'k1': 123, 'k2': 'abc'}

json.dump(data,open("text.json","w"))# 序列化到文件

d=json.load(open("text.json"))  #从文件反序化出来
print("d",d)
# d {'k1': 123, 'k2': 'abc'}

# pickle
p=pickle.dumps(data) #序列化
print(p)
# b'\x80\x03}q\x00(X\x02\x00\x00\x00k1q\x01K{X\x02\x00\x00\x00k2q\x02X\x03\x00\x00\x00abcq\x03u.'

rep=pickle.loads(p) #反序列化
print(rep)
# {'k1': 123, 'k2': 'abc'}
