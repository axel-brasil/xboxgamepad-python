#!/bin/python3

from time import sleep
from inputs import get_gamepad
import math
import threading

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.LeftJoystickY = 0.0
        self.LeftJoystickX = 0.0
        self.RightJoystickY = 0.0
        self.RightJoystickX = 0.0
        self.LeftTrigger = 0.0
        self.RightTrigger = 0.0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.Menu = 0
        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self): # return the buttons/triggers that you care about in this methode
        left_joystick_x = self.LeftJoystickX
        left_joystick_y = self.LeftJoystickY
        right_joystick_x = self.RightJoystickX
        right_joystick_y = self.RightJoystickY
        a = self.A
        x = self.X
        y = self.Y
        b = self.B
        left  = self.LeftDPad
        right = self.RightDPad
        up    = self.UpDPad 
        down  = self.DownDPad 
        bumber_left  = self.LeftBumper
        bumber_right = self.RightBumper
        trigger_left  = self.LeftTrigger
        trigger_right = self.RightTrigger
        back  = self.Back
        start = self.Start
        menu = self.Menu
        # left joystick:  0
        # right joystick: 1
        # A,X,Y,B:        2
        # DPAD:           3
        # bumps:          4
        # triggers:       5
        # options:        6
        # menu:           7
        return [[left_joystick_x,left_joystick_y], [right_joystick_x,right_joystick_y], [a,x,y,b], [left,up], [bumber_left,bumber_right], [trigger_left,trigger_right], [back,start], [menu]]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                #print(event.code)
                
                # LEFT JOYSTICK
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = float(str(round(event.state / XboxController.MAX_JOY_VAL, 2))[:-1]) # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = float(str(round(event.state / XboxController.MAX_JOY_VAL, 2))[:-1]) # normalize between -1 and 1
                
                # RIGHT JOYSTICK
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = float(str(round(event.state / XboxController.MAX_JOY_VAL, 2))[:-1]) # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = float(str(round(event.state / XboxController.MAX_JOY_VAL, 2))[:-1]) # normalize between -1 and 1
                
                # D-PAD
                elif event.code == "ABS_HAT0X":
                    self.LeftDPad = event.state
                elif event.code == "ABS_HAT0Y":
                    self.UpDPad = event.state
                
                # TRIGGERS
                    # Upper triggers
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                    # Lower triggers
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = round(event.state / XboxController.MAX_TRIG_VAL, 2) # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = round(event.state / XboxController.MAX_TRIG_VAL, 2) # normalize between 0 and 1
              
                # A,X,Y,B BUTTONS
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                
                # MENU BUTTONS
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state

                elif event.code == 'BTN_MODE':
                    self.Menu = event.state

if __name__ == '__main__':
    joy = XboxController()
    while True:
        sleep(0.01)
        print(joy.read())







