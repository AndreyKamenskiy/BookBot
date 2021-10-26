class Lybrary:
    """Labrary class"""
 
    def __init__(self):
        """init"""
        # Attributes
        self.books = []

    def GetChapterById(self, id):
        return Chapter(self.chapterts[id]) # вернем копию главы, чтобы книгу не портить. Потом можно исправить.

class Book:
    """Book class"""
 
    def __init__(self):
        """init"""
        # Attributes
        self.title = ""
        self.description = ""
        self.chapters = {}

    def GetChapterById(self, id):
        return self.chapters[id] # исправить
    
    def TestBook(self):
        """checking that links in every element of the chapter is valid"""
        pass


class Chapter:
    """Chapter class"""
 
    def __init__(self):
        """init"""
        # Attributes
        self.id = ""
        self.elements = []

class Element:
    """The Element class. It represent part of the chapter. 
    In the future, it may be a text, a pointer to the next chapter, some action, a picture, and so on."""
    def __init__(self, text = "", nextChapterId = ""):
        """The elemen class"""
        # Attributes
        self.text = text
        self.next = nextChapterId


