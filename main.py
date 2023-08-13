from Medical_Insurance import *
from Travel_Insurance import *


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
      quote_system = InsuranceQuoteSystem()
      user = User(age=25, health_condition="no")
      best_plan = quote_system.get_best_plan_for(user)
      print(f"The best plan for you is: {best_plan.name}\n- {best_plan.description}\n "
            f"Maximum Insurance Coverage: ${best_plan.coverage}\n Quote: ${best_plan.base_rate + user.age*2}/year")


# Example usage:
if __name__ == "__main__":
    quote_system1 = TravelQuoteSystem()
    user1 = Traveller(destination='China', trip_duration=8)
    best_plan1, quote1 = quote_system1.get_best_plan_for(user1)
    print(f"The best plan for you is: {best_plan1.name}\n - {best_plan1.description}\n"
          f"Quote: ${quote1}")
