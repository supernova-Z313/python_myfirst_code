
print('please guess a number between 1 and 10: ')
guess = int(input())

if guess < 5:
    print('please guess higher')
    guess = int(input())
    if guess == 5:
        print('well done, you guessed it.')
    else:
        print('sorry, you have not guessed correctly.')
elif guess > 5:
    print('please guess lower')
    guess = int(input())
    if guess == 5:
        print('well done, you guessed it.')
    else:
        print('sorry, you have not guessed correctly.')
else:
    print('you got it first time .')
# 1 ^
print('\n pi baraber {0:12.50} ast'.format(355 / 113))

print('\n please guess a number between 11 and 20: ')
ga = int(input())

if ga != 14:
    if ga > 14:
        print('please guess lower')
    else:
        print('please guess higher')
    gat = int(input())
    if gat == 14:
        print('well done, you guessed it.')
    else:
        print('sorry, you have not guessed correctly.')
else:
    print('you got it first time .')
