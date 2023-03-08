import random 
import time 

class RockPaperScissors:
    def __init__(self):
        self.user_wins = 0 
        self.computer_wins = 0 
        self.random_number = random.randint(0, 2) 
        self.options = ["rock", "paper", "scissors"] 

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            
            if self.user_wins == 2: 
                print("Congratulations! You win!")
                break
            if self.computer_wins == 2: 
                print("Sorry, you lose!")
                break
            if user_input == "q": 
                print("Thanks for playing!")
                break
            
            if user_input not in self.options: 
                print("Invalid input, please try again.")
                continue
            computer_pick = self.options[self.random_number]
            print("Computer picked", computer_pick + ".")
    
            if user_input == "rock" and computer_pick == "scissors":
                print("Rock smashes scissors!")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                
            elif user_input == "paper" and computer_pick == "rock":
                print("Paper covers rock!")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                
            elif user_input == "scissors" and computer_pick == "paper":
                print("Scissors cut paper!")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                
            elif user_input == computer_pick:
                print("It's a tie! Try again.")
                self.random_number = random.randint(0, 2)
                
            else:
                print("Computer wins this round!")
                self.computer_wins += 1
                self.random_number = random.randint(0, 2)
        
            print("Your score: ", self.user_wins)
            print("Computer score: ", self.computer_wins)
            print()
            
game = RockPaperScissors()
game.play()
