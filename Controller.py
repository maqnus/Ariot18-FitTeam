import pyvjoy
import sys
import datetime
import time

# input1 = sys.argv[1]
# input2 = sys.argv[2]
# print(datetime.datetime.now())
# print(input1)

# #Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

# #turn button number 15 on
# j.set_button(int(input1),int(input2))

# time.sleep(0.2);
# j.reset_buttons()

def playerinput(player, button, state, height):
    value = 0
    if(int(state) < (height/2)):
        value = 1
        print(player, button, state)
    
    pyvjoy.VJoyDevice(player).set_button(int(button), value)
    # print(player, button, value)
    return;