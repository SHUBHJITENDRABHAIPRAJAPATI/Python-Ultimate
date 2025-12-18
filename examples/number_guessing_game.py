"""
Number Guessing Game
====================
A fun game where the player tries to guess a random number.
"""

import random

def number_guessing_game():
    """Main game function."""
    print("=" * 40)
    print("Number Guessing Game")
    print("=" * 40)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100!")
                continue
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        
        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts -= 1  # Don't count invalid attempts
    
    if attempts == max_attempts and guess != secret_number:
        print(f"\n😔 Game Over! The number was {secret_number}.")
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() in ['yes', 'y']:
        number_guessing_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
