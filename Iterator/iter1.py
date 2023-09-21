# this is first iterator example
def simple():
    for i in range(10):
        yield i,i,i,i,i,i
save=simple()
first=iter(save)
print(next(first))
print(next(first))
print(next(first))
