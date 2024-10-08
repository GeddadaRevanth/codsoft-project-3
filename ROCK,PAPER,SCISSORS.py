import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer selection
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Score tracking
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Play again prompt
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    main()
