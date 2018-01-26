
# https://docs.python.org/3.5/library/collections.html#collections.Counter
from collections import Counter

# a new, empty counter
c=Counter()
print(c)

# a new counter from an iterable
c=Counter("aaabbbcccdddeeeeeffffff")
print(c)
print("c['a']=",c["a"])

# a new counter from a mapping
c=Counter({'red':1,'green':2,'yellow':3})
print(c)

# a new counter from keyword args
c=Counter(a=1,b=4,c=6)
print(c)

c=Counter([1,2,3,4,5,6,7,8,9,1,0,0,0])
print(c)
print(c[10])# count of a missing element is zero

# counter entry with a zero count
c[0]=0
print(c)

# del actually removes the entry
del c[0]
print(c)

print(c.most_common(3))
