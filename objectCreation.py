import LMS_Classes

# For Item Class Object Creation -----------------------------------------------------------------------

def itemListCreation(file):
    """Creating a list of items from our items from a file"""
    input_file = open(file, "r")
    #splitting the file at <NEW DATASET>. This should give my a list with the three data sets as items.
    items_list = input_file.read().split("<NEW DATASET>")
    input_file.close()
    return items_list

def dataSeperation(list):
    """Seperating the strings from item list into individual datasets"""
    data_list = []
    for item in list:
        data_list.append(item.split("\t"))
    return data_list

def itemTypeSeperation(i, items_list):
    """Creating a list of items based on item type"""
    temp_list = items_list[i].split("\n")
    # Removing first item as it doesn't contain data
    temp_list.pop(0)
    # Seperating each book into its own list of data
    item_type_list = dataSeperation(temp_list)
    item_type_list.pop(-1)
    return item_type_list

# def itemObjectDict(list, objectClass):
#     """Creating a dictionary of class objects from a list"""
#     obj_dict = {}
#     for item in list:
#         obj_dict[int(item[0])] = objectClass(int(item[0]), item[1], item[2], item[3], item[4], item[5])
#     return obj_dict

def objectDict(list, objectClass):
    """Creating a dictionary of class objects from a list"""
    obj_dict = {}
    # print(list)
    temp_list = [objectClass(*args) for args in list]
    for item in temp_list:
        obj_dict[item.id] = item
    return obj_dict

# For Library and Member Class Object Creation -----------------------------------------------------------------------

def listCreation(file):
    """Creating a list of from our file"""
    input_file = open(file, "r")
    temp_list = input_file.read().split("\n")
    input_file.close()
    object_list = dataSeperation(temp_list)
    object_list.pop(-1)
    return object_list

# def libObjectDict(list, objectClass):
#     """Creating a dictionary of class objects from a list"""
#     obj_dict = {}
#     for item in list:
#         obj_dict[int(item[0])] = objectClass(int(item[0]), item[1], item[2], item[3], item[4], item[5])
#     return obj_dict



# Main Scope

# Library Catalogue:

# Creating a list of each item
item_list = itemListCreation("items_test.txt")
# print(item_list)
book_list = itemTypeSeperation(1, item_list)
# print(book_list)
article_list = itemTypeSeperation(2, item_list)
# print(article_list)
film_list = itemTypeSeperation(3, item_list)

# Instantiating class objects based on those lists
book_obj_dict = objectDict(book_list, LMS_Classes.Book)
# print(book_obj_dict)
# for value in book_obj_dict.values():
#     print(value)

article_obj_dict = objectDict(article_list, LMS_Classes.Article)
# print(article_obj_dict)
# for value in article_obj_dict.values():
#     print(value)

film_obj_dict = objectDict(film_list, LMS_Classes.Film)
# print(film_obj_dict)
# for value in film_obj_dict.values():
#     print(value)

# Library and Members

# Create a list of libraries and members:
library_list = listCreation("library.txt")
# print(library_list)
member_list = listCreation("members.txt")
# print(member_list)

# Creating a dictionary of libraries and members:
library_dict = objectDict(library_list, LMS_Classes.Library)
# print(library_dict)
# for value in library_dict.values():
#     print(value)
member_dict = objectDict(member_list, LMS_Classes.Member)
# print(member_dict)
# for value in member_dict.values():
#     print(value)
