x = 5

def fun():
  global x
  x = 3

def fun2():
  x = 4

fun()
fun2()

print(x)