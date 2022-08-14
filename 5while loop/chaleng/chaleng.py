import random
highest = 10
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
gusse = int(input())
if gusse == answer:
    print('you got it first time .')
elif gusse == 0:
    print('exit game')
else:
    while gusse != answer:
        if gusse >= answer:
            print('please guess lower')
        else:
            print('please guess higher')
        gusse = int(input('please enter a new gusse: '))
        if gusse == 0:
            print('exit game')
            break
    else:
        print('your answer is true ')
print ('======================================================')
import random
highest = 10
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
gusse = 0
while gusse != answer:
    gusse = int(input())
    if gusse == 0:
        break
    if gusse == answer:
        print('your answer is true')
    # elif gusse[0] == "":
    elif gusse == "":
        while gusse == '':
            gusse = int(input('please guess a number between 1 to {}: '.format(highest)))
            if gusse != '':
                if gusse > answer:
                    print('please guess lower')
                elif gusse < answer:
                    print('please guess higher')
                else:
                    print('your answer is true ')
    else:
        if gusse > answer:
            print('please guess lower')
        elif gusse < answer:
            print('please guess higher')
        else:
            print('your answer is true ')
print('============================================================')
import random
highest = 10
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
gusse = 0
while gusse != answer:
    gusse = int(input())
    if gusse == 0:
        break
    if gusse > answer:
        print('please guess lower')
    elif gusse < answer:
        print('please guess higher')
    else:
        print('your answer is true ')
print('==============================================================')
import random
highest = 10
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
gusse = 0
while gusse != answer:
    gusse = int(input())
    if gusse == '':
        gusse = int(input('please guess a number between 1 to {}: '.format(highest)))
        while gusse == '':
            gusse = int(input('please guess a number between 1 to {}: '.format(highest)))
    elif gusse == 0:
        break
    else:
        if gusse > answer:
            print('please guess lower')
            gusse = int(input())
        elif gusse < answer:
            print('please guess higher')
            gusse = int(input())
        else:
            print('your answer is true ')
