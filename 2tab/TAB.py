for i in range(1, 5):
    print(i)
# in {preferences|edit|general|cod...|python} chang no. space

name = input("please enter youre name.")
age = int(input("how old are you, {0} ?".format(name)))

if age >= 18:
    print("you are old enough to vote")
    print("please put an X in the box")
else:
    print("please come back in {0} years".format(18 - age))

input()