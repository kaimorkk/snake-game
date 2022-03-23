import random
def welcome_message():
 print('welcome to number guessing game')
 number_to_gauss=random.randint(1,10)
count_number_of_tries =0
gauss=none
gauss=int(input('please gauss a number between 1and 10:'))
while number_to_gauss !=gauss:
    print('sorry wrong number!')
if count_number_of_tries ==10:
    breakpoint()
elif gauss<number_to_gauss:
    print('your gauss is less than the number')
else:
    print('your number was higher than the number')
gauss=int(input('gauss again:'))
count_number_of_tries +=1
if number_to_gauss==gauss:
    print('well done sir')
    print('you took''count_number_of_tries','go to complete the game')
else:
    print('sorry you loose')
    print('the number you needed to gauss was  number_to_gauss')
print('game over')

