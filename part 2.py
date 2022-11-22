import random
import string
import time
def match(code):
    state = 0
    for num in code:
        if state == 0:
            if num == "8":
                state = 1
        elif state == 1:
            if num == "4":
                state = 2
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 2:
            if num == "5":
                state = 34
            elif num == "8":
                state = 1
            else:
                state = 0

        elif state == 34:
            if num == "4":
                state = 44
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 44:
            if num == "4":
                state = 54
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 54:
            if num == "1":
                state = 6
                return ("unlock")
            elif num == "8":
                state = 1
            else:
                state = 0

def crack():
    count = 0
    passcode = True
    st = time.time()
    strin = ""
    while passcode:
        strin += str(random.randrange(10))
        count += 1
        if match(strin) == "unlock":
            print('unlock')
            et = time.time()
            print("Number of symbols generated " + str(count))
            elasped = et - st
            print('Time elasped ' + str(elasped))
            break
crack()
