from random import choice

def run_hangman():
    word: str = choice(['ocean', 'whale', 'fish', 'dolphin', 'wave'])
    
    username: str = input('What is your name? >>')
    print(f'Welcome to hangman game, {username}')

    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks+=1

        print() # Add a blank line

        if blanks == 0:
            print('You got it!')
            break

        guess: str = input('Please enter a letter: ')

        if guess in guessed:
            print(f"You've already entered the '{guess}', please enter another letter.")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry that was wrong, {tries} tries remaining')

            if tries == 0:
                print('No more tries remaining, you lost.')
                break

if __name__ == '__main__':
    run_hangman()
