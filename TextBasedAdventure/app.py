# Testing out ideas for a basic text based adventure
import time

opening_text = "This world isn't what it seems... dont believe everything you see..."

for char in opening_text:
    print(char, end="", flush=True)
    time.sleep(0.1)
print("Narrator: You wake up in a dark room. You do not recognize anything here, yet it is strangely familiar...")
print("Narrator: Are you going to investigate or just keep laying around?")
options = ["Investigate", "Keep laying around"]
user_input = input(">> ")

if user_input == "Investigate":
    print("Narrator: You decide to investigate... Good for you. In the room you see a nightstand, a desk, and a door.")
    print("Narrator: What are you going to investigate?")
    options = ["Nightstand", "Desk", "Door"]
    user_input = input(">> ")
    if user_input == "Nightstand":
        print("Narrator: You find a nightstand. It is empty.")
    elif user_input == "Desk":
        print("Narrator: You find a desk. It is empty.")
    elif user_input == "Door":
         print("Narrator: You find a door. Open it!")

else:
    print("Narrator: You decide to keep laying around. So lazy, and I won't let you ruin this adventure. Get up!")