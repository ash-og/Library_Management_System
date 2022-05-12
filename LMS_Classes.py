import datetime


# Defining Classes

class Library(object):
    """Library class"""
    def __init__(self, lid: int, name="", address="", location="", phone="", email="", website=""):
        self.id = lid
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

    def __init__(self, mid, name="", m_type="", dob="", address="", location="", phone="", email=""):
        self.id = mid
        self.__name = name
        self.type = m_type
        self.__DOB = dob
        self.__address = address
        self.__location = location
        self.__phone = phone
        self.__email = email
        self.__borrow_history = []

    def __str__(self):
        return "Member ID #{} is called {}, and is an {} member.".format(self.id, self.__name, self.type)

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

    def get_history(self):
        return self.__borrow_history

    def set_history(self, history):
        self.__borrow_history = history

    def update_borrow_history(self, item):
        self.__borrow_history.append(item)


class Item(object):
    """Items class to hold items available to borrow from Libraries"""

    def __init__(self, id, copies, title: str, genre="", date=""):
        self.id = id
        self.copies = copies
        self.title = title
        self.genre = genre
        self.release_date = date

    def __str__(self):
        return "{} is from the {} genre. It was released {}.".format(self.title, self.genre, self.release_date)

class Book(Item):
    """Book is a subclass of Item"""

    def __init__(self, id, copies, title: str, genre="", date="", author="", publisher=""):

        Item.__init__(self, id, copies, title, genre, date)
        self.author = author
        self.publisher = publisher
        self.copies = copies


    def __str__(self):
        result = "ID#: \t" + str(self.id) + "\n"
        result += "Title:\t" + self.title + "\n"
        result += "Author: \t" + self.author + "\n"
        result += "Available Copies: \t" + str(self.copies) + "\n"
        return result

class Article(Item):
    """Journal articles as a subclass of Item"""

    def __init__(self, id, copies, title: str, genre="", date="", author="", journal=""):
        Item.__init__(self, id, copies, title, genre, date)
        self.author = author
        self.journal = journal
        self.copies = copies

    def __str__(self):
        result = "ID#: \t" + str(self.id) + "\n"
        result += "Title:\t" + self.title + "\n"
        result += "Author: \t" + self.author + "\n"
        result += "Available Copies: \t" + str(self.copies)
        return result


class Film(Item):
    """Digital Media as a subclass of item"""
    def __init__(self, id, copies, title: str, genre="", date="", studio="", rt_score=""):
        Item.__init__(self, id, copies, title, genre, date)
        self.studio = studio
        self.rt_score = rt_score
        self.copies = copies

    def __str__(self):
        result = "ID#: \t" + str(self.id) + "\n"
        result += "Title:\t" + self.title + "\n"
        result += "Rotten Tomatoes Score: \t" + self.rt_score + "\n"
        result += "Available Copies: \t" + str(self.copies)
        return result

class BorrowTransaction(object):
    """Borrowed lists the borrowing transactions, storing the member, book and time associated with each transaction"""
    def __init__(self, id: int, member_id: str, m_name: str, item_id: str, i_name: str, start_date: str, return_date: str):
            self.id = id
            self.member_id = member_id
            self.m_name = m_name
            self.item_id = item_id
            self.i_name = i_name
            self.start_date = start_date
            self.return_date = return_date

    def __str__(self):
        result = "Transaction ID: \t" + str(self.id) + "\n"
        result += "Member: \t" + self.m_name + "\n"
        result += "Item: \t" + self.i_name + "\n"
        result += "Borrow Date: \t" + self.start_date + "\n"
        result += "Return Date: \t" + self.return_date + "\n"
        return result

    def my_borrowed(self):
        items_borrowed = "Transaction ID: \t" + str(self.id) + "\n"
        items_borrowed += "Item: \t" + self.i_name + "\n"
        return items_borrowed

# class Location(object):
#     """Locations for members or libraries"""
#     def __init__(self, street, town, city, county, eircode):
#         self.street = street
#         self.town = town
#         self.city = city
#         self.county = county
#         self.eircode = eircode





# Main Scope


