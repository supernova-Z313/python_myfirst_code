number = '22,356,785,23,65,955,755,855'
num = ''
for char in number:
    if char in '0123456789':
        num = num + char
total = int(num)
print("number is {}".format(total))
print('=============================')
for state in ['no pinin','no more','a stiff','bereft of life']:
    print('this parrot is ' + state)
    #print('this parrot is {}'.format(state))
print('================================')
for j in range(0, 105, 5):
    print('j is {} ~'.format(j),end='\t')
print('\n =============================')
for x in range(0, 13):
    for y in range(0, 13):
        print('{0:2} times {1:2} is {2:3}   |'.format(x, y, x*y),end='\t')
    # print(end='\n''---------------------------------------------------')
    print('')
print('================================')
number = '22,356,785,23,65,955,755,855'
kuf = ''
for char in number:
    if char in '0123456789':
        kuf += char
juf = int(kuf)
print('number is {}'.format(juf))
x = 23
x += 1
print(x)
x -= 4
print(x,end='\t')
x *= 5
print(x,end='\t')
x /= 4
print(x,end='\t')
x **= 2
print(x,end='\t')
x %= 60
print(x,)
greeting = 'good'
greeting += 'morning'
print(greeting)
greeting *=5
print(greeting)
# +=  , -=  , /=  , *=  , %=  , **=  , <<=  , >>=  , &=  , ^=  , |=


