# DnD Led Dice Roller

This is the Led Dice Roller using Raspberry Pi and Sense Hat kit

<br>
To Download clone this repository and run:
```
git clone https://github.com/maodijim/DnD-Led-Dice-Roller.git
```

<br>
To Run the LED Dice use following command:
```
python3 fun.py
```
Or use daemon program such as PM2 to keep the program running in the background.

<br>

#### Method 1:
1. Use the joystick on Sense Hat to change dice type, there are 6 of them at the moment(d4, d6, d8, d10, d12, d20)
2. shake the device you will see the symbol rotating and the random number showing up

<img src="/dice.gif?raw=true">

#### Method 2:
Run the file using IDE or terminal then enter the dice type you want to roll (4,6,8,10,12,20)

Enter 'dice type di' for disadvantage  EX. '20 di'  will roll d20 twice and output lower number

Enter 'dice type ad' for advantage     EX. '20 ad'  will roll d20 twice and output higher number

<img src="/dice_input.png?raw=true">
