#eXtra code for servo testing

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm= GPIO.PWM(11, 50)

x = 23
#pwmy= GPIO.PWM(3,50)  #ADD TO TOGETHER CODDE pwmy
pwm.start(0)

if x == 0:
    pwm.start(12)
elif x in range(1,55):
    pwm.start(10.8)
elif x in range(56,110):
    pwm.start(9.6)
elif x in range(111,165):
    pwm.start(8.4)
elif x in range(166,220):
    pwm.start(7.2)
elif x in range(221,330):
    pwm.start(6)
elif x in range(331,385):
    pwm.start(5.2)
elif x in range(386,440):
    pwm.start(4.4)
elif x in range(441,495):
    pwm.start(3.6)
elif x in range(496,549):
    pwm.start(2.8)
elif x == 550:
    pwm.start(2)