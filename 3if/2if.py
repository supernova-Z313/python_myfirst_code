
age = int(input('how old are you ?'))

# #  if age >= 16 and age <= 65:
# or (if (age >= 16) and (age <= 65):)
# or (if 16 <= age > 66: )

if (age <=16) or (age >=66):
    print('enjoy your free time')
else:
    print('have a good day at work ')

#if (some_condition) or (some_weird_function_that_dose_stuff()):
# moshgel ^

# x = 'false'
# if x:
#     print('x is true')
# else:
#     print('x cis not true')

x = input('please enter a text :')
if x:
    print('you entered "{}"'.format(x))
else:
    print('you did not entered anythings')

# print(not false)
# print(not true)

age = int(input('how old are you ?'))
if not (age <= 18):
    print('you are old enough to vote')
else:
    print('please come back in {} years '.format(18 - age))


parrot = 'Norwegian Blue'
letter = input('enter character :')

if letter in parrot :
    print('give me on {},bob'.format(letter))
else:
    print('I donot need that letter')


parrot = 'Norwegian Blue'
letter = input('enter character :')

if letter not in parrot :
    print('I donot need that letter')
else:
    print('give me on {},bob'.format(letter))

a = input('what is your name ?')
b = int(input('how old are you {} ?'.format(a)))
if 18 <= b < 31:
    print('welcome to club 18-30 holiday')
else:
    print('do you not open to club 18-30 holiday')