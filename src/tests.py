import library as lib


def make_simple_book():
    """https://drive.google.com/file/d/1IBThWDXxGgTHR869KEUjgeLzXxhsSsxh/view?usp=sharing - map"""
    book = lib.Book()
    book.title = "Простая книга для тестирования."
    book.description = "Самая простая книга. никаких активностей, только переход по ссылкам"

    ch = lib.Chapter()
    ch.id = "start"
    ch.elements = [lib.Element("глава1.Это Текст стартовой главы.Дальше пойдет выбор"),
                 lib.Element("Первый вариант выбора. ведет на главу 2", "2"),
                 lib.Element("Второй вариант выбора. ведет на главу 5", "5"),
                 lib.Element("Второй вариант выбора. ведет к смерти", "lose")
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "2"
    ch.elements = [lib.Element("глава2.Это Текст второй.Дальше пойдет выбор"),
                 lib.Element("Первый вариант выбора. ведет на главу 4", "4"),
                 lib.Element("Второй вариант выбора. ведет на главу 3", "3"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "3"
    ch.elements = [lib.Element("глава3.Это первая часть главы."),
                 lib.Element("Выбор в середине главы. Ведет к смерти ", "lose2"),
                 lib.Element("Это вторая часть главы 3. "),
                 lib.Element("выбор в конце главы. Ведет к победе ", "win"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "4"
    ch.elements = [lib.Element("глава4.Это глава 4. Она простая"),
                 lib.Element("Выбор главы 4. Ведет к смерти ", "lose"),
                 lib.Element("выбор в конце главы 4. Ведет к победе главе 5", "5"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "5"
    ch.elements = [lib.Element("глава5. Она ведет в начало и к главе 3. Она простая"),
                 lib.Element("Вернемся к началу?", "start"),
                 lib.Element("Перейдем к главе 3", "3"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "lose"
    ch.elements = [lib.Element("You lose. Это тупик, детка. Остается только начать все сначала."),
                 lib.Element("☠"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "lose2"
    ch.elements = [lib.Element("You lose2. Ты был так близок к финалу. К успеху шел, не подфартило, не свезло"),
                 lib.Element("☠"),
    ]
    book.chapters[ch.id] = ch

    ch = lib.Chapter()
    ch.id = "win"
    ch.elements = [lib.Element("Win. Ты победил! Крутышь! "),
                 lib.Element("✌"),
    ]
    book.chapters[ch.id] = ch

    return book
