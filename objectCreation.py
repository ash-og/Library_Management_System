import LMS_Classes

# For Item Class Object Creation -----------------------------------------------------------------------


def item_list_creation(file):
    """Creating a list of items from our items from a file"""
    input_file = open(file, "r")
    # splitting the file at <NEW DATASET>. This should give my a list with the three data sets as items.
    items_list = input_file.read().split("<NEW DATASET>")
    input_file.close()
    return items_list


def data_seperation(my_list):
    """Seperating the strings from item list into individual datasets"""
    data_list = []
    for item in my_list:
        data_list.append(item.split("\t"))
    return data_list


def item_type_seperation(i, items_list):
    """Creating a list of items based on item type"""
    temp_list = items_list[i].split("\n")
    # Removing first item as it doesn't contain data
    temp_list.pop(0)
    # Seperating each book into its own list of data
    item_type_list = data_seperation(temp_list)
    item_type_list.pop(-1)
    return item_type_list


def objectDict(my_list, objectClass):
    """Creating a dictionary of class objects from a list"""
    obj_dict = {}
    # print(my_list)
    temp_list = [objectClass(*args) for args in my_list]
    for item in temp_list:
        obj_dict[int(item.id)] = item
    return obj_dict

# For Library and Member Class Object Creation -----------------------------------------------------------------------


def list_creation(file):
    """Creating a list of from our file"""
    input_file = open(file, "r")
    temp_list = input_file.read().split("\n")
    input_file.close()
    object_list = data_seperation(temp_list)
    object_list.pop(-1)
    return object_list


# Main Scope

# Library Catalogue (Items):

# Creating a list of each item
item_list = item_list_creation("items_test.txt")
book_list = item_type_seperation(1, item_list)
article_list = item_type_seperation(2, item_list)
film_list = item_type_seperation(3, item_list)

# Instantiating class objects based on those lists
book_obj_dict = objectDict(book_list, LMS_Classes.Book)
article_obj_dict = objectDict(article_list, LMS_Classes.Article)
film_obj_dict = objectDict(film_list, LMS_Classes.Film)

# Creating a dictionary with all items

items_dict = {}
items_dict.update(book_obj_dict)
items_dict.update(article_obj_dict)
items_dict.update(film_obj_dict)

# Library and Members

# Create a list of libraries and members:
library_list = list_creation("library.txt")
member_list = list_creation("members.txt")

# Creating a dictionary of libraries and members:
library_dict = objectDict(library_list, LMS_Classes.Library)
member_dict = objectDict(member_list, LMS_Classes.Member)

# Creating a list and dictionary of borrow transactions:
borrow_list = list_creation("borrowing.txt")
borrow_dict = objectDict(borrow_list, LMS_Classes.BorrowTransaction)

# Adding in borrow history

for m in member_dict.values():
    for b in borrow_dict.values():
        if m.id == b.member_id:
            m.update_borrow_list(b)


# Testing the above code
# tests.object_creation_tests(item_list, book_list, article_list, book_obj_dict, article_obj_dict, film_obj_dict, items_dict, library_list, member_list, library_dict, member_dict, borrow_list, borrow_dict)
