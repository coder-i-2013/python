import random
from colorama import init, Fore, Style
init(autoreset=True)

possible_actions = ["rock", "paper", "scissors"]

while True:
    user = input(f"{Fore.CYAN}Choose your move [rock / paper / scissors]: ").lower()
    computer_action = random.choice(possible_actions)

    print(f"{Fore.MAGENTA}Computer chose: {computer_action}")

    if user == computer_action:
        print(f"{Fore.YELLOW}It's a tie!")

    elif user == "rock":
        if computer_action == "paper":
            print(f"{Fore.RED}Paper covers rock. \nYOU LOSE!")
        else:
            print(f"{Fore.GREEN}Rock smashes scissors. \nYOU WIN!")

    elif user == "paper":
        if computer_action == "scissors":
            print(f"{Fore.RED}Your paper gets cut. \nYOU LOSE!")
        else:
            print(f"{Fore.GREEN}Paper covers rock. \nYOU WIN!")

    elif user == "scissors":
        if computer_action == "rock":
            print(f"{Fore.RED}Rock breaks scissors. \nYOU LOSE!")
        else:
            print(f"{Fore.GREEN}Scissors cut paper. \nYOU WIN!")

    else:
        print(f"{Fore.RED}Invalid choice. Please pick rock, paper, or scissors.")
        continue

    play = input(f"{Fore.CYAN}Do you want to play again? (y/n): ").lower()
    if play == "n":
        print(f"{Fore.BLUE}Thanks for playing! Goodbye!{Style.RESET_ALL}")
        break
