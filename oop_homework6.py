class LibraryItem:
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year


    def __str__(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"



class Book:
    def __init__(self, number_of_pages: int):
        self.number_of_pages = number_of_pages

    def info_of_pages(self):
        return my_book.__str__() + f', Number_of_pages: {self.number_of_pages}'


class Magazine:
    def __init__(self, issue_number: int):
        self.issue_number = issue_number


    def info_of_issue_number(self):
        return my_book.__str__() + f', Issue_number: {self.issue_number}'


class DVD:
    def __init__(self, duration: int):
        self.duration = duration


    def info_of_duration(self):
        return my_book.__str__() + f', Duration: {self.duration}'



my_book = LibraryItem(title='hh', author_or_director='tti', year=2007)
ii = Book(number_of_pages=90)
print(ii.info_of_pages())
yy = Magazine(issue_number=56)
print(yy.info_of_issue_number())
uu = DVD(duration=9)
print(uu.info_of_duration())
