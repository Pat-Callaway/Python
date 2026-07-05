# Testing out ideas for a basic text based adventure
import time

opening_text = "This world isn't what it seems... dont believe everything you see..."

for char in opening_text:
    print(char, end="", flush=True)
    time.sleep(0.1)