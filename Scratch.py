import os
import LMS_Classes
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
print(objectCreation.book_obj_dict[1])
my_instance = objectCreation.book_obj_dict[1]
print(my_instance.release_date)
