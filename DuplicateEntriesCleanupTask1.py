#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.
#
#Example Code:
#
#customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
#Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, `{'C001', 'C002', 'C003', 'C004'}`. ---

#Writing Code for DuplicateEntriesCleanupTask1


#Instantiating customer ids list
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

#Instantiating user interface function to print customer ids list in user friendly format and calling delete_duplicates function
def user_interface():
    print("Your customer ids:")
#Printing user friendly list
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/ for reference
    cids = ''
    for id in customer_ids:
        cids += id + ' '
    print(cids)
    delete_duplicates()


#Instantiating route comparison function to take in user entry of only y or n and printing comparisions on y entry
def delete_duplicates():
    delete_extras = input("Delete duplicate ID's? Please type (yes/no):\n")
#Creating while loop to catch for any non y or n entry
    while True:
        if delete_extras.lower() == "yes" or delete_extras.lower() == "ok" or delete_extras.lower() == "y":
#Setting customer_ids list into set to automatically delete duplicates and sort random outputasdg
            unique_ids = sorted(set(customer_ids))
#Creating user friendly format
            u_ids = ''
            for uid in unique_ids:
                u_ids += uid + ' '
            print(f"Here is your list of Customer ID's without any duplicates:\n{u_ids}")
            break
        elif delete_extras.lower() == "no" or delete_extras.lower() == "n" or delete_extras.lower() == "no thanks":
            break
#Creating else statement to catch for non y or n entries
        else:
            delete_extras = input("Apologies, please type 'y' or 'n':")
#Prints exiting statement after while loop breaks and ends run after route_comparison function
    print("\nThank you, exiting.")

#Calling user interface function
user_interface()