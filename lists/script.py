arr = ['Apple', 'Orange', 'Watermelon', 'Melon', 'Strawberry']

arr[1:3] = ['Yammy', 'Nyammy']

arr.insert(2, 'Tomato')

arr.append('Potato')

arr.extend(["Hello", "World"])

arr.remove('Potato')

arr.pop(6)
arr.pop()

for x in arr:
  print(x)

arr2 = [x for x in arr if 'a' in x]