class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def display(self):
        print(f'{self.title} written by {self.author} is published by {self.publisher}')
       
r1 = Book('Nercotics','ajay')
r1.publisher = "aleena"
r1.display()