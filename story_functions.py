from sys import exit

left = ['left','the left','the left path','the path to the left','the left one' ]
right =['2','right','the right','the right path','the path to the right','the right one',
'the correct path','correct path']
accross = ['1','cross the bridge','cross bridge','cross old bridge','cross the old bridge',
'cross anyway']
upstream = ['2','go upstream','follow the river upstream','upstream']
downstream = ['3','downstream','follow the river downstream','follow river downstream',
'I follow the river downstream']
inspect_bridge = ['inspect bridge','Inspect bridge','look at bridge','is it a new bridge',
'is it an old bridge','is the bridge safe','is it safe','is it safe?','is it old']
talk_to_troll = ['talk to troll','talk','3']

def right_path (answer):
    if answer in right:
        print("""Ah, I see you have chosen the right path good for you. This path leads
to a river that has an old bridge accross it.  What do you do.""")
        print("1. Do you cross the bridge and continue on.")
        print("2. Do you follow the river upstream." )
        print("3. Follow the river downstream.")
        answer = input(">")
        old_bridge(answer)
    elif answer in left:
        print("""I see you chose the left path. This is the wrong path for you. You
should go back and choose the correct path.""")
        answer = input("> ")
        right_path(answer)
    else:
        print("""your unwillingness to choose the left or right path path placed
before you is confusing.  You need to sit down, you accidentally stumble and
fall hitting your head on a rock.  You are now unconcious.""")

def old_bridge(answer):
    if answer in accross:
        dead("""Woops wrong choice. The bridge broke and fell apart, you fall into
the river and die.  If only you had inspected the bridge first """)

    elif answer in upstream:
        dead("""You travel upstream and find a lake.  You decide that you would like to
go swimming.  You hop in the water. As you sink to the bottom you suddenly
realize that you never learned how to swim. Your adventure is over.""")

    elif answer in inspect_bridge or answer in downstream:
        print(""" After inspecting this old bridge you don't think it would hold up to well.
You decide that walking downstream is the better option. """)
        print("""While walking down the river you notice another bridge, this one
seems much sturdier.  What do you do. """)

        troll_bridge(answer)
            #if statement for troll bridge
    else:
        print("""your unwillingness to choose the a  path placed
before you is confusing.  You need to sit down, you accidentally stumble and
fall hitting your head on a rock.  You are now unconcious.""")
        print("please try again")
        answer = input("> ")
        old_bridge(answer)
def troll_bridge(answer):
    print("1. Cross this bridge on your left.")
    print("2. Take the path to your right.")
    print("3. Continue downstream.")
    answer = input("> ")
    # possibly a while loop to get second answer. talk = false
    #need to fix while loop should be in inspect_bridge if statement with new
    #function called Troll_language

    if answer in inspect_bridge:
        troll_speak(answer)
        #   New function with while loop
    # downstream answer needs to be in here
    if answer in right:
        print("""Ah what a great adventure this has been.  This path leads
you back to your village.  You managed to stay alive and well.
maybe next time you'll bring some supplies with you to help you on
you journey. """)
#### after your back at the village you can pick up supplies and start again if
#### you want. Fubction village (start) should allow you to go back and get supplies

    elif answer in accross:
        dead("""You really wish you had inspected the bridge.  A troll
jumps out and eats you. Your adventure has ended.""")


    #########elif
    else:
            dead("""your unwillingness to choose the correct path placed
before you is confusing.  You need to sit down, you accidentally stumble and
fall hitting your head on a rock.  You are now unconcious.""")
#    else:
#        print("""You realize you should take the path to your right and any
#other path would be wrong.""")
#        print("""  This path leads you back to your village. Ah what a
#great adventure this has been. You managed to stay alive and well. Maybe next
#time you'll bring some supplies with you to help you on you journey. """)

def troll_speak(answer):
    no_talk = True

    while True:
    #choice = input("> ")
        if answer in inspect_bridge:
            print("""After inspecting the bridge you beleive it will hold your weight.
however you notice a nasty looking troll lurking under it.  Do you 1. Try to
cross anyway. 2. Choose the path that was to your right. 3. try to
talk to the Troll  """)
            answer = input("> ")
            if answer in accross:
                dead("""The troll seems confused at first. It must have thought
that after you saw it you would not cross. He then decides you must also be
confused and he grabs you and eats you. Adventure over. """)

            elif answer in talk_to_troll and no_talk:
#future function for speaking in troll language function could be
# talk_again. talk variable used for  while loop
                print("""you try talking to the troll but it doesn't seem to
understand you because you don't speak troll. Try again.""")
                no_talk = False
                answer = input("> ")
                troll_speak(answer)

  #this gives multiple answers unable to decide answer and dead answers
  #I need a while loop for this one. if false run first talk to troll
  #if true run second print.
        if answer in talk_to_troll or inspect_bridge and not no_talk:
            dead("""This time the troll nods as you speak and waves at you to
come over the bridge.  As the troll grabs you and eats you,
you realize he didn't understand you he just wanted to eat you.""")


def dead(why):
    print(why)
    exit(0)
