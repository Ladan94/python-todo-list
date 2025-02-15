class Book:
    def __init__(self, title, writer, year, price):
        if year <= 0:
            raise ValueError("Year cannot be zero or less")  
        self.title = title
        self.writer = writer
        self.year = year
        self.price = price
        self.sales = 0  

    def sell(self, copies):
        if copies < 0:
            print("Invalid number of copies!")
            return
        self.sales += copies
        print(f"{copies} copies of '{self.title}' sold!")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.writer}, Year: {self.year}")
        print(f"Sold Copies: {self.sales}, Total Revenue: €{self.sales * self.price}")

if __name__ == "__main__":
    my_book = Book("The Magic Adventure", "Your Name", 2024, 10)
    my_book.sell(3)
    my_book.display_info()