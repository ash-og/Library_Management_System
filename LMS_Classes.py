# Defining Classes

class Library(object):
    """Library class"""
    def __init__(self, lid: int, name="", address="", location="", phone="", email="", website=""):
        self.ID = lid
        self.name = name
        self.location = location
        self.address = address
        self.phone = phone
        self.email = email
        self.website = website


    def __str__(self):
        return "{} is located in {}.\nYou can contact them via {} or {}"\
            .format(self.name, self.location, self.phone, self.email)


class Member(object):
    """Library Members class"""

    def __init__(self, mid: int, name="", m_type="", dob="", address="", location="", phone="", email="", branch="", history=None):
        self.ID = mid
        self.name = name
        self.type = m_type
        self.DOB = dob
        self.address = address
        self.location = location
        self.phone = phone
        self.email = email
        self.closest_branch = branch
        self.borrow_history = history

    def __str__(self):
        return "{} is a {} member. Their closest branch is {}.".format(self.name, self.type, self.closest_branch)


class Item(object):
    """Items class to hold items available to borrow from Libraries"""

    def __init__(self, id: int, title="", genre="", date=""):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_date = date

    def __str__(self):
        return "{} is from the {} genre. It was released {}.".format(self.title, self.genre, self.release_date)

class Book(Item):
    """Book is a subclass of Item"""

    def __init__(self, id: int, title="", genre="", date="", author="", publisher=""):

        Item.__init__(self, id, title, genre, date) #Check this - should it be release_date?
        self.author = author
        self.publisher = publisher

    def __str__(self):
        result = "{} is a {} book by {}\n".format(self.title, self.genre, self.author)
        result += "It was released " + self.release_date
        return result

class Article(Item):
    """Journal articles as a subclass of Item"""

    def __init__(self, id: int, title="", genre="", date="", author="", journal=""):
        Item.__init__(self, id, title, genre, date)
        self.author = author
        self.journal = journal

    def __str__(self):
        result = "\""+ self.title + "\"" + " is an article by " + self.author + ".\n"
        return result


class Film(Item):
    """Digital Media as a subclass of item"""
    def __init__(self, id: int, title="", genre="", date="", studio="", rt_score=""):
        Item.__init__(self, id, title, genre, date)
        self.studio = studio
        self.rt_score = rt_score

    def __str__(self):
        result = self.title + " is a " + self.genre + " movie \n"
        result += "It has a Rotten Tomatoes score of " + self.rt_score
        return result


# Main Scope


