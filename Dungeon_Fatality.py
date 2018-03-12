from sys import exit

#This array keeps track of various things that get turned on throughout the game
#the zeroeth slot is if the person found the wings
#the first slot is if the person found the gun
#the second slot is if the person found the gold answer
#the third slot is if the person found honey
#the fourth slot says if the game needs to load it's title.  we only want to do that once
#the fifth slot says if the nazi is alive or a zombie
#the sixth slot says if you have used the wings successfully
#the seventh slot says if you have used the honey successfully
inv =  {'wings' : 0, 'gun' : 0, 'gold_ans' : 0, 'honey' : 0, 'title' : 0, 'nazi_dead' : 0, 'wings_used' : 0, 'happy_bear':0}

def gold():
  print("This room is full of gold.  How many pieces do you take?")

  choice = input("> ")
  if RepInt(choice):
    how_much = int(choice)
  else:
    dead("The Sphinx shuts the door... you can't get out.")

  if how_much == 323:
    if inv['gold_ans'] == 1:
      print("You win!  Don't spend it all in one place!")
      exit(0)
    else:
      print("Lucky...but you probably cheated.  I'll give you double gold and take 14 years off your life.")
      exit(0)
  else:
    dead("The Sphinx shuts the door... you can't get out.")

def RepInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def bear():
  print("There is a bear here.")
  print("Maybe we should run!  What do you do?")
  choice = input("> ")

  if choice == "run" and inv['happy_bear'] == 0:
    gun()
  elif choice == "run" and inv['happy_bear'] ==1:
    dead("You tripped.  The bear shares some honey with you.  That's nice.  You die of diabetes.")
  elif choice == "honey" and inv['honey'] == 1:
    inv['happy_bear'] = 1
    print("The bear is enjoying some of your honey.")
    print("Would you like to go forward or back?")
    choice2 = input("> ")
    if choice2 == "back":
      gun()
    elif choice2 == "forward":
      sphinx()
    else:
      dead("The bear finished the honey.  You were a tasty desert.")
  else:
    dead("Don't be mad.  Bears gotta eat too.")

def boring():
    print("This room is really boring.  Don't designers put in any effort at all?")
    print("Go forward or back?")
    job = input("> ")
    if job == "back":
      start()
    elif job == "forward":
      wings()
    else:
        dead("You had one job!  For no apparent reason...")

def nazi():
  if inv['nazi_dead'] == 0:
    print("There's a Nazi!  Maybe we should run!")
  else:
    print("There's a zombie Nazi!")
  choice = input("> ")

  if choice == "run" and inv['nazi_dead'] == 0:
    start()
  elif choice == "run" and inv['nazi_dead'] == 1:
    dead("He's a zombie.  He caught you!")
  elif choice == "gun" and inv['gun'] == 1:
    print("Nice shot!")
    inv['nazi_dead'] == 1
    print("Go forward or back?")
    choice2 = input("> ")
    if choice2 == "forward":
      honey()
    elif choice2 == "back":
      start()
    else:
      dead("Dallying...Did you forget Nazi Zombies?")
  else:
    dead("Good try!  He shoots you.")

def honey():
  if inv['honey']==0:
    print("MMMMM some honey.  If a good time to use it arises type 'honey'.")
    inv['honey'] = 1
  else:
    print("This was the room with honey.")
  print("Go forward or back?")
  choice = input("> ")
  if choice == "forward":
    gold_answer()
  elif choice == "back":
    nazi()
  else:
    dead("GIANT SPIDER!")

def gold_answer():
  print("The wall has writing scrawled on it.  '323'.")
  inv['gold_ans'] = 1
  print("There's no where to go but backwards.  The door was there but now it's gone.")
  print("You panic and swoon.  What's happening??  The room around you transforms.")
  start()

def wings():
  if inv['wings'] == 0:
    print("Hm some make shift wings.  If a good time to use them arises type 'wings'.")
    inv['wings'] = 1
  else:
    print("This was the room with the wings.")
  print("Go forward or back?")
  choice = input("> ")
  if choice == "back":
    boring()
  elif choice == "forward":
    fake_gold()
  else:
    dead("The air is getting...thin?  I can't breathe!")

def fake_gold():
  print("It's here!  The gold....wait.  Not it's shiny guano")
  print("Go forward or back?")
  choice = input("> ")
  if choice == "back":
    wings()
  elif choice == "forward":
    pit2()
  else:
    print("Bats are nice.  Bet you expected them to kill you.")
    dead("The floor is shifting.  You're 14.5 feet deep in bat poop...that's rough buddy.")

