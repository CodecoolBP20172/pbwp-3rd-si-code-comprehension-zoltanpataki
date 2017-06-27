import random  # import random module

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # print 'Hello! What is your name?' on the screen
myName = input()  # Assign a user input to myName variable

number = random.randint(1, 20)  # Assign a random number in between 1 and 20 to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print 'Well, 'the value of myName',I am thinking.....1 and 20 on the screen

while guessesTaken < 6:  # Loop until guessesTaken less than 6 
    print('Take a guess.')  # Print 'Take a guess' on the sreen
    guess = input()  # Assign a user input to guess variable 
    guess = int(guess)  # Convert the value of guess into a number

    guessesTaken += 1  # Add 1 to guessesTaken's previous value

    if guess < number:  # If the user input is less than the random number
        print('Your guess is too low.')  # print 'Your guess is too low' on the screen

    if guess > number:  # If the user input is higher than the random number
        print('Your guess is too high.')  # print 'Your guess is too high' on the screen

    if guess == number:  # If the user input is equal to the random number
        break  # End the loop

if guess == number:  # If the user input is equal to the random number
    guessesTaken = str(guessesTaken)  # Convert the value of guessesTaken into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Print message with myName and guessesTaken variable on the screen

if guess != number:  # If the user input is not equal to the random number
    number = str(number)  # Convert the value of number into a string
    print('Nope. The number I was thinking of was ' + number)  # Print a message with number variable on the screen
