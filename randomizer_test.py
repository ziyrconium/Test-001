import random
import keyboard
import time
import os

start = True
running = False
word = None
end_prog = False

def run_program():
    global running, word
    running = not running
    if not running:
        print(f"YOU GOT : {word}")
        print("\nPress 'Space' key to start and stop randomizing...")
        print("Press 'X' to end program...")

def stop_program():
    global end_prog
    end_prog = not end_prog

keyboard.add_hotkey('space', run_program)
keyboard.add_hotkey('X', stop_program)

print("Press 'Space' key to start and stop randomizing...")
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