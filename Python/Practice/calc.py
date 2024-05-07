# Import module ot handle input validation
import pyinputplus as pyip

answer = 0 

# Creating while loop to give the user the option to stop the calculator
while True:
    # Get user choice to stop the calculator
    exit_choice = pyip.inputYesNo('Do you wish to exit? Press enter to continue or type Yes: ', blank=True)
    if exit_choice.lower() == 'yes':
        print('Powering down...')
        break
    else: # Continue to run the calculator
        # Getting 2 integers and the type of mathematics the user wants to use
        choice_1 = pyip.inputInt('Could you enter your first number: ')
        choice_2 = pyip.inputInt('Now please enter your second number: ')
        operation = pyip.inputMenu(['Addition', 'Subtraction', 'Division', 'Multiplication'], numbered=True)
        
        # Conditional logic to calculate the answer and print for the user
        if operation == 'Addition':
            answer = choice_1 + choice_2
            print(f'Calculating...\nDone, the answer is {answer}')           
        elif operation == 'Subtraction':
            answer = choice_1 - choice_2
            print(f'Calculating...\nDone, the answer is {answer}') 
        elif operation == 'Division':
            if choice_2 == 0:
                print('Error: Division by zero!')
                continue
            else:
                answer = choice_1 / choice_2
                print(f'Calculating...\nDone, the answer is {answer}')
        elif operation == 'Multiplication':
            answer = choice_1 * choice_2
            print(f'Calculating...\nDone, the answer is {answer}')
