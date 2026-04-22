class Book :
    title = "The Book"
    auther = "Fahad Hussain"
    pages = 300


    def __init__(self,title,auther,pages):
        self.title = title
        self.auther = auther
        self.pages = pages

    def Describe(self):
        print( self.title," | " ,self.auther," | ",self.pages,"pages")


Person1 = Book("Python Basics", "Fahad Hussain", 300)
Person2 = Book("Python Advanced", "Ahmed", 400)
Person1.Describe()
Person2.Describe()