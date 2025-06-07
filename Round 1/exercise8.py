import random
while True:

    def determine_winner(p1, p2):
        if p1 == p2:
            return "It's a draw!"
        elif (p1 == "rock" and p2 == "scissor") or \
            (p1 == "scissor" and p2 == "paper") or \
            (p1 == "paper" and p2 == "rock"):
            return "You win!"
        else:
            return "Computer wins!" # Changed for computer opponent

    valid_choices = ["rock", "paper", "scissor"]

    print("\n🎮 Welcome to the Rock-Paper-Scissors Game against the Computer!")

    while True:
        p1 = input("Enter your choice (rock/paper/scissor): ").strip().lower()
        computer_choice = random.choice(valid_choices)

        if p1 not in valid_choices:
            print("❌ Invalid input. Please enter 'rock', 'paper', or 'scissor'.")
            continue

        result = determine_winner(p1, computer_choice)
        print(f"\nYou chose: {p1.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        print(f"Result: {result}")

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break