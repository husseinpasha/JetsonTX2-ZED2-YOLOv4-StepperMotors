# This file is same as the Multi_Steppers.py file.
#  The differenc is that it made the whole file a one funtion
#  and at the end the function is called. 
# Later I need to call the funtion from another file

import concurrent.futures
import RPi.GPIO as GPIO
import time

def motion(X, Y, Z):
    pul_val_1 = X
    pul_val_2 = Y
    pul_val_3 = Z

    # pul_val_1 = 0
    dir_val_1 = GPIO.HIGH

    # pul_val_2 = 1000
    dir_val_2 = GPIO.LOW

    # pul_val_3 = 1000
    dir_val_3 = GPIO.HIGH


    Pul_1 = 11
    Dir_1 = 15
    Pul_2 = 22
    Dir_2 = 31
    Pul_3 = 37
    Dir_3 = 38 #regular pin, needs transistor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Pul_1, GPIO.OUT)
    GPIO.setup(Dir_1, GPIO.OUT)
    GPIO.setup(Pul_2, GPIO.OUT)
    GPIO.setup(Dir_2, GPIO.OUT)
    GPIO.setup(Pul_3, GPIO.OUT)
    GPIO.setup(Dir_3, GPIO.OUT)
    delay = 0.00001

    def motor_1(pul_val_1, dir_val_1):
        curr_val_1 = GPIO.HIGH
        GPIO.output(Dir_1, dir_val_1)

        while pul_val_1 !=0 :
            GPIO.output(Pul_1, curr_val_1)
            curr_val_1 ^= GPIO.HIGH
            time.sleep(delay)
            pul_val_1 -= 1


    def motor_2(pul_val_2, dir_val_2):
        curr_val_2 = GPIO.HIGH
        GPIO.output(Dir_2, dir_val_2)

        while pul_val_2 !=0 :
            GPIO.output(Pul_2, curr_val_2)
            curr_val_2 ^= GPIO.HIGH
            time.sleep(delay)
            pul_val_2 -= 1


    def motor_3(pul_val_3, dir_val_3):
        curr_val_3 = GPIO.HIGH
        GPIO.output(Dir_3, dir_val_3)

        while pul_val_3 !=0 :
            GPIO.output(Pul_3, curr_val_3)
            curr_val_3 ^= GPIO.HIGH
            time.sleep(delay)
            pul_val_3 -= 1




    with concurrent.futures.ProcessPoolExecutor() as executor:
            f1 = executor.submit(motor_1, pul_val_1, dir_val_1)
            f2 = executor.submit(motor_2, pul_val_2, dir_val_2)
            f3 = executor.submit(motor_3, pul_val_3, dir_val_3)
