class TravelInsurancePlan:
    def __init__(self, name, description, base_rate):
        self.name = name
        self.description = description
        self.base_rate = base_rate


class Traveller:
    def __init__(self, destination, trip_duration):
        self.destination = destination
        self.trip_duration = trip_duration


def read_file():
    plans = {}
    try:
        with open('Travel_Insurance_Plan.txt', 'r') as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                description = data[1]
                base_rate = float(data[2])
                plan = TravelInsurancePlan(name, description, base_rate)
                plans[name] = plan
    except FileNotFoundError:
        print(f"File 'Travel_Insurance_Plan.txt' not found.")

    return plans


def calculate_quote(plan, user: Traveller):
    base_rate = plan.base_rate
    if user.destination.lower() in ['usa', 'canada']:
        base_rate += 30
    if user.trip_duration > 5:
        base_rate += user.trip_duration * 5
    return base_rate


class TravelQuoteSystem:
    def __init__(self):
        self.plans = read_file()

    def get_best_plan_for(self, user: Traveller):
        if user.trip_duration < 60:
            plan = self.plans["Standard"]
            quote = calculate_quote(plan, user)
            return plan, quote
        else:
            plan = self.plans["Premium"]
            quote = self.plans["Premium"].base_rate
            return plan, quote

