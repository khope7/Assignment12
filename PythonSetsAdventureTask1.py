#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
#
#1. Destinations that both airlines fly to.
#
#2. Destinations unique to your airline.
#
#3. Whether there are any destinations that neither airline shares.

#Example Code:
#
#our_routes = {"LAX", "JFK", "CDG", "DXB"}
#competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Writing Code for PythonSetsAdventureTask1


#Instantiating routes sets
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Instantiating user interface function to print both airlines routes and calling route comparison function
def user_interface():
#Turning set entry into string and printing for user friendly formatting
#https://www.geeksforgeeks.org/convert-set-to-string-in-python/ for reference
    my_routes = ', '.join(our_routes)
    print("Your routes:")
    print(my_routes)
    print("\nCompetitor routes:")
    their_routes = ', '.join(competitor_routes)
    print(their_routes)
    route_comparison()

#Instantiating route comparison function to take in user entry of only y or n and printing comparisions on y entry
def route_comparison():
    compare_routes = input("Compare routes? Please type (yes/no):\n")
#Creating while loop to catch for any non y or n entry
    while True:
        if compare_routes.lower() == "yes" or compare_routes.lower() == "ok" or compare_routes.lower() == "y":
#Creating operation that checks if both airlines fly to the same element in both sets and prints 
            result1 = our_routes.intersection(competitor_routes)
            r1 = ', '.join(result1)
            print(f"Destinations that both airlines fly to: {r1}")

#Creating operation that checks to see if our routes elements are present in competitor routes and prints
            result2 = our_routes.difference(competitor_routes)
            r2 = ', '.join(result2)
            print(f"Only your airline flys to: {r2}")

#Creating operation that checks for unique elements in both sets and prints
            result3 = our_routes.symmetric_difference(competitor_routes)
            r3 = ', '.join(result3)
            print(f"Locations only on 1 airline for both airlines: {r3}")
            break
        elif compare_routes.lower() == "no" or compare_routes.lower() == "n" or compare_routes.lower() == "no thanks":
            break
#Creating else statement to catch for non y or n entries
        else:
            compare_routes = input("Apologies, please type 'y' or 'n':")
#Prints exiting statement after while loop breaks and ends run after route_comparison function
    print("\nThank you, exiting.")

#Calling user interface function
user_interface()