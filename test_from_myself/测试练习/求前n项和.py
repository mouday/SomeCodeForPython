sum = 0
x = 2
n = 0
while True:
    sum=sum+x**n
    n+=1
    if n>=20:
        break
print (sum)

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print (key+":"+str(d[key])