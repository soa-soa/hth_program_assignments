# Sophia Huang, 

def start():
    print("Oh no! You're late to school! (pre-pandemic era, please bare with me)")
    print("What do you do? (1 or 2)")
    print("1. Go back to sleep, this is all a dream.")
    print("2. You better get up. Get ready STAT.")
    first_input = input(">")
    if first_input == str(1):
        print("1. Go back to sleep, this is all a dream.")
        sleeping()
    else:
        print("2. You better get up. Get ready STAT.")
        getting_ready()
        

def sleeping():
    print("Too bad, your conscience guilts you into waking up. You have no choice")
    print("Your're awake now. You should do something (1 or 2)")
    print("1. Go brush your teeth. You got morning breath :/")
    print("2. Who cares about hygiene? You got to finish that homeowrk assignment that you've been putting off >:( Your past self must dislike you.")
    sleeping_input = input(">")
    if sleeping_input == str(1):
        print("1. Go brush your teeth. You got morning breath :/")
        
    else:
        print("2. Who cares about hygiene? You got to finish that homeowrk assignment that you've been putting off >:( Your past self must dislike you.")

def getting_ready():
    print("Alright alright. You freshen up and go outside")
    print("The beings above must not like you today because a horde of unicorns is blocking your way.")
    print("What do you do?(Choose option 1 or 2)")
    print("1. Politely ask them if they can make way for you. Education is very important")
    print("2. It's a signal! Ride one of the unicorns to run away from life")
    getting_ready_input = input(">")
    if getting_ready_input == str(1):
        print("What a gentle-person. The unicorns make way for you")
        horseshoe()
    else:
        print("You asked a unicorn if they could help you escape to freedom. The unicorn said 'Hop on!'")
        runaway_unicorn()

def horseshoe():
    print("but not without giving you a horseshoe")
    print("what do you do with the horseshoe? (1 or 2)")
    print("1. Erm yay? You got a horseshoe? Maybe it's a lucky charm, take it with you.")
    print("2. Ew what IS that? You don't know where it has been. ")

def runaway_unicorn():
    print("Both of you fly up and up into the sky!")
    print("sIKE! The unicorn knew you were skipping school.")
    print("Shame on you")
    print("In an instant you appear at school.")

start()