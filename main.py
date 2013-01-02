
### Instaead, could I do something like:

##while type (guess) not int:

###Check my character creator program. How did I handle the problem there?


def requireInt ():
    'Creates a try loop until program receives an integer.'
    rawGuess = str(raw_input ("\nTake a guess: ")) ### I thought I needed to make \
##    the input a string first, because otherwise it generates a name error if you
##    enter text without quotes. But maybe there's a more elegant way around this?
    try: guess = int (rawGuess)
    except:
        print 'Please enter only numbers.'
        guess = str(raw_input ("\nTake a guess: ")) ### I bet there's a more
##        elegant way to loop back to the input prompt.
    return guess




import random
print("\tWelcome to 'Number Guessing Game'")
print("The number is between 1 and 50, try to guess it in the fewest possible guesses")
trueNumber = random.randint(1, 50)


guess = requireInt()

tries = 1
while guess != trueNumber:
    if guess > trueNumber:
        print("To High! Guess lower...") ### Debugging: This error message always \
##        appears if the penultimate guess was not an integer. Why?
    else:
        print("Too low! Guess higher...")

    guess = requireInt()

    tries += 1

print("You guessed it! You got my number in", tries, "tries")
print("The number was", trueNumber)




    
