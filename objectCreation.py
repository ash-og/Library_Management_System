import LMS_Classes


def itemCreation(file):
    """Creating a list of items from our items.txt"""
    input_file = open(file, "r")
    #splitting the file at <NEW DATASET>. This should give my a list with the three data sets as items.
    items_list = input_file.read().split("<NEW DATASET>")
    return items_list

def dataSeperation(list):
    """Seperating the strings from item list into individual datasets"""
    data_list = []
    for item in list:
        data_list.append(item.split("\t"))
    return data_list

def booksCreation(items_list):
    """Creating a list of books"""
    temp_list = items_list[1].split("\n")
    # Removing first item as it doesn't contain data
    temp_list.pop(0)
    # Seperating each book into its own list of data
    book_list = dataSeperation(temp_list)
    book_list.pop(-1)
    return book_list

def articlesCreation(items_list):
    """Creating a list of articles"""
    temp_list = items_list[2].split("\n")
    # Removing first item as it doesn't contain data
    temp_list.pop(0)
    # Seperating each article into its own list of data
    article_list = dataSeperation(temp_list)
    article_list.pop(-1)
    return article_list

def filmsCreation(items_list):
    """Creating a list of films"""
    temp_list = items_list[3].split("\n")
    # Removing first item as it doesn't contain data
    temp_list.pop(0)
    # Seperating each film into its own list of data
    film_list = dataSeperation(temp_list)
    film_list.pop(-1)
    return film_list

def objectDict(list):
    """Creating a dictionary of class objects from a list"""
    obj_dict = {}
    for item in list:
        obj_dict[item[1]] = LMS_Classes.Article(int(item[0]), item[1], item[2], item[3], item[4], item[5])
    return obj_dict


# Main Scope

def main():
    #Creating a list of each item
    item_list = itemCreation("items_test.txt")
    book_list = booksCreation(item_list)
    article_list = articlesCreation(item_list)
    film_list = filmsCreation(item_list)
    #Instantiating class objects based on those lists
    book_obj_dict = objectDict(book_list)
    print(book_obj_dict)
    article_obj_dict = objectDict(article_list)
    print(article_obj_dict)
    film_obj_dict = objectDict(film_list)
    print(film_obj_dict)








main()
