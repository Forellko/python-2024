a = "blood"

# loop for string
for x in a:
  print(x)

# length of string
len(a)

# check string
'oo' in a

# check not in string
'oo' not in a

# slice
a[2:4]

# slice from the start
a[:2]

# slice to the end
a[2:]

# uppercase
a.upper()

# lowercase
a.lower()

# strip remove whitespace
"  blood  ".strip()

# replace
a.replace('b', 'm')

# split
a.split()

# string to array
list(a)

# format
b = "Hello, {0}, age {1}, level {2}"
b.format('world', '26', '3')