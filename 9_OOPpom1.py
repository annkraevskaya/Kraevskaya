
  class LibraryBook:           #создание класса (шаблон)
    _LIBRARY_NAME ="Central City Library"    #инициализация общего атрибута

    def __init__(self, title,author):     #создание констурктора
        self.title = title
        self.author = author

    def info(self):        #создание метода info для взаимодействия
        return f"{self.title} by {self.author} - kept in {self._LIBRARY_NAME}"

book=LibraryBook("The Green Mile", "Stephen King")    #создание новой книги
print(book.info())

LibraryBook._LIBRARY_NAME="Downtown Branch"    #замена общего атрибута
print(book.info())