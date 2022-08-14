shoping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shoping_list:
    if item == 'spam':
        print('i am ignoring' + item)
        continue
    print('buy ' + item)
print('================================')
# shoping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shoping_list:
    if item == 'spam':
        # print('i am ignoring' + item)
        break
    print('buy' + item)
print('===============================')
meal = ['eggs', 'bacon', 'spam', 'sausages']
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
if nasty_food_item:
    print('can not I have anythings without apam in it')
print('===============================')
foods = ['eggs', 'bacon', 'tomato', 'sausages']
nasty_food_item = ''
for item in foods:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print('I have a plate of that, then, please')
if nasty_food_item:
    print('can not I have anythings without apam in it')
print('================================')
