import random

def display_scores(user_score, computer_score, number_of_tours):
    print(f"Score is: {user_score}-{computer_score} for {number_of_tours} tours.")

# Rules are:
# Rock beats scissors
# Scissors beat paper
# Paper beats rock
options = ['rock', 'paper', 'scissors']

# Initialization of the scores
user_score = 0
computer_score = 0

# Initialization of number ot tours
number_of_tours = 0
print("Welcome to Rock, Paper, Scissors!")

# while the user continues playing
while True:
    # we start with an empty choice
    user_choice = ""

    # the player enters either rock, paper or scissors. If something else, then display a message
    while (user_choice not in options):
        # if the user didn't choose anything, we just redisplay the input
        if (user_choice != ""):
            print("You entered an invalid choice.")
        user_choice = input("Please choose between 'rock', 'paper', or 'scissors': ")

    # we randomly select the computer's choice
    computer_choice = random.choice(options)
    print("The computer chose : " + computer_choice)

    # user and computer chose something, we increment the number of tours
    number_of_tours += 1

    # we compare the user choice and the computer choice to determine who won
    if (user_choice == computer_choice):
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
        print("You win!")
        user_score += 1
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    # display the scores and the number of tours
    display_scores(user_score, computer_score, number_of_tours)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

# display the final scores and the final number of tours
display_scores(user_score, computer_score, number_of_tours)