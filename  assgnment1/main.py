num=int(input('enter a value:'))
if num>1:
    for i in range(2,num//2):
        if (num%i)==0:
            print('not prime')
    else:
            print('😇')