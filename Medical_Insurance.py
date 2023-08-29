class MedicalInsurancePlan:
    def __init__(self, name, description, coverage, base_rate):
        self.name = name
        self.description = description
        self.coverage = coverage
        self.base_rate = base_rate




class User:
    def __init__(self, age, health_condition):
        self.age = age
        self.health_condition = health_condition  


def read_file():
    plans = {}
    try:
        with open('Medical_Insurance_Plan.txt', 'r') as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                description = data[1]
                coverage = int(data[2])
                base_rate = float(data[3])
                plan = MedicalInsurancePlan(name, description, coverage, base_rate)
                plans[name] = plan
            file.close()
    except FileNotFoundError:
        print(f"File 'Medical_Insurance_Plan.txt' not found.")

    return plans

def calculate_quote(plan, user: User):
    base_rate = plan.base_rate 
    base_rate += user.age * 2.5
    return base_rate


class InsuranceQuoteSystem:
    def __init__(self):
        self.plans = read_file()  # Call the read_file method here

    def get_best_plan_for(self, user: User):
        if user.age < 30 and user.health_condition == "no":
            plan = self.plans["Bronze"]
            quote = calculate_quote(plan, user)
            return plan, quote
        elif (user.age >= 30 and user.health_condition == "no") or (user.health_condition == "yes" and user.age < 30):
            plan = self.plans["Silver"]
            quote = calculate_quote(plan, user)
            return plan, quote
        else:
            plan = self.plans["Gold"]
            quote = calculate_quote(plan, user)
            return plan, quote

