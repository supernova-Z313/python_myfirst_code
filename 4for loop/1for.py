for i in range(0, 6):
    print('i is now {}'.format(i))
number = '22,356,785,23,65,955,755,855'
for i in range(0, len(number)):
    print(number[i],end=' ')
number = '22,356,785,23,65,955,755,855'
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i],end='\t')
# number = '22,356,785,23,65,955,755,855'
# nnumber = ''
# for j in range(0 , len(number)):
#     if number[j] in '0123456789':
#         intnumber = nnumber + number[j]
# Nnumber = int(intnumber)
# print('\n the numbers is {}'.format(Nnumber))
number = '22,356,785,23,65,955,755,855'
nnumber = ''
for j in range(0 , len(number)):
    if number[j] in '0123456789':
        nnumber = nnumber + number[j]
Nnumber = int(nnumber)
print('\n the numbers is {}'.format(Nnumber))
# number = '22,356,785,23,65,955,755,855'
# nnumber = ''
# for j in range(0 , len(number)):
#     if number[j] in '0123456789':
#         nnumber = nnumber + number[j]
#     Nnumber = int(nnumber)#1 or 2 tabs not exchang
# print('\n the numbers is {}'.format(Nnumber))
