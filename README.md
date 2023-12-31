# Mortgage Calculator

This is a mortgage calculator that estimates the amount of money you can afford to spend or borrow as a loan. Here you can view the project [LINK](https://ninaschulte-mortgagecalculator-4bb5d57d1e7f.herokuapp.com/).

*Please note that these calculations are simplified and a real mortgage calculator would need to consider additional factors, such as taxes and fees.
## User stories
| ID | User Stories |
|----|--------------|
| 1 | As a user, I wish to view a welcome message to understand the purpose of this program. |
| 2 | As a user, I desire to access rules to make an informed decision about proceeding with my calculations. |
| 3 | As a user, I aim to find a clear starting point for utilizing the mortgage calculator. |
| 4 | As a user, I expect to receive an error message when my input contains mistakes. |
| 5 | As a user, I anticipate receiving a success message when my entered data is valid. |
| 6 | As a user, I would like to see final calculations in order to comprehend the potential investment amount. |
## Flowchart
The flowchart represents the logic of the application:
![Image Alt Text](./documentation/flowchart.png)
## Features
### Welcome message
A welcome message display two emojis and text in typewriter style. It also display menu where user can choose between rules and calculator.
![Image Alt Text](./documentation/welcome.png)
### Rules
An explanation to the user about the purpose of the program and a set of accompanying rules.
![Image Alt Text](./documentation/rules.png)
### Go back button
A "Go back" button is provided on both the rules screen and upon completing the calculator. This button returns the user to the initial page, where they can choose between rules and the calculator.
### User input
The calculator prompts users to input their current age, retirement age, salary, disposable income, and other expenses. The calculator validates the data, and the data is considered invalid in the following cases:

- If there's a space before or after the user input.
- If there's a special character or any non-integer value.
- For age input, there's also an age validation ensuring the user is at least 18 years old and cannot retire before the age of 40.

The application provides user feedback when the data is found to be invalid, as well as when the data is valid. Refer to the details in the screenshot below.
![Image Alt Text](./documentation/age_val.png)
### Salary, expenses and other expenses input
The calculator also prompts users for three additional inputs: salary, regular expenses, and other expenses. If the total expenses exceed the user's salary, the program returns an error indicating that the user cannot afford to buy a property.
![Image Alt Text](./documentation/expense_error.png)
### Result
Upon successful validation of the input data, the program presents the user with a results page displaying three calculated values:

- The monthly amount available for investment.
- The total investment amount over the years (calculated as user's salary minus the sum of all expenses).
- The number of years required to pay off this investment (calculated as (retirement age - user age) * 12) * monthly amount.
  
![Image Alt Text](./documentation/result.png)
## Technologies Used
### Languages:
- [Python](https://docs.python.org/3/library/os.html): serves as the foundation of the project, guiding and shaping all aspects of the application's behavior.
- [JavaScript](https://www.javascript.com/): contributes the essential start script, enabling the execution of the Code Institute's mock terminal within the browser environment.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): is employed in crafting the fundamental elements integral to constructing the simulated terminal experience within the browser.
## Frameworks/Libraries, Programmes and Tools
### Python modules/packages:
#### Standard library imports:
- [os](https://docs.python.org/3/library/os.html) module for various operating system-related tasks.
- [time](https://docs.python.org/3/library/time.html) this module was imported for timewriter functionality of the welcome text.
- [sys](https://docs.python.org/3/library/sys.html) this module was imported for timewriter functionality of the welcome text.
#### Third-party imports:
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.
- [Simple Menu](https://pypi.org/project/simple-term-menu/) was used to implement the menu.
- [Emoji](https://pypi.org/project/emoji/) was used for emojis.
#### Other tools:
- [Codeanywhere](https://dashboard.codeanywhere.com/) was used to edit code.
- [GitHub](https://github.com/) was used to host the website's code.
- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) was used to deploy the project.
## Testing
### PEP3
The code was tested with [PEP3](https://pep8ci.herokuapp.com/). This checking was done manually by copying python code and pasting it into the validator.
No errors were found:
![Image Alt Text](./documentation/pep.png)
### Manual testing
| Test Scenario | Pass/Fail |
|---------------|-----------|
| Run the app and view the title, menu: rules, calculator. | Pass |
| Tap on the "rules" tab and view the text. | Pass |
| Tap on the "back button" and view the menu. | Pass |
| Tap on "calculator" to view the application title and the first question. | Pass |
| Enter age and retirement data; confirm that the view displays data as valid in green. | Pass |
| Enter salary input, your expenses, and other expenses; ensure that the view shows data as valid text in green. | Pass |
| View the result and the three calculations: monthly investment, total investment, and years to pay off. | Pass |
| Tap the "go back" button and click on "calculator." | Pass |
| Test for errors: enter input with space, special character; for age, validate the age and confirm that the view displays data as not valid in red. | Pass |
| Also, enter expenses greater than salary and observe the view showing an error that you can't afford anything. | Pass |
### Bugs
#### Validate data on money input fields
1. I have a code with three money inputs that need to be validated. In my first version of the code, I attempted to validate all three inputs through one while loop. The issue here was that the error messages didn't appear, and in case of an error, the terminal just displayed the same question again.
```python
def get_money_info():
    """
    Function that will get user input on salary, expenses, and other expenses.
    Function also validate user input data based on space around and special characters.
    """
    salary, expense, other_expense = None, None, None
    
    while salary is None or expense is None or other_expense is None:
        user_input = input("Enter your input:")

        if user_input.strip() != user_input:
            print("Enter your input without space")
            continue

        try:
            value = int(user_input.strip())
            if salary is None:
                salary = value
            elif expense is None:
                expense = value
            elif other_expense is None:
                other_expense = value
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("All your data is valid.")
    return salary, expense, other_expense

```
2. Then I created three separate while loops within a single function. This resolved the problem of error messages not displaying. However, according to the best practices that I learned at Code Institute, this wasn't the optimal approach, as it's recommended to have small functions.
```python
def get_money_info():
    """
    Function that will get user input on salary, expenses, and other expenses.
    Function also validate user input data based on space around and special characters.
    """
    while True:
        salary_input = input("Enter your nett monthly salary:")
        salary_input_stripped = salary_input.strip()

        if salary_input_stripped != salary_input:
            print("Enter your input without space")
            continue

        try:
            salary = int(salary_input_stripped)
            break  
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    while True:
        expense_input = input("Enter your sum of your food, leisure expenses per month:")
        expense_input_stripped = expense_input.strip()

        if expense_input_stripped != expense_input:
            print("Enter your input without space")
            continue

        try:
            expense = int(expense_input_stripped)
            break  
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        other_expense_input = input("Enter your sum of other expenses (other loans etc.):")
        other_expense_input_stripped = other_expense_input.strip()

        if other_expense_input_stripped != other_expense_input:
            print("Enter your input without space")
            continue

        try:
            other_expense = int(other_expense_input_stripped)
            break  
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("All your data is valid.")
    return salary, expense, other_expense
```
3. After that I was trying out different approaches how to make this code shorter and also readable and I created two different functions out of it. 
```python
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
            print_success("Your data is valid.")
            return data
        except ValueError:
            print_error("Invalid input. Please enter an integer.\n")


def get_money_info():
    """
    Function to get the user input.
    After that data is validated with the validate_user_input function.
    """
    salary = validate_user_input("Enter your nett monthly salary(€):\n")
    expense = validate_user_input("Enter your sum of your disposal income(€):\n")
    other_expense = validate_user_input("Enter your sum of other expenses (other loans etc.)(€):\n")

    if expense + other_expense > salary:
        return None, expense, other_expense

    return salary, expense, other_expense
```
## Deployment 
- The program was deployed to [Heroku]([[https://pypi.org/project/colorama/](https://dashboard.codeanywhere.com/)](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)).
- The program can be reached by the [link](https://ninaschulte-mortgagecalculator-4bb5d57d1e7f.herokuapp.com/)
### Steps to launch the application
1. In Codeanywhere, create a list of requirements.txt that project needs to run (all the imports). Run command "Pip3 freeze > requirements.txt". 
2. Save changes and with command git push, push the files to your repository.
3. Create a [Heroku](https://dashboard.heroku.com/account) account.
4. Create a new Heroku application on the following page [Heroku - new app](https://dashboard.heroku.com/apps):
   ![Image Alt Text](./documentation/new_app.png)
5. Tap on deploy:
   ![Image Alt Text](./documentation/deploy.png)
6. Link your GitHub account and connect the application to the repository:
   ![Image Alt Text](./documentation/connect_github.png)
7. Tap on Setting:
   ![Image Alt Text](./documentation/setting.png)
8. Click on "Add buildpack":
   ![Image Alt Text](./documentation/add_buildpack.png)
9. Add the Python and Node.js buildingpacks in the following order:
    ![Image Alt Text](./documentation/node_python.png)
11. Click on "Reveal Config Vars":
   ![Image Alt Text](./documentation/config.png)
12. Add 1 new config vars:
    - Key: PORT Value: 8000
    - Provided by [Code Institute](https://codeinstitute.net/de/)
13. Go back to Deploy tab:
    ![Image Alt Text](./documentation/deploy.png)
14. Click on "Deploy Branch:
    ![Image Alt Text](./documentation/manual.png)
15. Wait for the completion:
    ![Image Alt Text](./documentation/wait_completion.png)
16. Click on "View" to launch the application inside a web page:
    ![Image Alt Text](./documentation/successfuldeploy.png)
## Credits
- For colors in the terminal, I used [colorama](https://pypi.org/project/colorama/).
- For menu, I used [Simple Menu](https://pypi.org/project/simple-term-menu/)
- For validating [Python tutorials on Errors](https://docs.python.org/3/tutorial/errors.html) and a helpful [YouTube tutorial](https://www.youtube.com/watch?v=LUWyA3m_-r0&t=644s).
- Typewrite style is covered in this [YouTube tutorial](https://www.youtube.com/watch?v=2h8e0tXHfk0).
- If statements are explained in the [Python tutorial on if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements).
- For space validation, I refer to the [Python tutorial on strip()](https://docs.python.org/3/library/stdtypes.html#str.strip).
- For many small details, I used also [Python W3Schools resource](https://www.w3schools.com/python/).
### Acknowledgements
- I am truly grateful for the unwavering support and valuable feedback provided by my mentor [Julia Konovalova](https://github.com/IuliiaKonovalova) throughout my journey. Julia Konovalova guidance has been instrumental in shaping my growth and progress.
