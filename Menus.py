import menuFunctions


def staff_menu():
    """Menu for staff users"""
    while True:
        user_input = input("What would you like to do?\n"
                           "1. Add or Remove Member\n"
                           "2. Modify Member\n"
                           "3. Add or Remove Item\n"
                           "4. Return to Main Menu\n")
        if user_input == "1":
            add_or_remove = input("Would you like to add or remove?\n")
            if add_or_remove.lower() == "add":
                menuFunctions.add_member()
            elif add_or_remove.lower() == "remove":
                menuFunctions.remove_member()
            else:
                print("Invalid input. Please try again.")
            input("Press any key to continue..\n")

        elif user_input == "2":
            menuFunctions.modify_member()
            input("Press any key to continue..\n")

        elif user_input == "3":
            add_or_remove = input("Would you like to add or remove?\n")
            if add_or_remove.lower() == "add":
                menuFunctions.add_item()
            elif add_or_remove.lower() == "remove":
                menuFunctions.remove_item()
            else:
                print("Invalid input. Please try again.")
            input("Press any key to continue..\n")

        elif user_input == "4":
            print("Returning to main menu...")
            break
        else:
            print("Not a valid option. Try again.\n")


def member_menu():
    """Menu for Member users"""
    while True:
        user_input = input("What would you like to do?\n"
                           "1. Browse Catalogue\n"
                           "2. Borrow Catalogue Item\n"
                           "3. Return Catalogue Item\n"
                           "4. View Items I'm Currently Borrowing\n"
                           "5. View my Overdue Items\n"
                           "6. Join Library\n"
                           "7. Cancel Membership\n"
                           "8. Return to Main Menu\n")
        if user_input == "1":
            menuFunctions.browse_catalogue()
            input("Press any key to continue..\n")
        elif user_input == "2":
            menuFunctions.borrow_item()
            input("Press any key to continue..\n")
        elif user_input == "3":
            menuFunctions.return_item()
            input("Press any key to continue..\n")
        elif user_input == "4":
            menuFunctions.my_borrow_list()
            input("Press any key to continue..\n")
        elif user_input == "5":
            menuFunctions.my_overdue_list()
            input("Press any key to continue..\n")
        elif user_input == "6":
            menuFunctions.add_member()
            input("Press any key to continue..\n")
        elif user_input == "7":
            menuFunctions.cancel_membership()
            input("Press any key to continue..\n")
        elif user_input == "8":
            print("Quitting program...")
            break
        else:
            print("Not a valid option. Try again.\n")


def main_menu():
    while True:
        user_input = input("Which user are you?\n"
                           "1. Staff\n"
                           "2. Member\n"
                           "3. Quit Program\n")
        if user_input == "1":
            staff_menu()
            input("Press any key to continue..\n")
        elif user_input == "2":
            member_menu()
            input("Press any key to continue..\n")
        elif user_input == "3":
            print("Quitting program...")
            break
        else:
            print("Not a valid option. Try again.\n")

# Main


main_menu()
