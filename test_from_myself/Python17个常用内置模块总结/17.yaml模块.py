import yaml
#需要安装yaml库
"""
person1:
    name:Tom
    age:29
    sex:man
person2:
    name:Jack
    age:20
    sex:women
"""
#
f=open("test.yaml","r")   #读取文件
x=yaml.load(f)  #导入
print(x)
f.close()

#写入
d={
    'person2': 
        {
        'name':'Jack',
        'age':20, 
        'sex':'women'
        }, 
    'person1': 
        {
        'name':'Tom',
        'age':29
        }
    }

f=open("newtest.yaml","w")
yaml.dump(d, f, default_flow_style=False)
f.close() 

"""
person1:
  age: 29
  name: Tom
person2:
  age: 20
  name: Jack
  sex: women
"""