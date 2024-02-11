#4.	Create a generator function file_reader that reads a file line by line and yields each line.

def file(val):
    f1=open(val, 'r')
    for i in f1:
        yield i.strip()

val='abc.txt'

read=iter(file(val))
print(next(read))
print(next(read))
print(next(read))
