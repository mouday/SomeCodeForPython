def bi_search(lst,v):
    low=0
    high=len(lst)-1

    while low<=high:
        mid=(high+low)/2
        if lst[mid]<v:
            low=mid+1
        elif lst[mid]>v:
            high=mid-1
        else:
            return mid
    return -1

lis=[1,3,4,5,6,5]
print bi_search(lis,5)
sorted(lis)
print lis
            
        
