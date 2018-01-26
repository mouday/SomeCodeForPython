import checkcode

print(dir(checkcode))
print(help(checkcode))
print(help(checkcode.getCheckCode))
print(checkcode.getCheckCode.__doc__)

lst=checkcode.getCheckCodeByNum(50)
with open("随机码.txt","w") as f:
    f.write("\n".join(lst))
