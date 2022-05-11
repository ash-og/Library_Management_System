import datetime
import os
import LMS_Classes
import menuFunctions
import objectCreation
# import menuFunctions


# temp_list = []
# with open("members.txt", "r") as member_file:
#     for line in member_file.readlines():
#         temp_list.append(line)
# print(temp_list)

# "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format{id, name, m_type, dob, address, location, phone, email, branch}

# writing changes to the file
# try:
#     os.remove("test.txt")
# except FileNotFoundError:
#     pass
# new_file = open("test.txt", "w+")
# for value in objectCreation.member_dict.values():
#     entry = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(value.ID, value.get_name(), value.type, value.get_dob(), value.get_address(), value.get_location(), value.get_phone(), value.get_email(), value.get_branch())
#     print(entry, file=new_file)
# new_file.close()
#
# with open("test.txt", "r") as test_file:
#     print(test_file.read())
# print(objectCreation.book_obj_dict[1])
# my_instance = objectCreation.book_obj_dict[1]
# print(my_instance.release_date)
#
# m_attr = "set_name()"
# m_value = "Sarah Young"
# objectCreation.member_dict[6].m_attr(m_value)
# print(objectCreation.member_dict[6].get_name())
#
# def attr_input_menu():
#     user_input = input("Which value would you like to modify?\n "
#                        "1. Name \n"
#                        "2. Member Type \n "
#                        "3. DOB \n"
#                        "4. Address \n"
#                        "5. Location \n"
#                        "6. Phone \n"
#                        "7. Email)?\n"
#                        "8. Quit\n")
#     new_value = input("Please enter the updated value: ")
#     if user_input == "1":
#         m_attr = name
#     elif user_input == "2":
#         m_attr = m_type
#     elif user_input == "3":
#         m_attr = dob
#     elif user_input == "4":
#         m_attr = address
#     elif user_input == "5":
#         m_attr = location
#     elif user_input == "6":
#         m_attr = phone
#     elif user_input == "7":
#         m_attr = email
#     elif user_input == "8":
#         print("Returning to previous menu\n")
#         break
#     else:
#         print("Invalid option. Please try again.")




# mid = 6
# new_value = "Sarah Young"
# objectCreation.member_dict[mid].set_name(new_value)
# print(objectCreation.member_dict[mid].get_name())
# menuFunctions.rewrite_members()
# new_value = "0982738482"
# print(objectCreation.member_dict[mid].type)
# objectCreation.member_dict[mid].type = new_value
# print(objectCreation.member_dict[mid].type)
# print(objectCreation.member_dict[mid])
# menuFunctions.rewrite_members()
# objectCreation.member_dict[mid].set_phone(new_value)
# menuFunctions.rewrite_members()
# print("This member's address is now: ")
# print(objectCreation.member_dict[mid].get_phone())

# def itemObjectDict(list, objectClass):
#     """Creating a dictionary of class objects from a list"""
#     obj_dict = {}
#     for item in list:
#         obj_dict[int(item[0])] = objectClass(int(item[0]), item[1], item[2], item[3], item[4], item[5])
#     return obj_dict



# def libObjectDict(list, objectClass):
#     """Creating a dictionary of class objects from a list"""
#     obj_dict = {}
#     for item in list:
#         obj_dict[int(item[0])] = objectClass(int(item[0]), item[1], item[2], item[3], item[4], item[5])
#     return obj_dict



print(datetime.date.today().strftime("%d-%m-%Y"))
