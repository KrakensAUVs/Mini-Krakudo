from robot import Robot

class Control(object):
    """docstring for Controle."""

    def __init__(self, robot):
        super(Control, self).__init__()
        self.robot = robot

    def control_robot(key):
        if key == "w":
            self.robot.forward()
        elif key == "a":
            self.robot.left()
        elif key == "d":
            self.robot.right()
        elif key == "s":
            self.robot.backward()
        elif key == "p": #para
            self.robot.stop()
        elif key == "x":
            pass
