from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style, init
import os
import emoji
from blessed import Terminal
term = Terminal()


def print_error(message):
    """
    Function that style all error messages with colorama.
    Style is red background with white letters.
    """
    print(Back.RED + Fore.WHITE + message + Style.RESET_ALL)


def print_success(message):
    """
    Function that style all valid data with colorama.
    Style is green background with black letters.
    """
    print(Back.GREEN + Fore.BLACK + message + Style.RESET_ALL)


def validate_age(prompt):
    """
    Validate data for age and retirement age.
    User must be above 18.
    User should not enter any space before and after.
    User should only enter int and not string data.
    """
    while True:
        age_input = input(prompt)
        age_input_stripped = age_input.strip()

        if age_input_stripped != age_input:
            print_error("Enter your input without space\n")
            continue

        try:
            age = int(age_input_stripped)
            if 18 <= age <= 122:
                print_success("Your age is valid.\n")
                return age
            else:
                print_error("Your age must be above 18 and less then 122.\n")
        except ValueError:
            print_error("Invalid input. Please enter an integer.\n")


def get_age():
    """
    Function to get user input on age and retirement.
    Above function then validates this data.
    """
    age_data = validate_age("Enter your age:\n")
    age_retirement = validate_age("Enter your retirement age:\n")

    print_success("All your data is valid.\n")
    return age_data, age_retirement


def validate_user_input(message):
    """Function to validate user data."""
    while True:
        user_input = input(message)
        user_stripped = user_input.strip()

        if user_stripped != user_input:
            print_error("Enter your input without space\n")
            continue

        try:
            data = int(user_stripped)
            return data
        except ValueError:
            print_error("Invalid input. Please enter an integer.\n")


def get_money_info():
    """
    Function to get the user input.
    After that data is validated with the validate_user_input function.
    """
    salary = validate_user_input("Enter your nett monthly salary(€):\n")
    expense = validate_user_input("Enter your sum of food/leisure expenses(€):\n")
    other_expense = validate_user_input("Enter your sum of other expenses (other loans etc.)(€):\n")

    return salary, expense, other_expense


class Calculator:
    """
    This class consists of all calculations 
    needed to give the user result. Consists of several methods 
    __init__ and some other math methods.
    """

    def __init__(
        self, user_age, user_retirement_age, user_salary, user_expense, user_other_expense
        ):
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
        total_invest = (
            (self.user_retirement_age - self.user_age) * 12) * monthly_invest
        return total_invest
     
    def calculate_total_years(self):
        total_years = self.user_retirement_age - self.user_age
        return total_years


def clear_screen():
    """this function clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


#ef show_menu():
    o#ptions = ["rules", "calculator"]
    t#erminal_menu = TerminalMenu(options)
    m#enu_entry_ind'ex = terminal_menu.show()
    #print(f"You have selected {options[menu_entry_index]}!")
    
    #if __name__ == "__main__":
    #else 
    

def main():
    """
    This is the main function that gets all 
    the validated and calculated data in the end.
    """
    user_age = validate_age("Enter your age(must be above 18):\n")
    print("User's age:\n", user_age)

    user_retirement_age = validate_age("Enter your retirement age:\n")
    print("User's retirement age:\n", user_retirement_age)

    user_salary, user_expense, user_other_expense = get_money_info()
    print("User's salary(€):\n", user_salary)
    print("User's expenses(€):\n", user_expense)
    print("User's other expenses(€):\n", user_other_expense)

    calculator = Calculator(user_age, user_retirement_age, user_salary, user_expense, user_other_expense)
    user_monthly_investment = calculator.calculate_month()
    print("Per month you can invest(€):\n", user_monthly_investment)
    user_total_investment = calculator.calculate_total()
    print("In total you can spend(€):\n", user_total_investment)
    user_total_years = calculator.calculate_total_years()
    print("You will pay off in (years):\n", user_total_years)


print(term.home + term.clear + term.move_y(term.height // 2))
print(term.move_x(0) + term.black_on_darkkhaki("Welcome to the Mortgage calculator.\nEnter only integer.\nNo space.No special characters.\n"))
main()