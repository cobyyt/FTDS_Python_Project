from Medical_Insurance import *
from Travel_Insurance import *

def get_user_input():
    while True:
        inp = int(input('What kind of insurance are you looking for?\n 1. Medical Insurance\n 2. Travel Insurance\n'))
        if inp == 1:

            # Instantiate the InsuranceQuoteSystem
            quote_system = InsuranceQuoteSystem()

            # Prompt the user for input
            age = int(input("Pease enter your age: "))
            health_condition = input("Do you have any health conditions? (yes/no): ")

            # Create a User object with the provided input
            user = User(age, health_condition)
            # Get the best plan for the user

            best_plan = quote_system.get_best_plan_for(user)

            # Display the result
            print(f"The best plan for you is: {best_plan.name}\n- {best_plan.description}\n "
                    f"Maximum Insurance Coverage: ${best_plan.coverage}\n Quote: ${best_plan.base_rate + user.age*2}/year\n"
                        f"------------------------------------------------------------------------------------")
            break
            
        elif inp == 2:
            quote_system1 = TravelQuoteSystem()
            destination = input("Please enter your destination: ")
            trip_duration = int(input("How many days will you travel? "))
            user1 = Traveller(destination, trip_duration)
            best_plan1, quote1 = quote_system1.get_best_plan_for(user1)
            print(f"The best plan for you is: {best_plan1.name}\n - {best_plan1.description}\n"
                    f"Quote: ${quote1}\n"
                        f"------------------------------------------------------------------------------------")
            break
            
        else:
            # Invalid input
            print("Please input 1 or 2")
            print("------------------------------------------------------------------------------------")