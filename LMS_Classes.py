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

    def __init__(self, mid: int, name="", m_type="", dob="", address="", location="", phone="", email="", branch="", history=""):
        self.ID = mid
        self.__name = name
        self.type = m_type
        self.__DOB = dob
        self.__address = address
        self.__location = location
        self.__phone = phone
        self.__email = email
        self.__closest_branch = branch
        self.__borrow_history = history

    def __str__(self):
        return "{} is a {} member. Their closest branch is {}.".format(self.name, self.type, self.closest_branch)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__DOB

    def set_dob(self, dob):
        self.__DOB = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_branch(self):
        return self.__closest_branch

    def set_branch(self, branch):
        self.__closest_branch = branch

    def get_history(self):
        return self.__borrow_history

    def set_history(self, history):
        self.__borrow_history = history


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
        result = "{} \t-\t {} \t-\t {}\n".format(self.id, self.title, self.author)
        return result

class Article(Item):
    """Journal articles as a subclass of Item"""

    def __init__(self, id: int, title="", genre="", date="", author="", journal=""):
        Item.__init__(self, id, title, genre, date)
        self.author = author
        self.journal = journal

    def __str__(self):
        result = "{} \t-\t {} \t-\t {}\n".format(self.id, self.title, self.author)
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

class BorrowTransaction(object):
    """Borrowed lists the borrowing transactions, storing the member, book and time associated with each transaction"""
    def __init__(self, id: int, member: Member, item, start_date, return_date):
            self.id = id
            self.member = member
            self.item = item
            self.start_date = start_date
            self.return_date = return_date

    def __str__(self):
        result = self.member + "borrowed " + self.item.title
        return result

# class Location(object):
#     """Locations for members or libraries"""
#     def __init__(self, street, town, city, county, eircode):
#         self.street = street
#         self.town = town
#         self.city = city
#         self.county = county
#         self.eircode = eircode





# Main Scope


