'''
Ben Lepsch
Scrolls the road function for Owen and Luca's MSP.py
'''

import time

sand = ['..  .   .   ',' .   .     .','.  . ..  .  ','  ..  .   ..']
road = ['/\\', '/  \\', '/    \\', '/      \\']

def print_end():
  print(" ____  _   _  ____    ____  _  _  ____")
  print("(_  _)( )_( )( ___)  ( ___)( \( )(  _ \\")
  print("  )(   ) _ (  )__)    )__)  )  (  )(_) )")
  print(" (__) (_) (_)(____)  (____)(_)\_)(____/")
  print("_________________________________________")

def print_road(i):
  print_string = ''
  print_end()
  for x in range(len(road)):
    while i >= 4:
      i -= 4
    print_string = (' '*(4-x)) + sand[i] + road[x] + sand[i]
    print(print_string)
    print_string = ''
    i = i - 1
  time.sleep(0.25)
  print('\n'*50)


for i in range(1000):
  print_road(i)
