import random
import string

def hangman():
    # List of words for the game
    word_list = ["python", "hangman", "computer", "programming", "algorithm", 
                 "developer", "keyboard", "internet", "software", "debugging"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list).lower()
    letters_guessed = set()  # Letters the player has guessed
    alphabet = set(string.ascii_lowercase)
    remaining_letters = alphabet - letters_guessed
    word_letters = set(secret_word)  # Letters in the secret word
    
    lives = 6  # Number of incorrect guesses allowed
    
    while len(word_letters) > 0 and lives > 0:
        # Letters already guessed
        print(f"You have {lives} lives left and you've used these letters: {' '.join(letters_guessed)}")
        
        # Show current progress (like p _ _ p _ _)
        current_word = [letter if letter in letters_guessed else '_' for letter in secret_word]
        print("Current word:", ' '.join(current_word))
        
        # Get user input
        user_letter = input("Guess a letter: ").lower()
        
        if user_letter in remaining_letters:
            letters_guessed.add(user_letter)
            remaining_letters.remove(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1  # Wrong guess
                print(f"\nYour letter, {user_letter}, is not in the word.")
        elif user_letter in letters_guessed:
            print("\nYou've already guessed that letter. Try again.")
        else:
            print("\nThat's not a valid letter.")
    
    # Game ends here
    if lives == 0:
        print(f"You died! The word was {secret_word}")
    else:
        print(f"Congratulations! You guessed the word {secret_word}!")

if __name__ == "__main__":
    hangman()