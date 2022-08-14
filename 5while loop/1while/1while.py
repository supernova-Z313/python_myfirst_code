i = 0
while i < 10:
    print('i is now {}'.format(i))
    i += 1
print('=========================================')
available_exist = ['east', 'north', 'north east']
chosen_exist = ""
while chosen_exist not in available_exist:
    chosen_exist = input('pleas choose a direction:')
    if chosen_exist == 'quit':
        print('GAME OVER')
        break
else:  # else is not
    print('are not you glad you got out of there')
print('=========================================')
import random
highest = 10
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
ga = int(input())
if ga != answer:
    if ga > answer:
        print('please guess lower')
    else:
        print('please guess higher')
    gat = int(input())
    if gat == answer:
        print('well done, you guessed it.')
    else:
        print('sorry, you have not guessed correctly.')
else:
    print('you got it first time .')
print('=========================================')
