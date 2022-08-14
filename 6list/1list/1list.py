ipaddress = input('enter your ipaddress :')
print(ipaddress.count('.'))
print('=======================================')
number = ['3', '2', '5']
number.append('4')
print(number)
print('=======================================')
even = ['2', '0', '4']
odd = ['1', '5', '3', '7']
numbers = odd + even
numbers.sort()
print(numbers)
# sort is not a new list , actualy exchang a list
# print(number.sort()) is false => none
# x = number.sort() is false
print('=======================================')
even = ['2', '0', '4']
odd = ['1', '5', '3', '7']
numbers = odd + even
print(sorted(numbers))
# nnumber = sorted(numbers)
# print(nnumber)
# is sorted make a new things
print('=======================================')
even = ['2', '0', '4']
odd = ['1', '5', '3', '7']
numbers = odd + even
nnumber = sorted(numbers)
print(nnumber)
print('=======================================')
if numbers == nnumber:
    print('true')
else:
    print('false')
# ==
if sorted(numbers) == nnumber:
    print('true')
else:
    print('false')
print('=======================================')
print(min(nnumber))
print(max(nnumber))
xnumber = min(nnumber)
print(xnumber)
print('=======================================')
