# Object Creation
def object_creation_tests(item_list, book_list, article_list, book_obj_dict, article_obj_dict, film_obj_dict, items_dict, library_list, member_list, library_dict, member_dict, borrow_list, borrow_dict):
    print(item_list)

    print(book_list)

    print(article_list)

    print(book_obj_dict)
    for value in book_obj_dict.values():
        print(value)

    print(article_obj_dict)
    for value in article_obj_dict.values():
        print(value)

    print(film_obj_dict)
    for value in film_obj_dict.values():
        print(value)

    print(items_dict)

    print(library_list)

    print(member_list)

    print(library_dict)
    for value in library_dict.values():
        print(value)

    print(member_dict)
    for value in member_dict.values():
        print(value)

    print(borrow_list)

    print(borrow_dict)
    for value in borrow_dict.values():
        print(value)

# Menu Functions

def menu_functions_test():
    """Tests for menuFunctions module"""

    # rewrite functions
    # rewrite_members() test
    with open("members.txt", "r") as temp_file:
        print(temp_file.read())
    rewrite_members()
    with open("members.txt", "r") as temp_file:
        print(temp_file.read())
    # rewrite_libraries() test
    with open("library.txt", "r") as temp_file:
        print(temp_file.read())
    rewrite_libraries()
    with open("library.txt", "r") as temp_file:
        print(temp_file.read())
    # rewrite_items() test
    with open("items_test.txt", "r") as temp_file:
        print(temp_file.read())
    rewrite_items()
    with open("items_test.txt", "r") as temp_file:
        print(temp_file.read())

    # rewrite_borrowing() test
    with open("borrowing.txt", "r") as temp_file:
        print(temp_file.read())
    rewrite_borrowing()
    with open("borrowing.txt", "r") as temp_file:
        print(temp_file.read())

    # copy_decrease test
    print(objectCreation.book_obj_dict[1].copies)
    copy_decrease(1)
    print(objectCreation.book_obj_dict[1].copies)

    # copy_increase test
    print(objectCreation.book_obj_dict[1].copies)
    copy_increase(1)
    print(objectCreation.book_obj_dict[1].copies)

    # borrow() function test
    print(new_transaction)
    print(objectCreation.borrow_dict[new_id])
