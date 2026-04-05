import random 
number=random.randint(1,100)

lives=5
count=0
numberOfHints=1

if number%2==0:
    hint='even'
else:
    hint='odd'

while lives>0:
    lives-=1
    count+=1
    guess=input('enter your guess: ')

    if not guess.isdigit():
        print('Please enter a valid number.')
        lives += 1
        count -= 1
        continue
    if int(guess)==number:
        print('Congrats! You found the number in '+' '+str(count)+'.'+' tries!')
    elif int(guess)<number:
        print('go up')
        if (int(numberOfHints)>0):
             askHint=input('Would you like to have a hint? ')
             if askHint=='yes':
                 print(hint)
                 numberOfHints-=1
    else:
        print('go down')
        if (int(numberOfHints)>0):
             askHint2=input('Would you like to have a hint? ')
        if askHint2=='yes':
            print(hint)
            numberOfHints-=1
    if lives==0:
        print('You are out of lives :( The number was '+str(number))
        break
