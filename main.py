from random import randint

# asking player for a rematch


def rematch():
    retry = input('Do you want to try again? y/n ')
    if retry == 'y':
        Number_guessing_game(randint(1, 100))


def Number_guessing_game(answear: int):
    '''Start a game in which you must guess the correct number '''
    print('Wellcome to the number guessing game and please enjoy it! ')
    # choosing a difficulty level
    difficulty = input('On which difficulty do you want to play? easy/hard ')
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        print('Do not try to be funny')

# guessing
    while True:
        guess = int(input('Give me your guess: '))
        if guess > answear:
            print('Too high!')
            lives -= 1
            print(f'You have {lives} lives left')
        elif guess < answear:
            print('Too low!')
            lives -= 1
            print(f'You have {lives} lives left')
        else:
            print('You win!')
            rematch()

        if lives == 0:
            print('You ran out of lives!')
            rematch()


number_to_guess = randint(1, 100)
Number_guessing_game(number_to_guess)
