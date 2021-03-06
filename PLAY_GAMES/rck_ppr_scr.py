from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand
import random

# Print multiline instruction
# performstring concatenation of string
def RockPaperScissor():
    print("Winning Rules of the Rock paper scissor game as follows: \n"
          + "Rock vs paper->paper wins \n"
          + "Rock vs scissor->Rock wins \n"
          + "paper vs scissor->scissor wins \n")

    speak("Winning Rules of the Rock paper scissor game as follows: \n"
          + "Rock vs paper->paper wins \n"
          + "Rock vs scissor->Rock wins \n"
          + "paper vs scissor->scissor wins \n")

    print("The game is best of - choose between 1 to 10  \n")
    speak("The game is best of - choose between 1 to 10  \n")


    while True:
        speak("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

        # take the input from user
        print("User turn:")
        choice = TakeCommand().lower()

        # OR is the short-circuit operator
        # if any one of the condition is true
        # then it return True value
        # looping until user enter invalid input
        while choice > 3 or choice < 1:
            print("\nEnter valid input: ")
            choice = TakeCommand().lower()

        # initialize value of choice_name variable
        # corresponding to the choice value
        if 'one' or 'rock' in choice:
            choice_name == 1
        elif 'two' or 'paper' in choice:
            choice_name ==2
        else:
            choice_name == 3

        # print user choice
        print("user choice is: " + choice_name)
        print("\nNow its computer turn.......")

        # Computer chooses randomly any number
        # among 1 , 2 and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)

        # looping until comp_choice value
        # is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        print("Computer choice is: " + comp_choice_name)

        print(choice_name + " V/s " + comp_choice_name)

        # condition for winning
        if ((choice == 1 and comp_choice == 2) or
                (choice == 2 and comp_choice == 1)):
            print("paper wins => ", end="")
            result = "paper"

        elif ((choice == 1 and comp_choice == 3) or
              (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end="")
            result = "Rock"
        else:
            print("scissor wins =>", end="")
            result = "scissor"

        # Printing either user or computer wins
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        print("Do you want to play again? (Y/N)")
        ans = TakeCommand().lower()

        # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break

    # after coming out of the while loop
    # we print thanks for playing
    speak("Thanks for playing")
    print("\nThanks for playing")