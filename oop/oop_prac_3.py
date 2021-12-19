class Book():

    def __init__(self, name, author, pages):

        self.name = name
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"{self.name} by the {self.author}"

    def __len__(self):
        print(int(self.pages))

    def __del__(self):
        print("A book object has been deleted from the memory.")


mybook = Book('sign of times', 'Harry Styles', 10)

print(mybook)
len(mybook)
del mybook
