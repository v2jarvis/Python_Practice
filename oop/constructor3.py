#this is a simple example of constructor
class test:
    def __init__(self,title):
        self.title=title
    def book(self):
        print("This is the title of",self.title)
obj=test('python crash course')
obj.book()