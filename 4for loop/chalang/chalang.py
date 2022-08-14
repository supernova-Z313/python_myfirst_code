# input_prompt = "pleas enter your IP address. An IP address consists of 4 number, " \
#                "separates from each other wich a full stop."
input_prompt = ("pleas enter your IP address. An IP address consists of 4 number, "
                "separates from each other with a full stop.")
number = input(input_prompt)
if number[-1] != '.':
    number += '.'
sh = 0
gh = 1
char = ''
for char in number:
    if char == '.':
        print('segment {} contains {} characters'.format(gh, sh))
        gh += 1
        sh = 0
    else:
        sh += 1
fsd = input()
# unless the final character for the string was a then we have not printed the last segment.
# if char != '.':
#     print('segment {} contains {} characters'.format(gh, sh))
