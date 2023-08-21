
import os
import time
import sys
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style, init
import emoji


def show_menu():
    """
    Function that shows the menu.
    In the menu you can see rules and calculatior.
    With "enter", "alt-d", "ctrl-i" you can navigate through the menu.
    """
    terminal_menu = TerminalMenu(
        ["rules", "calculator"], accept_keys=("enter", "alt-d", "ctrl-i")
        )
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        print(
            "Estimate property affordability using this mortgage calculator.\n"
            )
        print("Here are some rules that you need to follow:\n")
        print(f"""
        Please don´t use special characters.\n
        Please type without space.\n
        You must be at leat 18 years old.\n
        """)
        go_back()
    else:
        main()
        go_back()


def go_back():
    """Function that return user to the menu."""
    terminal_menu = TerminalMenu(
        ["go back"], accept_keys=("enter", "alt-d", "ctrl-i")
        )
    menu_entry_index = terminal_menu.show()
    clear_screen()

    if menu_entry_index == 0:
        print(
            "☠️ Welcome to the best mortgage calculator in the universe. ☠️\n"
            )
        show_menu()


def clear_screen():
    """this function clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(message):
    """
    Function that style all error messages with colorama.
    Style is red background with white letters.
    """
    print(Fore.RED + message + Style.RESET_ALL)


def print_success(message):
    """
    Function that style all valid data with colorama.
    Style is green background with black letters.
    """
    print(Fore.GREEN + message + Style.RESET_ALL)


def validate_age(prompt, min_age, max_age):
    """
    Validate data for age and retirement age.
    User must be within the specified age range.
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
            if min_age <= age <= max_age:
                print_success("Your age is valid.\n")
                return age
            else:
                print_error(
                    f"Your age must be between {min_age} and {max_age}.\n"
                    )
        except ValueError:
            print_error("Invalid input. Please enter an integer.\n")


def get_age():
    """
    Function to get user input on age and retirement.
    Above function then validates this data.
    """
    age_data = validate_age(
        "Enter your age (must be above 18):\n", 18, 122
        )
    age_retirement = validate_age(
        "Enter your retirement age (must be above 40):\n", 40, 122
        )

    print_success("All your data is valid.\n")
    return age_data, age_retirement


def validate_user_input(message):
    """
    Function to validate user data.
    Return error in case of space, special character.
    Return valid in case of int.
    """
    while True:
        user_input = input(message)
        user_stripped = user_input.strip()

        if user_stripped != user_input:
            print_error("Enter your input without space\n")
            continue

        try:
            data = int(user_stripped)
            print_success("Your data is valid.")
            return data
        except ValueError:
            print_error("Invalid input. Please enter an integer.\n")


def get_money_info():
    """
    Function to get the user input.
    After that data is validated with the validate_user_input function.
    """
    salary = validate_user_input(
        "Enter your nett monthly salary(€):\n"
        )
    expense = validate_user_input(
        "Enter your sum of your disposal income(€):\n"
        )
    other_expense = validate_user_input(
        "Enter your sum of other expenses (other loans etc.)(€):\n"
        )

    if expense + other_expense > salary:
        return salary, expense, other_expense
    return salary, expense, other_expense


class Calculator:
    """
    This class consists of all calculations
    needed to give the user result.
    Consists of several methods
    __init__ and some other math methods.
    """

    def __init__(self, user_a, user_ret_a, user_sal, user_exp, user_other_exp):
        self.user_a = user_a  # user age
        self.user_ret_a = user_ret_a  # user retirement age
        self.user_sal = user_sal  # user salary
        self.user_exp = user_exp  # user expenses (disposal income (€))
        self.user_other_exp = user_other_exp  # other expenses

    def calculate_month(self):
        """Calculate how much you can invest per month"""
        if self.user_sal is None:
            return None
        monthly_invest = self.user_sal - (
            self.user_exp + self.user_other_exp
            )
        return monthly_invest

    def calculate_total(self):
        """Calculate total investment"""
        if self.user_sal is None:
            return None
        monthly_invest = self.calculate_month()
        total_invest = (
            (self.user_ret_a - self.user_a) * 12) * monthly_invest
        return total_invest

    def calculate_total_years(self):
        """Calculate in how many years you need to pay off total investment"""
        if self.user_sal is None:
            return None
        total_years = self.user_ret_a - self.user_a
        return total_years


def typewriter(message):
    """Function for special effect for welcome message"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def welcome_message():
    """Function that exist only to display welcome message"""
    typemessage = typewriter(
        "☠️ Welcome to the best mortgage calculator in the universe. ☠️\n"
        )


def main():
    """
    This is the main function that gets all
    the validated and calculated data in the end.
    """
    user_a = validate_age(
        "Enter your age(must be above 18):\n", 18, 122
        )
    print("Your age:\n", user_a)

    user_ret_a = validate_age(
        "Enter your retirement age:\n", 40, 122
        )
    print("Your retirement age:\n", user_ret_a)

    user_sal, user_exp, user_other_exp = get_money_info()
    print("Your salary (€):\n", user_sal)
    print("Sum of your disposal income (€):\n", user_exp)
    print("Your other expenses (€):\n", user_other_exp)

    if user_sal is not None and (user_exp + user_other_exp) <= user_sal:

        calculator = Calculator(
            user_a,
            user_ret_a,
            user_sal, user_exp,
            user_other_exp
        )
        user_monthly_investment = calculator.calculate_month()
        print("Per month you can invest (€):\n", user_monthly_investment)
        user_total_investment = calculator.calculate_total()
        print(
            "Your total investment (€):\n", user_total_investment
            )
        user_total_years = calculator.calculate_total_years()
        print("You will pay off in (years):\n", user_total_years)
    else:  # display error message in case of bigger expenses then salary
        print_error("Sorry, you can't afford to buy anything.\n")


welcome_message()
show_menu()
main()
