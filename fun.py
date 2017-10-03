from sense_hat import SenseHat
from time import sleep
from random import randint
import sys
from subprocess import Popen
import threading

sense = SenseHat()
default_rotation = 0
menu = ['4','6','8', '10','12','20']
angles = [180, 270, 0, 90, 180, 270, 0, 90, 180]
current_position = 1

def arrB(turn = True):
    r = (255,0,0)
    w = (0,0,0)
    bl = (0,51,102)
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
            sleep(0.1)

def dragon(turn = True):
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
            sleep(0.1)

def happyFace(turn = True):
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
            sleep(0.1)

def rollDice(message, printDice = True, extra = None):
    message_arr = message.split(' ')
    message = message_arr[0]
    sec_roll = None
    if message == 'd20' or message == '20':
        roll = randint(1,20)
    elif message == 'd12' or message == '12':
        roll = randint(1,12)
    elif message == 'd8' or message == '8':
        roll = randint(1,8)
    elif message == 'd10' or message == '10':
        roll = randint(1,10)
    elif message == 'd6' or message == '6':
        roll = randint(1,6)
    elif message == 'd4' or message == '4':
        roll = randint(1,4)
    else:
        roll = 'Error'

    # Handling disadvantage and advantage roll
    if extra == 'di':  # roll in disadvantage
        print('first roll: ' + str(roll))
        if message == 'd20' or message == '20':
            sec_roll = randint(1,20)
            if(sec_roll < roll):
                roll = sec_roll
        elif message == 'd12' or message == '12':
            sec_roll = randint(1,12)
            if(sec_roll < roll):
                roll = sec_roll
        elif message == 'd8' or message == '8':
            sec_roll = randint(1,8)
            if(sec_roll < roll):
                roll = sec_roll
        elif message == 'd10' or message == '10':
            sec_roll = randint(1,10)
            if(sec_roll < roll):
                roll = sec_roll
        elif message == 'd6' or message == '6':
            sec_roll = randint(1,6)
            if(sec_roll < roll):
                roll = sec_roll
        elif message == 'd4' or message == '4':
            sec_roll = randint(1,4)
            if(sec_roll < roll):
                roll = sec_roll
    elif extra == 'ad':     #roll in advantage
        print('first roll: ' + str(roll))
        if message == 'd20' or message == '20':
            sec_roll = randint(1,20)
            if(sec_roll > roll):
                roll = sec_roll
        elif message == 'd12' or message == '12':
            sec_roll = randint(1,12)
            if(sec_roll > roll):
                roll = sec_roll
        elif message == 'd8' or message == '8':
            sec_roll = randint(1,8)
            if(sec_roll > roll):
                roll = sec_roll
        elif message == 'd10' or message == '10':
            sec_roll = randint(1,10)
            if(sec_roll > roll):
                roll = sec_roll
        elif message == 'd6' or message == '6':
            sec_roll = randint(1,6)
            if(sec_roll > roll):
                roll = sec_roll
        elif message == 'd4' or message == '4':
            sec_roll = randint(1,4)
            if(sec_roll > roll):
                roll = sec_roll

    if sec_roll:
        print('sec roll:' + str(sec_roll))

    if printDice:
        print('roll: ' + str(roll))


    return str(roll)

def inputMessage(e,message = None,process = None):
    try:
        if not message:
            message = input('Type of dice (type "q" to quit):')
        if message == 'q':
            if process:
                process.kill()
            sense.show_message('')
            e.set()
            raise ValueError('Program Exit')
        elif 'di' in message:
            arrB()
            roll = rollDice(message, True, 'di')
            process = Popen(['python3', './fun1.py', roll])
            message = input('Type of dice (type "q" to quit):')
            process.kill()
            sense.show_message('')
            happyFace(False)
            inputMessage(e, message, process)
        elif 'ad' in message:
            arrB()
            roll = rollDice(message, True, 'ad')
            process = Popen(['python3', './fun1.py', roll])
            message = input('Type of dice (type "q" to quit):')
            process.kill()
            sense.show_message('')
            happyFace(False)
            inputMessage(e, message, process)
        else:
            arrB()
            roll = rollDice(message)
            process = Popen(['python3', './fun1.py', roll])
            message = input('Type of dice (type "q" to quit):')
            process.kill()
            sense.show_message('')
            happyFace(False)
            inputMessage(e, message, process)
    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        print('exception')
        inputMessage()

def joystick(e):
    global current_position
    sense.set_rotation(default_rotation)
    idle = False
    while not e.isSet():
        event = sense.stick.wait_for_event()
        if event.direction == 'up' and (event.action == 'pressed' or event.action == 'held'):
            idle = False
            if current_position < len(menu):
                current_position += 1
            sense.set_rotation(0)
            sense.show_message(menu[current_position-1], 0.05, text_colour=(200,200,200))
        elif event.direction == 'down' and (event.action == 'pressed' or event.action == 'held'):
            idle = False
            if current_position > 1:
                current_position -= 1
            sense.set_rotation(0)
            sense.show_message(menu[current_position-1], 0.05, text_colour=(200,200,200))
        elif event.direction == 'middle' and event.action == 'held':
            idle = True
            sense.show_letter(' ')
        if not idle:
            happyFace(False)

def movementDetec(e):
    x = round(sense.get_accelerometer_raw()['x'], 2)
    y = round(sense.get_accelerometer_raw()['y'], 2)
    z = round(sense.get_accelerometer_raw()['z'], 2)
    threshold = 0.80
    while not e.isSet():
        acceleration = sense.get_accelerometer_raw()
        x_tmp = round(acceleration['x'],2)
        y_tmp = round(acceleration['y'],2)
        z_tmp = round(acceleration['z'],2)

        if abs(x_tmp - x) > threshold or abs(y_tmp - y) > threshold or abs(z_tmp - z) > threshold:
            roll = rollDice(menu[current_position-1],False)
            arrB()
            for i in range(3):
                sense.show_message(roll, 0.08,text_colour=(200,200,200))
            happyFace(False)
            sleep(3)
        x = x_tmp
        y = y_tmp
        z = z_tmp


if __name__ == '__main__':
    arrB(False)
    #happyFace(False)
    threads = []
    e = threading.Event()
    t1 = threading.Thread(target=inputMessage, args=(e,))
    threads.append(t1)
    t2 = threading.Thread(target=joystick, args=(e,))
    threads.append(t2)
    t3 = threading.Thread(target=movementDetec, args=(e,))
    threads.append(t3)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    sense.show_letter(' ')
