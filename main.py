from Medical_Insurance import *
from Travel_Insurance import *

if __name__ == "__main__":
    print('----------------------- Insurance Quote System -----------------------')
    while True:
        try:
            inp = int(input('What kind of insurance are you looking for?\n 1. Medical Insurance\n 2. Travel Insurance\n Type: '))
            if inp == 1: # Medical

                # Instantiate the InsuranceQuoteSystem
                quote_system = InsuranceQuoteSystem()

                # Prompt the user for input
                while True:
                    try:
                        age = int(input("Please enter your age: "))
                        if age > 0:
                            break
                        else:
                            print("Invalid age. Please enter a positive number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    health_condition = input("Do you have any health conditions? (yes/no): ").lower()
                    if health_condition in ['yes', 'no']:
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

                # Create a User object with the provided input
                user = User(age, health_condition)
                
                # Get the best plan for the user
                best_plan, quote = quote_system.get_best_plan_for(user)

                # Display the result
                print(f"The best plan for you is: {best_plan.name}\n- {best_plan.description}\n "
                        f"Maximum Insurance Coverage: ${best_plan.coverage:,}\n Quote: ${quote:,}/year\n"
                            f"------------------------------------------------------------------------------------")
                break
                
            elif inp == 2: # Travel
                quote_system_travel = TravelQuoteSystem()

                while True:
                    destination = input("Please enter your destination: ")
                    if destination:
                        break
                    else:
                        print("Invalid input. Please enter a destination.")

                while True:
                    try:
                        trip_duration = int(input("How many days will you travel? "))
                        if trip_duration > 0:
                            break
                        else:
                            print("Invalid number of days. Please enter a positive number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                traveller = Traveller(destination, trip_duration)
                best_plan_travel, quote_travel = quote_system_travel.get_best_plan_for(traveller)

                print(f"The best plan for you is: {best_plan_travel.name}\n - {best_plan_travel.description}\n"
                        f"Quote: ${quote_travel:,}\n"
                            f"------------------------------------------------------------------------------------")
                break
                
            else:
                print("Please input 1 or 2")              

        except ValueError:
            print("Invalid input. Please input 1 or 2")