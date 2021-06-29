# YOUR NAME, PARTNER NAME



# monster room- you will need to rename this function.
def monster_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of a monster!")
  print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  # get user input take input()

  if :
    # lead him to the diamond_room()
  elif:
    # the player is dead, call game_over() with "reason"
  else:
    # game_over() with "reason"


# function to ask play again or not
def play_again():
  # use print statement to ask if user wants to play again
  
  # get input

  # evaluate input using conditional 
  if():
  
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
  # have some introductory text printed like: ("\nYou are standing in a dark room.")
  
  # get user input using input() and save 
  answer = input(">").lower()

  # use a loop to manage game -- 

 # if x in input:
    #go to a function()
 # elif "r" in input:
    #go to another function()
  # elif:
    # go somewhere else
  # elif
    # go somewhere else
   else:
    # else go to game over function
    game_over("Don't you know how to type something properly?")


# calling start function. 
start()