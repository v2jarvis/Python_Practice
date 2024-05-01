class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author


# Create a Book object
book = Book("Python Programming", "John Doe")
# Try to change the title
book.__title = "New Title"
# Print the title and author
print(book.__title())
print(book.get_author())