print('π΄happy birthday claudiaπ΄')
import time
from random import randint
for i in range(1,65):
    print('')
space=''
for i in range(1,800):
    count=randint(1,100)
    while(count > 0):
        space +=' '
        count -=1
    if(i%10==0):
        print(space + 'π'"happy birthday claudia!"'π')
    elif(i%8==0):
        print(space +'ππ' "kevglow" 'ππ')
    elif(i%7==0):
        print(space +'π'*10)
    elif(i%6==0):
        print(space +"gro to glow")
    elif(i%4==0):
        print(space +"π₯""happy birthday sweetheart" 'π₯')
    space=''
    time.sleep(0.3)



