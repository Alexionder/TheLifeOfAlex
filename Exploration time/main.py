from items import *
import random
worldLimit = 50
world = [[-1 for y in range (worldLimit)] for x in range(worldLimit)]
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
    if world[x][y] == -1:
        text += " nothing"
    else:
        for i in world[x][y]:
            text += " a " + i.name + ","
    text = text[:-1] + " here."
    print text

print ""
print "***************************"
print "*****STARTING THE GAME*****"
print "***************************"
print ""

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
        elif response[i] != "." and response[i] != "," and response[i] != "?" and response[i] != "!":
            tmp = response[i]
            if tmp.isupper():
                tmp = tmp.lower()
            sentence[counter] += tmp

    if sentence[0] == "end":
        for txt in sentence:
            if txt == "game":
                on = False
    elif response == "fuck off":
        print "I would like to"
    elif response == "who are you?" or response == "who are you":
        print "I am everything and nothing at the same time. But you can just call me a helper"
    elif sentence[0] == "inspect":
        if sentence[1] == "surroundings" or sentence[1] == "":
            see()
        elif sentence[1] == "myself":
            print "You have " + str(hp) + " hp and " + str(hunger) + " hunger."
            if slotB == None:
                print "You do not have anything equipped."
            else:
                print "You have a " + slotB.name + " equipped."
            if slotA == None:
                print "You are not holding anything."
            else:
                print "You are holding a " + slotA.name + "."
        else:
            item = sentence[1]
            for it in sentence[2:]:
                if it != "":
                    item += " " + it
            if slotA != None and item == slotA.name:
                slotA.inspect()
            elif slotB != None and item == slotB.name:
                slotB.inspect()
            else:
                print "You do not have that"
    elif sentence[0] == "go":
        if sentence[1] == "north" and y+1 < worldLimit:
            y+=1
            seen = False
            print "Going north."
        elif sentence[1] == "west" and x+1 < worldLimit:
            x+=1
            seen = False
            print "Going west."
        elif sentence[1] == "south" and y > 0:
            y-=1
            seen = False
            print "Going south."
        elif sentence[1] == "east" and y > 0:
            x-=1
            seen = False
            print "Going east."
        else:
            print "You cannot go there."

        if world[x][y] == -1:
            world[x][y] = []
            for i in range(random.randint(1, 4)):
                chance = random.randint(0, 3)
                if chance == 0:
                    world[x][y].append(Sword(random.randint(10, 25), random.randint(3, 10), "sword"))
                elif chance == 1:
                    world[x][y].append(Axe(random.randint(10, 25), random.randint(3, 10), "axe"))
                elif chance == 2:
                    world[x][y].append(HPbottle(random.randint(10, 70)))
                else:
                    world[x][y].append(Food(random.randint(10, 70), "bread"))
    elif sentence[0] == "take":
        item = sentence[1]
        for it in sentence[2:]:
            if it != "":
                item += " " + it
        taken = False
        for it in world[x][y]:
            if item == it.name:
                taken = True
                if slotA != None:
                    world[x][y].append(slotA)
                    print "You dropped " + slotA.name + "."
                print "You took " + it.name + "."
                world[x][y].remove(it)
                slotA = it
        if not taken:
            print "There is no " + item + " here."
    elif sentence[0] == "equip":
        item = sentence[1]
        for it in sentence[2:]:
            if it != "":
                item += " " + it
        if item == slotA.name:
            if slotB != None:
                print "You unequipped " + slotB.name + " and equipped " + slotA.name + "."
                tmp = slotB
                slotB = slotA
                slotA = tmp
            else:
                print "You equipped " + slotA.name + "."
                slotB = slotA
                slotA = None
        else:
            print "You do not have that."
    elif sentence[0] == "drop":
        item = sentence[1]
        for it in sentence[2:]:
            if it != "":
                item += " " + it
        if slotA != None:
            if slotA.name == item:
                print "You dropped " + slotA.name + "."
                world[x][y].append(slotA)
                slotA = None
            else:
                print "You are not holding that."
        else:
            print "You are not holding that."
    elif sentence[0] == "unequip":
        item = sentence[1]
        for it in sentence[2:]:
            if it != "":
                item += " " + it
        if slotB != None and slotB.name == item:
            if slotA != None:
                print "You dropped " + slotA.name + " and you unequipped " + slotB.name + "."
                world[x][y].append(slotA)
                slotA = slotB
                slotB = None
            else:
                print "You uneuipped " + slotB.name + "."
                slotA = slotB
                slotB = None
        else:
            print "You don't have that equipped."
    elif sentence[0] == "devins":
        print world[x][y]
    else:
        print "That is not something that I understand."
    print "***"


print ""
print "***************************"
print "******ENDING THE GAME******"
print "***************************"
print ""
