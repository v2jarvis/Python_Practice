#5.	Write a generator function unique_elements that yields only unique elements from a given iterable.

def smart_data(val):
    #s1={}
    s1=set()
    for i in val:
        #s1.update(i)
        #s1.add(i)
        #if i not in s1:
        s1.add(i)
    yield s1


val=[1,2,3,4,5,1,2,3,4,5,6]
res=iter(smart_data(val))

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
