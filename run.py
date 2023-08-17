from colorama import just_fix_windows_console

def get_age():
    """
    Get user age and validate this data.
    User must be between 18 and 65.
    User should not enter any space before and after.
    User should only enter int and not string data.
    """
    while True:
        age_input = input("Enter your age:")
        age_input_stripped = age_input.strip() 

        if age_input_stripped != age_input:
            print("Enter your input without space")
            continue

        try:
            age = int(age_input_stripped)
            if 18 <= age <= 65:
                print("Your age is valid.")
                return age
            else:
                print("Your age must be between 18 and 65.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_age_retirement():
    """
    Get user retirement age and validate this data.
    User must be between 18 and 65.
    User should not enter any space before and after.
    User should only enter int and not string data.
    """
    while True:
        age_input = input("Enter your retirement age:")
        age_input_stripped = age_input.strip() 

        if age_input_stripped != age_input:
            print("Enter your input without space")
            continue

        try:
            age_retirement = int(age_input_stripped)
            if 18 <= age_retirement:
                print("Your age is valid.")
                return age_retirement
            else:
                print("Your age must be between 18 and 65.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validate_user_input(message):
    while True:
        user_input = input(message)
        user_stripped = user_input.strip()

        if user_stripped != user_input:
            print("Enter your input without space")
            continue

        try:
            data = int(user_stripped)
            return data  
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_money_info():
    salary = validate_user_input("Enter your nett monthly salary:")
    expense = validate_user_input("Enter your sum of your food, leisure expenses per month:")
    other_expense = validate_user_input("Enter your sum of other expenses (other loans etc.):")

    print("All your data is valid.")
    return salary, expense, other_expense

class Calculator:
    """
    This class consist of all calculations needed to give the user result.
    Consist of several methods __init__ and come other math methods.
    """

    def __init__(self, user_age, user_retirement_age, user_salary, user_expense, user_other_expense):
        self.user_age = user_age
        self.user_retirement_age = user_retirement_age
        self.user_salary = user_salary
        self.user_expense = user_expense
        self.user_other_expense = user_other_expense

    def calculate_month(self):
        monthly_invest = self.user_salary - (self.user_expense + self.user_other_expense)
        return monthly_invest

    def calculate_total(self):
        monthly_invest = self.calculate_month()
        total_invest = ((self.user_retirement_age - self.user_age) * 12) * monthly_invest
        return total_invest

def main(): 
    """
    This is main function that get all the validated and calculated data in the end.
    """
    user_age = get_age()
    print("User's age:", user_age)

    user_retirement_age = get_age_retirement()
    print("User's retirement age:", user_retirement_age)

    user_salary, user_expense, user_other_expense = get_money_info()
    print("User's salary:", user_salary)
    print("User's expenses:", user_expense)
    print("User's other expenses:", user_other_expense)

    calculator = Calculator(user_age, user_retirement_age, user_salary, user_expense, user_other_expense)
    user_monthly_investment = calculator.calculate_month()
    print("Per month you can spend:", user_monthly_investment)
    user_total_investment = calculator.calculate_total()
    print("Your can afford to buy property in:", user_total_investment)

print("Welcome to the Mortgage calculator.\nYou need to type your input without space.\nType only integer.")
main()