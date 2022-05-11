import os
import datetime
import LMS_Classes
import objectCreation



# Removing a data file and creating a new version

def rewrite_members():
    """Removing members.txt and creating a new version"""
    try:
        os.remove("members.txt")
    except FileNotFoundError:
        pass
    new_file = open("members.txt", "w+")
    for value in objectCreation.member_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.get_name(), value.type, value.get_dob(), value.get_address(), value.get_location(), value.get_phone(), value.get_email(), value.get_branch())
        print(entry, file=new_file)
    new_file.close()
    with open("members.txt", "r") as temp_file:
        print(temp_file.read())


def rewrite_libraries():
    """Removing library.txt and creating a new version"""
    try:
        os.remove("library.txt")
    except FileNotFoundError:
        pass
    new_file = open("library.txt", "w+")
    for value in objectCreation.library_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.name, value.address, value.location, value.phone, value.email, value.website)
        print(entry, file=new_file)
    new_file.close()


def rewrite_items():
    """Removing items.txt and creating a new version"""
    try:
        os.remove("items_test.txt")
    except FileNotFoundError:
        pass
    new_file = open("items_test.txt", "w+")
    print("<NEW DATASET>", file=new_file)
    # Adding each instance of Book
    for value in objectCreation.book_obj_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.copies, value.title, value.genre, value.release_date, value.author, value.publisher)
        print(entry, file=new_file)
    print("<NEW DATASET>", file=new_file)
    # Adding each instance of Article
    for value in objectCreation.article_obj_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.copies, value.title, value.genre, value.release_date, value.author, value.journal)
        print(entry, file=new_file)
    print("<NEW DATASET>", file=new_file)
    # Adding each instance of Film
    for value in objectCreation.film_obj_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.copies, value.title, value.genre, value.release_date, value.studio, value.rt_score)
        print(entry, file=new_file)
    new_file.close()


def rewrite_borrowing():
    """Removing borrowing.txt and creating a new version"""
    try:
        os.remove("borrowing.txt")
    except FileNotFoundError:
        pass
    new_file = open("borrowing.txt", "w+")
    for value in objectCreation.borrow_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.member_id, value.m_name, value.item_id, value.i_name, value.start_date, value.return_date)
        print(entry, file=new_file)
    new_file.close()


# for ID generation

def id_generation(dictionary):
    """Generates a new id based on the highest existing id"""
    new_id = (max(dictionary.keys()) + 1)  # Finding the largest key in dictionary and adding one to it
    # print(id)
    return new_id

# Date generation

def date_generator():
    """Generates a today's date and a date +2weeks"""
    start_date = datetime.date.today()
    return_date = start_date + datetime.timedelta(days=14)
    return (start_date, return_date)

def copy_decrease(item_id):
    """Decreases available copies of an item"""
    if item_id in objectCreation.book_obj_dict.keys():
        objectCreation.book_obj_dict[item_id].copies = int(objectCreation.book_obj_dict[item_id].copies)-1
    if item_id in objectCreation.article_obj_dict.keys():
        objectCreation.article_obj_dict[item_id].copies = int(objectCreation.article_obj_dict[item_id].copies)-1
    if item_id in objectCreation.film_obj_dict.keys():
        objectCreation.film_obj_dict[item_id].copies = int(objectCreation.film_obj_dict[item_id].copies)-1
    rewrite_items()

def copy_increase(item_id):
        """Increases available copies of an item"""
        if item_id in objectCreation.book_obj_dict.keys():
            objectCreation.book_obj_dict[item_id].copies = int(objectCreation.book_obj_dict[item_id].copies)+1
        if item_id in objectCreation.article_obj_dict.keys():
            objectCreation.article_obj_dict[item_id].copies = int(objectCreation.article_obj_dict[item_id].copies)+1
        if item_id in objectCreation.film_obj_dict.keys():
            objectCreation.film_obj_dict[item_id].copies = int(objectCreation.film_obj_dict[item_id].copies)+1
        rewrite_items()


# -------Staff Menu ---------------------------------------------------------------------------------


# adding members

def add_member():
    """Adding an instance of the Member class based on user input, then updating the dictionary and .txt file"""
    print("Please enter the following details: ")
    # Getting user input for each attribute
    name = input("Name: ")
    m_type = input("Member Type (m or s): ")
    dob = input("DOB: ")
    address = input("Address: ")
    location = input("Location: ")
    phone = input("Phone no.: ")
    email = input("Email: ")
    # Generating a new ID
    new_id = id_generation(objectCreation.member_dict)
    # Creating a new member based on the above info
    new_member = LMS_Classes.Member(new_id, name, m_type, dob, address, location, phone, email)
    print("New Member is: ")
    print(new_member)
    # Adding new member to member_dict
    objectCreation.member_dict[new_member.id] = new_member
    # Rewriting members text file based on dictionary update
    rewrite_members()

# Remove member function


def remove_member():
    """Removing an instance of the Member class"""
    while True:
        try:
            # Requesting ID and Name of member to be removed
            print("Please enter the details of the member you would like to remove:")
            while True:
                try:
                    mid = int(input("Member ID: ")) # input loops until an int is entered. Int must be a key in member_dict
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for Member ID.")
            m_name = input("Member Full Name: ")
            if objectCreation.member_dict[mid].get_name().lower().strip() == m_name.lower(): # if the name and id entered, match a name and id in the dict, the program continues
                # Requesting confirmation before removal
                print("The Member you have selected is: ")
                print("#", objectCreation.member_dict[mid].id, objectCreation.member_dict[mid].get_name())
                confirmation = input("Press y to confirm. Press n to return to previous menu.\n")
                if confirmation == "y":
                    objectCreation.member_dict.pop(mid)
                    print(m_name, "has been removed.")
                    print("The remaining memebers are: ")
                    rewrite_members()
                    break
                else:
                    break
            else:
                raise ValueError
        except ValueError:
            print("We have no record of that member. Please check details and try again.\n")
        except KeyError:
            print("Invalid Member ID. Please try again.\n")

