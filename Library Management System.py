# Defining Classes

class Library(object):
    """Library class"""
    def __init__(self, libID=0, name="", location="", phone="", email="", website=""):
        self.libID = libID
        self.name = name
        self.location = location
        self.phone = phone
        self.email = email
        self.website = website


    def __str__(self):
        return "{} is located at {}.\nYou can contact them via {} or {}"\
            .format(self.name, self.location, self.phone, self.email)






# Main Scope

Library1 = Library(name="Carlow Library", location="Tullow Street, Carlow", phone="0505-12345", email="info@carlowlibrary.ie")
print(Library1)


