import random
import keyboard
import time
import os

start = True
running = False
word = None
end_prog = False
clear_terminal = False

def run_program():
    global running, word
    running = not running
    if not running:
        print(f"\nYOU GOT : {word}")
        print("\nPress 'Space' key to start and stop randomizing...")
        print("Press 'C' to clear terminal...")
        print("Press 'X' to end program...")

def reset_terminal():
    global clear_terminal
    clear_terminal = not clear_terminal
    if clear_terminal:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Press 'Space' key to start and stop randomizing...")
        print("Press 'C' to clear terminal...")
        print("Press 'X' to end program...")


def stop_program():
    global end_prog
    end_prog = not end_prog

keyboard.add_hotkey('space', run_program)
keyboard.add_hotkey('X', stop_program)
keyboard.add_hotkey('C', reset_terminal)

print("Press 'Space' key to start and stop randomizing...")
print("Press 'C' to clear terminal...")
print("Press 'X' to end program...")

while start:
    if running:
        word = random.choices(["TRUE", "FALSE"])[0]
        print(word)
    elif end_prog:
        print("Stopping Program...")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        start = not start 