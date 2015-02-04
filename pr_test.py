# Simple text based game, Try to guess the number in 10 times.

from random import randint

print("\n\nWelcome to the 'Random Number Game!' ")
player = raw_input("What is your name? >>>  ")
name = player.capitalize()

print("\nHello {}!, I am thinking of a number between 1 - 100!").format(name)
print("I will give you 10 tries to guess my number, ready? GO!")

number = randint(1, 100)
turns = 0

for turns in range(10):
	guess = int(raw_input("\nWhat do you think my number is >>> "))
	
	if guess == number:
		print("\nGood Job! You guessed it on turn {}!").format(turns)
		print("\nGame Over, You Win!!!\n\n\n")
		break
	elif guess > number:
		print("Sorry thats too high.")
	elif guess < number:
		print("Sorry thats too low.")

	turns+= 1
	total_turns = 10 - turns 
	print("You have {} turns remaining.").format(total_turns)

if turns == 10:
	print("\n\nMy number was {}.").format(number)
	print("Game Over. You Lose.\n\n\n\n")
