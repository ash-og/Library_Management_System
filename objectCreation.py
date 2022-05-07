import LMS_Classes

# For Item Class Object Creation -----------------------------------------------------------------------

def itemCreation(file):
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

def objectDict(list, objectClass):
    """Creating a dictionary of class objects from a list"""
    obj_dict = {}
    for item in list:
        obj_dict[item[1]] = objectClass(int(item[0]), item[1], item[2], item[3], item[4], item[5])
    return obj_dict

# For Library and Member Class Object Creation -----------------------------------------------------------------------

def objectCreation(file):
    """Creating a list of from our file"""
    input_file = open(file, "r")
    temp_list = input_file.readlines()
    input_file.close()
    object_list = []
    for item in temp_list:
        object_list.append(item.split("\t"))
    return object_list


# Main Scope

def main():
    # Library Catalogue:

    #Creating a list of each item
    item_list = itemCreation("items_test.txt")
    book_list = itemTypeSeperation(1, item_list)
    article_list = itemTypeSeperation(2, item_list)
    film_list = itemTypeSeperation(3, item_list)

    #Instantiating class objects based on those lists

    book_obj_dict = objectDict(book_list, LMS_Classes.Book)
    print(book_obj_dict)
    article_obj_dict = objectDict(article_list, LMS_Classes.Article)
    print(article_obj_dict)
    film_obj_dict = objectDict(film_list, LMS_Classes.Film)
    print(film_obj_dict)

    # Libraries:
    #Create a list of libraries:

    library_list = objectCreation("library.txt")
    print(library_list)








main()
