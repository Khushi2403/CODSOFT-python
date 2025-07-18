import random

# Mapping choices to hand emojis
hand_symbols = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌"
}

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_choices(user, computer):
    print(f"\nYou chose: {user} {hand_symbols[user]}")
    print(f"Computer chose: {computer} {hand_symbols[computer]}")

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game ! 🎮")

    while True:
        user_choice = input("\nEnter rock, paper, or scissors: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        display_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print("🏁 Result:", result)

        # Score tracking
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"\n📊 Score => You: {user_score} | Computer: {computer_score}")

        # Ask for another round
        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n👋 Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

# Run the game
play_game()
