import collections
index=collections.defaultdict(list)
print(index)
for item in range(10):
    key=item %2
    index[key].append(item)

print(index)
print(index[6])
