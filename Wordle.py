import random
import time
import os
import sys
import keyboard

G = "\033[42;30m" # Green
Y = "\033[43;30m" # Yellow
X = "\033[100;30m" # Grey
R = "\033[0m" # Reset

alpha_color = {l: R for l in "QWERTYUIOPASDFGHJKLZXCVBNM"}
def load_words():
    # This finds the actual folder where your script lives
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "5-letter-words.txt")

    try:
        with open(file_path, "r") as f:
            words = [line.strip().upper() for line in f.readlines()]
        return [w for w in words if len(w) == 5]
    except FileNotFoundError:
        print(f"ERROR: Could not find {file_path}")
        input("Press Enter to close...")
        sys.exit()



print(" " * 55 + "WORDLE.PY")

guesses = 0
word_list = load_words()

hidden_word = random.choice(word_list).upper()

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

pool = list(hidden_word)

results = [""] * 5
ail = 7
move = 1
guess = ""
def get_manual_guess():
    global guess, move
    guess = ""

    print(" " * 57, end="", flush=True)
    print(f"\033[H\033[{move}B" + " " * 57, end="")
    move += 1
    while True:

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            # Handle Backspace
            if event.name == 'backspace':
                if len(guess) > 0:
                    guess = guess[:-1]
                    # ANSI: Move back, print space, move back again
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()

            elif event.name == 'enter' and len(guess) == 5:
                if guess in word_list:
                    break


            elif len(event.name) == 1 and event.name.isalpha():
                if len(guess) < 5:
                    char = event.name.upper()
                    guess += char
                    sys.stdout.write(char)
                    sys.stdout.flush()

            if len(guess) > 5:
                guess = guess[:5]
            # Handle Enter (only if length is 5)

def print_alphabet():
    global ail
    print(f"\033[{ail}B")
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    indent = 54

    for row in rows:
        line = " " * indent
        for char in row:
            color = alpha_color[char]
            line += f"{color}{char}{R}"
        print(line)
        indent += 1


    ail -= 1


while True:
    print_alphabet()
    print("", end="")
    pool = list(hidden_word)
    results = [""] * 5
    get_manual_guess()

    guesses += 1
    if guess == hidden_word:
        print("YOU WIN!")
        time.sleep(1000)
        break

    for i in range(5):
        if guess[i] == hidden_word[i]:
            pool[i] = None

            results[i] = "G"


    for b in range(5):
        if results[b] == "G":
            continue

        if guess[b] in pool:
            target_index = pool.index(guess[b])
            pool[target_index] = None

            results[b] = "Y"
        else:

            results[b] = "X"

    formatted_string = ""
    for i in range(5):
        if results[i] == "G":
            color = G
        elif results[i] == "Y":
            color = Y
        else:
            color = X

        for a in range(5):
            char = guess[i]
            res = results[i]
            if res == "G":
                alpha_color[char] = G
            elif res == "Y" and alpha_color[char] != G:
                alpha_color[char] = Y
            elif res == "X" and alpha_color[char] not in [G, Y]:
                alpha_color[char] = X



        formatted_string += color + guess[i] + R

    print("\033[A")
    print(" " * 57 + formatted_string)

    if guesses == 6:
        print(" " * 50 + "The word was " + hidden_word)
        time.sleep(5000)
        break



