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

# Get the validated age
user_age = get_age()
print("User's age:", user_age)
