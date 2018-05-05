from items import *
world = [[-1 for y in range (50)] for x in range(50)]
hp = 100
hunger = 100
x = 25
y = 25
world[x][y] = [Sword(25, 2, "beginner's sword"), Axe(25, 1, "beginner's axe"), Food(10, "bread"), HPbottle(10)]
slotA = None
slotB = None

seen = False

def see():
    text = "There is"
    if world[x][y] == None:
        text += " nothing"
    else:
        for i in world[x][y]:
            text += " a " + i.name + ","
    text = text[:-1] + " here"
    print text

on = True
while on:
    if not seen:
        see()
        seen = True

    response = raw_input("What would you like to do?\n")

    counter = 0
    sentence = ["", "", "", "", ""]
    for i in range(len(response)):
        if response[i] == " ":
            counter+=1
            if counter > 4:
                break
        else:
            sentence[counter] += response[i]

    if response == "end the game":
        on = False
    elif response == "fuck off":
        print "I would like to"
    elif response == "who are you?" or response == "who are you":
        print "I am everything and nothing at the same time. But you can just call me a helper"
    elif sentence[0] == "inspect":
        if sentence[1] == "surroundings":
            see()
        elif sentence[1] == "myself":
            print "You have " + str(hp) + " hp and " + str(hunger) + "hunger."
            if slotB == None:
                print "You do not have anything equiped"
            else:
                print "You have a " + slotB.name + " equiped."
            if slotA == None:
                print "You are not holding anything."
            else:
                print "You are holding a " + slotA.name + "."
        else:
            item = sentence[1] + sentence[2] + sentence[3] + sentence[4]
            if item == slotA.name:
                slotA.inspect()
            elif item == slotB.name:
                slotB.inspect()
            else:
                print "You do not have that"

    else:
        print "That is not something that I understand"