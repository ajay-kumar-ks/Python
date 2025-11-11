class Publisher :
    def __init__(self,name):
        self.name = name
    def display(self):
        print('Name => ',self.name)
        
class Book(Publisher):
    def __init__(self, name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print('title => ',self.title)
        print('author => ',self.author)
        
class Python(Book):
    def __init__(self, name, title, author,price,no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
        
    def display(self):
        super().display()
        print('price => ',self.price)
        print('no_of_pages => ',self.no_of_pages)
        
r1 = Python('Nercotics','dirtyBusiness','ajay',1000,200)
r1.display()
