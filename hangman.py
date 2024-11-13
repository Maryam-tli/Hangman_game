from random import choice


def run_game():
    word: str = choice(['eraser', 'secret', 'banana', 'phone', 'Maryam'])

    username: str = input('What is your name? ')
    print(f'Welcome to hangman , {username}')

    guessed: str = ''
    tries: int = 3
