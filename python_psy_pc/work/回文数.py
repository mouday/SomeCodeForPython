num = 123321
num_p = 0
num_t = num

while num !=0:
    num_p = num_p * 10 + num % 10
    num = num / 10
    
print num,num_p,num_t
if num_t == num_p:
    print "ok"
else:
    print "no"
