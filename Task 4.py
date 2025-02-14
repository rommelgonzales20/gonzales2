class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"'{self.title}' by {self.author}, published in {self.year_published}.")

# Creating three book objects
book1 = Book("History of the Baptists (Hardcover)", " Robert G. Torbet", 1973)
book2 = Book("An Orthodox Catechism", " Hercules Collins ", 1680)
book3 = Book("Baptists in America: A History (Hardcover)", " Thomas S. Kidd ", 2015)

# Displaying their details
book1.describe()
book2.describe()
book3.describe()

