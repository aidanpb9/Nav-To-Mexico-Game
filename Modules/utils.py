import os
import sys
import time

#checks if terminal is real or pycharm
def in_ide():
    return 'PYCHARM_HOSTED' in os.environ

#clear terminal
def clear():
    if in_ide():
        print("\n" * 50)
    else:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

#prints to terminal slowly
def slow_print(text, delay=0.01, end="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

#to pause text in terminal
def text_buffer():
    input(">")