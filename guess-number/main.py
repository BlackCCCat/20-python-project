import random

def main():
    scale = input('Choose a number between 1 and ? :')
    number = random.randint(1, int(scale))
    game = True
    while game:
        guess = input('Enter your guess: ')
        guess = int(guess)

        if guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        else:
            print('Correct')
            game = False
    
    restart = input('Would you like to play again? (y/n)')
    if restart == 'y':
        main()
    else:
        print('Goodbye!')


if __name__ == '__main__':
    main()