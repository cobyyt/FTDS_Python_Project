class MedicalInsurancePlan:
    def __init__(self, name, description, coverage, base_rate):
        self.name = name
        self.description = description
        self.coverage = coverage
        self.base_rate = base_rate




class User:
    def __init__(self, age, health_condition):
        self.age = age
        self.health_condition = health_condition  # "good" or "poor"


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


class InsuranceQuoteSystem:
    def __init__(self):
        self.plans = read_file()  # Call the read_file method here

    def get_best_plan_for(self, user: User):
        if user.age < 30 and user.health_condition == "yes":
            return self.plans["Bronze"]
        elif (user.age >= 30 and user.health_condition == "yes") or (user.health_condition == "no" and user.age < 30):
            return self.plans["Silver"]
        else:
            return self.plans["Gold"]

