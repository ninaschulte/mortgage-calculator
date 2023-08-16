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

# Get the validated age
def main(): 
    user_age = get_age()
    print("User's age:", user_age)
    user_retirement_age = get_age_retirement()
    print("User's retirement age:", user_retirement_age)

main()
