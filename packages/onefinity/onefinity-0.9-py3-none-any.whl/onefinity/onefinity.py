import math
import random
import os
from onefinity import random_words


def main():
    print("Welcome to OneFinity - A number and word guessing game!")
    print("1. Number Guesser")
    print("2. Number guesser (Computer)")
    print("3. Word Guesser")
    choice = int(input("Enter choice: "))

    if choice == 1:
        os.system('clear')
        number_guesser()
    elif choice == 2:
        os.system('clear')
        number_to_guess()
    elif choice == 3:
        os.system('clear')
        word_guesser()
    else:
        print("Incorrect option entered!")
        exit


def number_guesser():
    print("The computer will choose a number between 1 - 10")
    print("You have to guess it")

    user_guess = int(input("Enter your guess: "))
    computer_choice = random.randrange(1, 10)
    attempt = 0

    while(user_guess != computer_choice):    
        if(user_guess > computer_choice):
            attempt += 1
            print("Guessed too high!")
            user_guess = int(input("Guess again: "))
        elif(user_guess < computer_choice):
            attempt += 1
            print("Guessed too low!")
            user_guess = int(input("Guess again: "))
        else:
            break
        
    print("Congratulations, you got it right.")
    print(f"You got {(5 - attempt) * 2} points!")
    
  
def word_guesser():
    print("The computer will choose a word and give you hints.")
    print("You have to guess it.\n")
    
    print("1. Random words")
    print("2. Animals")
    print("3. Birds")
    print("4. Cities")
    print("5. Countries")
    choice = int(input("Enter: "))
    
    if choice == 1:
        chosen_word = random.choice(random_words.random_words)
    elif choice == 2:
        chosen_word = random.choice(random_words.animals)
    elif choice == 3:
        chosen_word = random.choice(random_words.birds)
    elif choice == 4:
        chosen_word = random.choice(random_words.cities)
    elif choice == 5:
        chosen_word = random.choice(random_words.countries)
    else:
        print("Invalid choice!")
        exit
    
    print(f"The word starts with {chosen_word[0]} and ends with {chosen_word[-1]}. The word also has {len(chosen_word)} letters.")
    guessed_word = input("Enter guess: ")
    
    if guessed_word == chosen_word:
        print("Right, you won!")
    else:
        if len(chosen_word) > 4:        
            updated_chosen_word = ""
            mid = math.floor(len(chosen_word) / 2)
            
            for i in range(1, len(chosen_word) - 1):
                updated_chosen_word += '_'
            
            updated_chosen_word = chosen_word[0] + updated_chosen_word + chosen_word[-1]
            updated_chosen_word = updated_chosen_word[:mid] + chosen_word[mid] + updated_chosen_word[mid+1:]
            
            print("Not correct, you got a hint")
            print(updated_chosen_word)
            new_guess = input("Guess again: ")
            
            if new_guess == chosen_word:
                print("You got it right.")
            else:
                print("That is not right.")
                print(f"The word is {chosen_word}")
        else:
            print("That is not correct.")
            print("As the word has less than 5 letters, there are no hints.")
            print("Try the game again!")
            
        
    
    
def number_to_guess():
    print("Give the minimum and maximum value for the range and choose a number")
    print("The computer will try to guess it")
    
    min_number = int(input("Enter minimum number: "))
    max_number = int(input("Enter maximum number: "))
    
    computer_guess = random.randrange(min_number, max_number)
    print(f"Is the number {computer_guess}?")
    
    choice = input("Enter (higher / lower / yes) : ")
    
    while choice != "yes":
        if choice == "higher":
            max_number = computer_guess
            computer_guess = random.randrange(min_number, max_number)
            print(f"Is it {computer_guess}?")
            choice = input("Enter (higher / lower / yes) : ")
        elif choice == "lower":
            min_number = computer_guess
            computer_guess = random.randrange(min_number, max_number)
            print(f"Is it {computer_guess}?")
            choice = input("Enter (higher / lower / yes) : ")
        else:
            break
        
    print("I got it right. Thank you for playing.")
    
    
    