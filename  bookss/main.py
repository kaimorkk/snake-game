class Book:
    language='Eng'
    is_book=True
    book_1=Book()
    book_2=Book()
    book_1, author='Dan Brown'
    book_1, title='inferno'
    book_2, author='Dan Brown'
    book_2, title='The van Da code'
    book_2, year_of_publish=2002
    books=[book_1,book_2]
    for books in books:
     for attr in books.__dict__:
print(f'{attr)-->(getattr,(Book,attr)}')