def pit2():
  print("Another pit?  Wait have you seen the first pit?  Whatever.  We should run!")
  choice = input("> ")
  if choice == "run" and inv['wings_used'] == 0:
    fake_gold()
  elif choice == "run" and inv['wings_used'] == 1:
    dead("You slipped and broke your neck!")
  elif choice == "wings" and inv['wings'] == 1:
    print("Yay!  You can fly.  Go forward or back?")
    inv['wings_used'] = 1
    choice2 = input("> ")
    if choice2 == "forward":
      riddle_answer()
    elif choice2 == "back":
      fake_gold()
    else:
      print("Secret win con!!  What's my favorite number?")
      choice3 = input("> ")
      if choice3 == "317":
        print("What does your heart desire?")
        choice4 = input("> ")
        print(f"You may have {choice4} and 5000000 gold pieces!")
      else:
        print("Wrong!  You flew to close to the sun.  Disintigration!")
  else:
    dead("The pit expands and something very similar to a Sarlaac eats you.  Not a Sarlaac because that's copyrited but something very similar.")

def pit():
  print("Another pit?  Wait have you seen the first pit?  Whatever.  We should run!")
  choice = input("> ")
  if choice == "run" and inv['wings_used'] == 0:
    start()
  elif choice == "run" and inv['wings_used'] == 1:
    dead("You slip and fall, breaking your tibia.  You'd rather not live without a functioning tibia, so you welcome death.")
  elif choice == "wings" and inv['wings']==1:
    print("Yay!  You can fly.  Go forward or back?")
    inv['wings_used'] = 1
    choice2 = input("> ")
    if choice2 == "forward":
      gun()
    elif choice2 == "back":
      start()
    else:
      dead("It starts to storm.  RIDE THE LIGHTNING")
  else:
    dead("You fall into the pit.  Hey you didn't die!  It's wet down here.  Is that blood?  A werewolf bites your neck.")

def gun():
  if inv['gun'] == 0:
    print("Alright a gun!  If a good time to use it arises type 'gun'.")
    inv['gun'] = 1
  else:
    print("This is the room in which you found the gun.")
  print("Go back or forward?")
  choice = input("> ")
  if choice == "back":
    pit()
  elif choice == "forward":
    bear()
  else:
    dead("I'm not morbid enough for this.  You know what?  You live.  Just kidding.  Eaten by squirrels.")

def sphinx():
  print("A sphinx screams at you in an incomprehensible way.  We should run!  Why are you still in this horrible place?")
  choice = input("> ")
  if choice == "run":
    bear()
  elif choice == "green":
    print("The sphinx moves aside and bows to you.  It's really not such a mean critter.")
    print("Go forward?")
    choice2 = input("> ")
    if choice2 == "forward":
      gold()
    else:
      dead("The sphinx is offended by you refusing her gift.  She eats you.")
  else:
    dead("The sphinx stares in horror mouth agape.  Silence.  You wonder, what you could have done instead.  Slowly you both turn to stone.")

def riddle_answer():
  print("Blood stains the wall.  It is shaped into words.  \n'I have deciphered her language.  I have answered her riddle, but bone vampires ate my pelvis.  \nWith my last blood I tell you the answer is 'green'.")
  print("The door behind you slams shut!  You spy a trap door; trap door or chill out?")
  choice = input("> ")
  if choice == "trap door":
    start()
  else:
    dead("Bone vampires eat your pelvis.  You obscure the other guy's message as you die...way to ruin it for everyone.")

def dead(why):
  print(why, "You Died!")
  exit(0)

def start():
  if inv['title'] == 0:
    inv['title'] = 1
    print("DUNGEON FATALITY!")
    print("We say forward to mean away from the starting room.  We say back to mean towards the starting room.")
  print("You are in a room.  What a pretty arrangement of skulls they have!")
  print("There are doors to your right, left, and straight.")
  print("Which one do you take?")

  choice = input("> ")

  if choice == "left":
    nazi()
  elif choice == "right":
    boring()
  elif choice == "straight":
    pit()
  else:
    dead("You feel a stream of finely mashed avocado cascade onto you. \nYou turn around to see a Hipster Dragon is preparing you for dinner. \nYou both get eaten by a bigger dragon who hates avocado.")

start()
