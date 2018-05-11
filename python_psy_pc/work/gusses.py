#This is a simple game program
#Programmed by pengshiyu
import random
guesses_made=0
name=raw_input('Hello! what is your name?\n')

number=random.randint(1,20)
print 'well,{0},i am thinking of a number between 1 and 20.'.format(name)

while guesses_made <6:
    guess=int(raw_input('Take a guess:'))
    guesses_made +=1
    
    if guess <number:
        print 'your guess is too low'
    if guess >number:
        print 'your guess is to high'
    if guess==number:
        break
if guess==number:
    print'good job,{0}!you guessed my number in {1} guesses!'.format(name,guesses_made)
else:
    print 'nope,the number i was thinking was {0}'.format(number)


