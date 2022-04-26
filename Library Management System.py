# Defining Classes

class Library(object):
    """Library class"""
    def __init__(self, libid=0, name="", location="", phone="", email="", website=""):
        self.libID = libid
        self.name = name
        self.location = location
        self.phone = phone
        self.email = email
        self.website = website

    def __str__(self):
        return "{} is located at {}.\nYou can contact them via {} or {}"\
            .format(self.name, self.location, self.phone, self.email)


class Member(object):
    """Library Members class"""

    def __init__(self, m_id=0, name="", m_type="", dob="", address="", phone="", email="", branch="",
                 history=None):
        self.ID = m_id
        self.name = name
        self.type = m_type
        self.DOB = dob
        self.address = address
        self.phone = phone
        self.email = email
        self.closest_branch = branch
        self.borrow_history = history

    def __str__(self):
        return "{} is a {} member. Their closest branch is {}.".format(self.name, self.type, self.closest_branch)


class Item(object):
    """Items class to hold items available to borrow from Libraries"""

    def __init__(self, title="", description="", genre="", date="", language="", awards="", notes=""):
        self.title = title
        self.description = description
        self.genre = genre
        self.release_date = date
        self.language = language
        self.awards = awards
        self.notes = notes

    def __str__(self):
        return "{} is from the {} genre. It was released {}.".format(self.title, self.genre, self.release_date)

class Book(Item):
    """Book is a subclass of Item"""

    def __init__(self, title="", description="", genre="", date="", language="", awards="", notes="", isbn="", author="", publisher=""):

        Item.__init__(self, title, description, genre, date, language, awards, notes)
        self.ISBN = isbn
        self.author = author
        self.publisher = publisher

    def __str__(self):
        result = "{} is a {} book by {}\n".format(self.title, self.genre, self.author)
        result += "It is " + self.description + "\n"
        result += "It was released " + self.release_date
        return result

class Article(Item):
    """Journal articles as a subclass of Item"""

    def __init__(self, title="", description="", genre="", date="", language="", awards="", notes="", author="", abstract="", issn=""):
        Item.__init__(self, title, description, genre, date, language, awards, notes)
        self.author = author
        self.abstract = abstract
        self.ISSN = issn

    def __str__(self):
        result = "\""+ self.title + "\"" + " is an article by " + self.author + ".\n"
        return result


class Digital(Item):
    """Digital Media as a subclass of item"""
    def __init__(self, title="", description="", genre="", date="", language="", awards="", notes="", media_type="", performers=""):
        Item.__init__(self, title, description, genre, date, language, awards, notes)
        self.media_type = media_type
        self.performers = performers

    def __str__(self):
        result = self.title + " is a " + self.media_type + "\n"
        result += "It is " + self.description
        return result


# Main Scope


Library1 = Library(name="Carlow Library", location="Tullow Street, Carlow", phone="0505-12345", email="info@carlowlibrary.ie")
print(Library1)

print("\n")

Member1 = Member(name="Aisling Young", m_type="Adult", branch="Carlow Library")
print(Member1)

print("\n")

Item1 = Item("Harry Potter", "A tale from the Harry Potter wizarding world", "Children's Fiction", "Dec 2001")
print(Item1)

print("\n")

Book1 = Book("Consolations", "David Whyte's third volume of poetry", "Poetry", "Dec 2020", author="David Whyte")
print(Book1)

print("\n")

Article1 = Article("Study of Multicore processors: Advantages and Challenges", author="Vinayak Shinde")
print(Article1)

Digital1 = Digital("Pulp Fiction", "Quentin Tarantino's Masterpiece", "Action", "March 1992", "English", media_type="Movie", performers="Samuel L Jackson, Uma Thurman")
print(Digital1)
