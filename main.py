from robot import Robot
from control import Control

krakudo = Robot()
control = Control(krakudo)
#krakudo.set_motors()

while(True):
    key = input()
    if key == 'w':
        krakudo.forward()
    control.control_robot(key)
