import LMS_Classes
import objectCreation
import os


# Removing a data file and creating a new version

def rewrite_members():
    """Removing members.txt and creating a new version"""
    try:
        os.remove("members.txt")
    except FileNotFoundError:
        pass
    new_file = open("members.txt", "w+")
    for value in objectCreation.member_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.ID, value.get_name(), value.type, value.get_dob(), value.get_address(), value.get_location(), value.get_phone(), value.get_email(), value.get_branch())
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
    with open("library.txt", "r") as temp_file:
        print(temp_file.read())


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
        entry = "{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.title, value.genre, value.release_date, value.author, value.publisher)
        print(entry, file=new_file)
    print("<NEW DATASET>", file=new_file)
    # Adding each instance of Article
    for value in objectCreation.article_obj_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.title, value.genre, value.release_date, value.author, value.journal)
        print(entry, file=new_file)
    print("<NEW DATASET>", file=new_file)
    # Adding each instance of Film
    for value in objectCreation.film_obj_dict.values():
        entry = "{}\t{}\t{}\t{}\t{}\t{}".format(value.id, value.title, value.genre, value.release_date, value.studio, value.rt_score)
        print(entry, file=new_file)
    new_file.close()
    with open("items_test.txt", "r") as temp_file:
        print(temp_file.read())


# for ID generation


def id_generation(dictionary):
    new_id = (max(dictionary.keys()) + 1)  # Finding the largest key in dictionary and adding one to it
    # print(id)
    return new_id


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
    objectCreation.member_dict[new_member.ID] = new_member
    # Rewriting members text file based on dictionary update
    rewrite_members()


# print(add_member())

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
                print("#", objectCreation.member_dict[mid].ID, objectCreation.member_dict[mid].get_name())
                confirmation = input("Press y to confirm")
                if confirmation == "y":
                    pass
                    break
                else:
                    break
            else:
                raise ValueError
        except ValueError:
            print("We have no record of that member. Please check details and try again.\n")
        except KeyError:
            print("Invalid Member ID. Please try again.\n")

remove_member()

# print(objectCreation.member_dict[1].get_name().lower().strip())

# For browsing the catalogue
def browse_catalogue():
    print("ID \t-\t Title \t\t-\t\t Author")
    for value in objectCreation.book_obj_dict.values():
        print(value)
