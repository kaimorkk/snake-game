import random
min=1
max=8
roll_again='y'
while roll_again=='y':
    print('rolling the dices...')
    print('the values are....')
    dice1=random.randint(min,max)
    print('dice1')
    dice2=random.randint(min,max)
    print('dice2')
    roll_again=input('roll the dice again?(y/n):')
