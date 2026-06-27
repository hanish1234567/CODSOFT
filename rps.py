import random
import sys

def show_header():
    print("\n==================================================")
    print("         CODSOFT ROCK-PAPER-SCISSORS AI           ")
    print("==================================================")

def main():
    # Initialize game score matrices
    user_score = 0
    computer_score = 0
    
    choices = ["rock", "paper", "scissors"]
    
    show_header()
    print("Rules: Rock beats Scissors | Scissors beat Paper | Paper beats Rock")
    
    while True:
        print(f"\nSCOREBOARD: You [ {user_score} ] | Computer [ {computer_score} ]")
        print("--------------------------------------------------")
        
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit'): ").strip().lower()
        
        if user_choice in ['exit', 'quit']:
            print("\nFinalizing scores... thanks for playing!")
            print(f"FINAL SCORE - You: {user_score} | Computer: {computer_score}")
            break
            
        if user_choice not in choices:
            print("Error: Invalid weapon chosen. Try again.")
            continue
            
        # AI random structural selection
        computer_choice = random.choice(choices)
        
        print(f"\nYour Choice:     {user_choice.capitalize()}")
        print(f"Computer Choice: {computer_choice.capitalize()}")
        print("--------------------------------------------------")
        
        # Core game rule logic evaluations
        if user_choice == computer_choice:
            print("Result: It's a structural tie! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("Result: 🎉 You Win this round!")
            user_score += 1
        else:
            print("Result: 😢 Computer Wins this round!")
            computer_score += 1
            
        print("==================================================")
        
        # Ask to play again sequence
        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("\nFinalizing scores... thanks for playing!")
            print(f"FINAL SCORE - You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()