import keyboard

def hello():
  print('hello')

keyboard.add_hotkey('a', hello)
keyboard.wait('c')