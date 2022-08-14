a = 'hello '
b = input("what is your name?")
# comment 2 line = ctrl + \
cc = 12
print(type(cc))
sxd = 5
sxd = sxd + 2
sxd += 2
print(a + b)
print(b[2])
g = '1,234,233,576,346,456'
print(g[1::4])
print(g[0::2])
print((a + b + '  ') * 5)
print('a' in b)
print((a + b) + "1\t4\t5\n145")
age = 16
# print('my age is' + age +'years')false
print('my age is' + str(age) + 'years')
print('there are {0} days in, {1}, {2}'.format(31, "march", "may"))
# print("""farvardin: {1}
# mehr: {2}
# esfand: {0}
# khordad: {1}""".format(31, 30, 29))
# moshgel ^
print('my age is %d %s, %d %s' % (age, 'years', 6, 'monts'))
for x in range(1, 12):
    print("no. %2d squared is %4d and cubed is %4d" % (x, x ** 2, x ** 3))
print('pi is approximately %12.50f ' % (22 / 7))
for x in range(1, 12):
    print("no. {0:2} squared is {1:<4} and cubed is {2:4}".format(x, x ** 2, x ** 3))

