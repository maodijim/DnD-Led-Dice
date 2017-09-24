import sys
from sense_hat import SenseHat
import time
from random import randint
sense = SenseHat()

def arrB(turn = False):
    r = (255,0,0)
    w = (0,0,0)
    bl = (105,105,105)
    br = (153,102,51)
    sl = (102,102,153)
    y = (255,177,0)
    image = [
          w,w,y,y,w,w,w,w,
          w,w,bl,w,y,w,w,w,
          w,w,bl,w,w,y,sl,w,
          br,br,br,br,br,y,br,sl,
          w,w,bl,w,w,y,sl,w,
          w,w,bl,w,y,w,w,w,
          w,w,y,y,w,w,w,w,
          w,w,w,w,w,w,w,w
        ]

    sense.set_pixels(image)

    if turn:
        for r in angles:
            sense.set_rotation(r)
            sleep(0.3)

def dragon(turn = False):
    r = (255,0,0)
    w = (0,0,0)
    s = (105,105,105)
    yellow (255,177,0)
    image = [
          w,w,w,s,r,r,r,r,
          w,w,w,s,r,w,r,r,
          w,w,w,s,r,r,r,r,
          w,s,s,s,r,w,w,w,
          r,r,r,r,r,r,r,w,
          w,r,r,r,r,w,w,w,
          w,r,r,r,r,w,w,w,
          w,w,r,w,r,w,w,w
        ]

    sense.set_pixels(image)
    
    if turn:
        for r in angles:
            sense.set_rotation(r)
            sleep(0.3)

def happyFace(turn = False):
    sense.set_pixel(2, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (0, 0, 255))
    sense.set_pixel(3, 4, (105, 105, 105))
    sense.set_pixel(1, 5, (255, 0, 0))
    sense.set_pixel(2, 6, (255, 0, 0))
    sense.set_pixel(3, 6, (255, 0, 0))
    sense.set_pixel(4, 6, (255, 0, 0))
    sense.set_pixel(5, 5, (255, 0, 0))

    if turn:
        for r in angles:
            sense.set_rotation(r)
            sleep(0.3)


    
if sys.argv[1]:
    roll = sys.argv[1]
    sense.set_rotation(180)
    start = time.time()
    while roll and ((start + 60) > time.time()):
        r1 = randint(0,255)
        r2 = randint(0,255)
        r3 = randint(0,255)
        
        sense.show_message(roll, 0.15, text_colour=(r1,r2,r3))

    happyFace()
