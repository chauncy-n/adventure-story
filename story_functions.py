from sys import exit

###### after adding number list to choices if statements stopped working correctly
###### also will choose some if statements as a default
# create def nochoice for choice not allowed response(unconcious response)
print("test")
def right_path (answer):
    ### first option in story, only choice to move forward is choosing the "right" path
    correct_path = ["East","east",'the correct path','correct path','the right one','the right path']
    west = ["west","West"]
    if answer in  correct_path:
        print("""Ah, I see you have chosen the right path good for you. This path leads
to a river that has an old bridge accross it.  What do you do.""")
        print("1. Do you cross the bridge to the East and  continue on.")
        print("2. Do you follow the river North upstream." )
        print("3. Follow the river South downstream.")
        answer = input(">")
        old_bridge(answer)
    elif answer in west:
        print("""I see you chose the path to the West path. This is the wrong path for
you. You should go back and choose the correct path.""")
        answer = input("> ")
        right_path(answer)
    else:
        print("""your unwillingness to choose one of the path paths placed
        before you is confusing.  You need to sit down, you accidentally stumble and
        fall hitting your head on a rock.  You are now unconcious.""")

def old_bridge(answer):
    ### 3 choices at old old_bridge upstream and accross call the dead function
    ### downstream continues on story calls troll_bridge. else try again
    accross = ['cross the bridge','cross bridge','cross old bridge','cross the old bridge',
'cross anyway',"1","East","east"]
    upstream = ["north", "North","N","n","2",'go upstream','follow the river upstream','upstream']
    inspect_bridge = ["3",'inspect bridge','Inspect bridge','look at bridge','is it a new bridge',
'is it an old bridge','is the bridge safe','is it safe','is it safe?','is it old',"s","South","south"]

    if answer in accross:
        dead("""Woops wrong choice. The bridge broke and fell apart, you fall into
the river and die.  If only you had inspected the bridge first """)

    elif answer in upstream:
        dead("""You travel upstream and find a lake.  You decide that you would like to
go swimming.  You hop in the water. As you sink to the bottom you suddenly
realize that you never learned how to swim. Your adventure is over.""")

    elif answer in inspect_bridge:
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
    ### 3 questions west takes you back to the village and ends storyself. calls exit for now
    ### accross calls dead function with troll jumping out
    ###downstream is unfinished and suggests trying inspaect bridge reruns troll_bridge
    ###inspect bridge is an unprompted response and calls troll_speak function
    inspect_bridge = ['inspect bridge','Inspect bridge','look at bridge','is it a new bridge',
'is it an old bridge','is the bridge safe','is it safe','is it safe?','is it old']
    accross = ["East","east","E","e","1",'cross the bridge','cross bridge','cross old bridge',
    'cross the old bridge','cross anyway']
    west = ["West","west","W","w","2"]
    downstream = ['downstream','follow the river downstream','follow river downstream',
    'I follow the river downstream',"S","s","South","south","3"]

    print("1. Cross this bridge on the east.")
    print("2. Take the path to the West.")
    print("3. Continue south downstream.")
    answer = input("> ")
    # possibly a while loop to get second answer. talk = false
    #need to fix while loop should be in inspect_bridge if statement with new
    #function called Troll_language

    if answer in inspect_bridge:
        troll_speak(answer)
        #   New function with while loop

    elif answer in west:
        print("""Ah what a great adventure this has been.  This path leads
you back to your village.  You managed to stay alive and well.
maybe next time you'll bring some supplies with you to help you on
you journey. """)
        exit(0)
#### after your back at the village you can pick up supplies and start again if
#### you want. Function village (start) should allow you to go back and get supplies

    elif answer in accross:
        dead("""You really wish you had inspected the bridge.  A troll
jumps out and eats you. Your adventure has ended.""")

    elif answer in downstream:
            print("""I'm sorry I haven't thought this far ahead yet. Instead
you decide to take the path to your West.""")
            print("""Ah what a great adventure this has been.  This path leads
you back to your village.  You managed to stay alive and well.
maybe next time you'll bring some supplies with you to help you on
you journey. """)
            exit(0)
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
    #choice = input("> ")
    # while loop not working correctly, if answer 2 is chosen it loops still
    inspect_bridge = ['inspect bridge','Inspect bridge','look at bridge','is it a new bridge',
    'is it an old bridge','is the bridge safe','is it safe','is it safe?','is it old']
    across =  ['cross the bridge','cross bridge','cross old bridge','cross the old bridge',
    'cross anyway','one']
    talk_to_troll = ['talk to troll','talk','3']
    west = ["west","West","2"]
    downstream = ['downstream','follow the river downstream','follow river downstream',
    'I follow the river downstream']
    if answer in inspect_bridge:
        while no_talk == True:
            print("""After inspecting the bridge you beleive it will hold your weight.
however you notice a nasty looking troll lurking under it.  Do you 1. Try to
cross anyway. 2. Choose the path to the West. 3. try to talk to the Troll  """)
            answer = input("> ")
            if answer in accross:
                dead("""The troll seems confused at first. It must have thought
that after you saw it you would not cross. He then decides you must also be
confused and he grabs you and eats you. Adventure over. """)

            elif answer in talk_to_troll and no_talk:
#future function for speaking in troll language function could be
# talk_again. talk variable used for  while loop
                print("""you try talking to the troll but it doesn't seem to
understand you because you don't speak troll. Do you 1. Try to
cross anyway. 2. Choose the path to the West. 3. try to
talk to the Troll again  .""")
                no_talk == False
                answer = input("> ")
                troll_speak(answer)
    elif answer in west:
        print("""Ah what a great adventure this has been.  This path leads
you back to your village.  You managed to stay alive and well.
maybe next time you'll bring some supplies with you to help you on
you journey. """)
        exit(0)
  #this gives multiple answers unable to decide answer and dead answers
  #I need a while loop for this one. if false run first talk to troll
  #if true run second print.
    elif answer in downstream:
        print("""I'm sorry I haven't thought this far ahead yet. Instead
you decide to take the path to the West.""")
        print("""Ah what a great adventure this has been.  This path leads
you back to your village.  You managed to stay alive and well.
maybe next time you'll bring some supplies with you to help you on
you journey. """)
        exit(0)

    if answer in talk_to_troll or inspect_bridge and not no_talk:
        dead("""This time the troll nods as you speak and waves at you to
come over the bridge.  As the troll grabs you and eats you,
you realize he didn't understand you he just wanted to eat you.""")



def dead(why):
    print(why)
    exit(0)
