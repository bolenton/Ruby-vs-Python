# Simple text based game, Try to guess the number in 10 times.

puts "\n\nWelcome to the 'Random Number Game!' "
print "What is your name? >>>  "
player = gets
name = player.upcase.chomp

puts "\n\nHello #{name}!, I am thinking of a number between 1 - 100!"
puts "I will give you 10 tries to guess my number, ready? GO!"

number = rand(100) + 1
turns = 0

while turns < 10
	print "\n\nWhat do you think my number is >>> "
	guess = gets.to_i

	if guess == number
		puts "Good Job! You guessed it on turn #{turns}!"
		puts "\nGame Over, You Win!!!\n\n\n"
		break
	elsif guess > number
		puts "Sorry thats too high."
	elsif guess < number
		puts "Sorry thats too low"
	end

	turns = turns + 1
	turns_left = 10 - turns
	puts "You have #{turns_left} turns remaining."
end
 
if turns == 10
	puts "\n\nMy number was #{number}."
	puts "Game Over. You Lose.\n\n\n\n"
end