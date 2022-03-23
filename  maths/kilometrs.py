kilometers=int(input('enter the value in kilometers:'))
if(kilometers>=0):
    print('positive number')
else:
    print('negative number')

miles=kilometers/1.654
print(kilometers,"km converts to",miles,'miles')
