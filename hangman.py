# Importing the choice function from the random library to randomly select a word
from random import choice


# Defining the main game function
# Randomly selecting a word from the list for the game
def run_game():
    word: str = choice(['eraser', 'secret', 'banana', 'phone', 'Maryam'])
    # Getting the user's name and displaying a welcome message
    username: str = input('What is your name? ')
    print(f'Welcome to hangman , {username}')
    # Initializing variables for guessed letters and the number of remaining tries
    guessed: str = ''
    tries: int = 3
    # Main game loop that continues while there are remaining tries
    # Displaying the word with underscores for unknown letters and the guessed letters
    while tries > 0:
        blanks: int = 0
        print('Word: ', end='')
        # Loop through the word to display the correct letters and underscores for unknown ones
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()
        # Checking if all the letters are guessed correctly
        if blanks == 0:
            print('you got it !')
            break
        # Asking the user to enter a letter as their guess
        guess: str = input('Enter a letter: ')
        # Checking if the guess has already been made
        if guess in guessed:
            print(f'You already used: {guess}. please try with another letter!')
            continue
        # Adding the guessed letter to the guessed string
        guessed += guess
        # If the guess is wrong, reduce the number of tries
        if guess not in word:
            tries -= 1
            print(f'sorry , that was wrong... ({tries} tries remaining)')
        # Checking if tries have run out, if so, end the game
        if tries == 0:
            print('Game Over...')
            break


# Running the game if this script is executed directly
if __name__ == '__main__':
    run_game()
