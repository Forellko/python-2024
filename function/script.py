def fun(*args):
  print(args)

def fun2(**args):
  print(args)

fun(1,2,3)
fun2(name="Sylas", age=54)