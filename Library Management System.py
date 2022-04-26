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



# Main Scope


Library1 = Library(name="Carlow Library", location="Tullow Street, Carlow", phone="0505-12345", email="info@carlowlibrary.ie")
print(Library1)

Member1 = Member(name="Aisling Young", m_type="Adult", branch="Carlow Library")
print(Member1)

Item1 = Item("Harry Potter", "A tale from the Harry Potter wizarding world", "Children's Fiction", "Dec 2001")
print(Item1)
