import random

def get_lower():
    input_lower = int(input('Enter the lower bound:'))
    return input_lower
    

def get_upper(lower):
    input_upper = int(input('Enter the upper bound:'))
    if input_upper > lower:
        return input_upper
    else:
        print('The lower bound must be less than the upper bound.')
        get_upper()


def compare_validated_nums(input_val, comparative_val):
    if input_val > comparative_val:
        print('Nope, too high.')
    elif input_val < comparative_val:
        print('Nope, too low.')
    else:
        print('You got it!')
        

def run_app():
    input_username = input('Please enter your name')
    print(f'Welcome to the higher/lower game, {input_username}!')
    
    validated_lower = get_lower()

    validated_upper = get_upper(validated_lower)

    has_guessed_once = False

    def get_guess(flag):
        if flag:
            subsequent_guess = input(f'Guess another number: ')
        else:
            has_guessed_once = True
            first_guess = input(f'Great, now guess a number between {validated_lower} and {validated_upper}: ')
            compare_validated_nums(first_guess)
    
    get_guess(has_guessed_once)


run_app()