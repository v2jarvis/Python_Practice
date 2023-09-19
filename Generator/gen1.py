# this is first generator example
def simple():
    for x in range(10):
        yield x
save=simple()
for i in save:
    print(i)