# Modifying a member

def modify_member():
    """Modifying user details"""
    while True:
        try:
            # Requesting ID and Name of member to be
            print("Please enter the following details for the member you wish to modify:\n")
            while True:
                try:
                    mid = int(input("Member ID: ")) # input loops until an int is entered. ID must be a key in member_dict
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for Member ID.")
            m_name = input("Member Full Name: ")
                        # if the name and id entered, match a name and id in the dict, the program continues
            if objectCreation.member_dict[mid].get_name().lower().strip() == m_name.lower():
                    user_input = input("Which value would you like to modify?\n "
                       "1. Name \n"
                       "2. Member Type \n "
                       "3. DOB \n"
                       "4. Address \n"
                       "5. Location \n"
                       "6. Phone \n"
                       "7. Email)?\n"
                       "8. Quit\n")
                    new_value = input("Please enter the updated value: ")
                    if user_input == "1":
                        objectCreation.member_dict[mid].set_name(new_value)
                        rewrite_members()
                        print("This member's name is now: ")
                        print(objectCreation.member_dict[mid].get_name())
                    elif user_input == "2":
                        if new_value.lower().strip() != "s" or new_value.lower().strip() != "m":
                            raise TypeError
                        else:
                            objectCreation.member_dict[mid].type = new_value
                            rewrite_members()
                            print("This member's type is now: ")
                            print(objectCreation.member_dict[mid].type)
                    elif user_input == "3":
                        objectCreation.member_dict[mid].set_dob(new_value)
                        rewrite_members()
                        print("This member's DOB is now: ")
                        print(objectCreation.member_dict[mid].get_dob())
                    elif user_input == "4":
                        objectCreation.member_dict[mid].set_address(new_value)
                        rewrite_members()
                        print("This member's address is now: ")
                        print(objectCreation.member_dict[mid].get_address())
                    elif user_input == "5":
                        objectCreation.member_dict[mid].set_location(new_value)
                        rewrite_members()
                        print("This member's location is now: ")
                        print(objectCreation.member_dict[mid].get_location())
                    elif user_input == "6":
                        objectCreation.member_dict[mid].set_phone(new_value)
                        rewrite_members()
                        print("This member's phone number is now: ")
                        print(objectCreation.member_dict[mid].get_phone())
                    elif user_input == "7":
                        objectCreation.member_dict[mid].set_email(new_value)
                        rewrite_members()
                        print("This member's email is now: ")
                        print(objectCreation.member_dict[mid].get_email())
                    elif user_input == "8":
                        print("Returning to previous menu\n")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                raise ValueError
        except ValueError:
            print("We have no record of that member. Please check details and try again.\n")
        except TypeError:
            print("Not a valid type. Please try again.")

def add_item():
    pass

def remove_item():
    pass

def add_library():
    pass

def remove_library():
    pass



# -------Member Menu ---------------------------------------------------------------------------------


# For browsing the catalogue


def browse_catalogue():
    """Displaying all of the items in the libraries"""
    print("The available books are: \n")
    for value in objectCreation.book_obj_dict.values():
        print(value, "\n")
    print("The available articles are: \n")
    for value in objectCreation.article_obj_dict.values():
        print(value, "\n")
    print("The available films are: \n")
    for value in objectCreation.film_obj_dict.values():
        print(value, "\n")


def borrow_item():
    """Borrow an item from the library catalogue"""
    print("Please enter the following details: \n")
    while True:
        try:
            while True:
                try:
                    # input loops until an int is entered.
                    mid = int(input("Your Member ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for Member ID.")
            while True:
                try:
                    iid = int(input("Item ID: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for Item ID.")
            # Requesting confirmation before continuing
            print("You are member: ")
            print("#", objectCreation.member_dict[mid].id, objectCreation.member_dict[mid].get_name())
            print("The item you have selected to borrow is: ")
            print("#", objectCreation.items_dict[iid].id, objectCreation.items_dict[iid].title)
            confirmation = input("Press y to confirm. Press n to return to previous menu.\n")

            if confirmation == "y":
                # Generating a new Borrow Transaction ID
                new_id = id_generation(objectCreation.borrow_dict)
                # Assigning member and item name variables
                m_name, i_name = objectCreation.member_dict[mid].get_name(), objectCreation.items_dict[iid].title
                # Generating dates
                dates = date_generator()
                start_date = dates[0]
                return_date = dates[1]
                # Creating a new borrow transaction based on the above info
                new_transaction = LMS_Classes.BorrowTransaction(new_id, mid, m_name, iid, i_name, start_date, return_date)
                objectCreation.borrow_dict[new_id] = new_transaction
                rewrite_borrowing()
                # Subtracting copies available of item
                copy_decrease(iid)
                # Transaction receipt
                print("Transaction details: ")
                print(new_transaction)
                break
            else:
                break
        except KeyError:
            print("Invalid ID. Please try again.\n")

def return_item():
    # Ask user for their member id and the item id

    # Check if they both appear in borrow_dict

    # Ask for confirmation

    # Remove from borrowing

    # Increase the copies count

    # print receipt


    pass

def join_library():
    pass

def cancel_membership():
    pass
