#Mya Weiss
#Prison Escape
#1/15/25

#Init
import random
#global variables
recruits = 0
floor = 0
day = 1

#Functions
def info():
    global floor, day, recruits
    day = day + 1
    print("Day " + str(day) + " completed")
    if floor == 4:
        print("Congratulations, you have escaped the last floor!")
    if day == 10:
        print("Unfortunatly prisoner your days are up, the electric chair is awaiting.")
    if recruits == 10:
        print("Congratulations, you were able to start a riot with all your recruits, and escape.")

def cafeteria():
    global recruits
    print("You went to the cafeteria and scoped the scenery for strong inmates. You attempted to recruit 2 for your plan and they ")
    approval = random.randint(1,2) #50% chance yes or no
    if approval == 1:
        recruits = recruits + 2
        print("say your plan is smart and that they will help. You now have " + str(recruits) + " recruits")
    else:
        print("ignored you. You have " + str(recruits) + " recruits")

def workout():
    global recruits
    print("You went to the gym and go up to the 3 men lifting heavy weights. You explain your plan and they")
    approval = random.randint(1,2) #50% chance yes or no
    if approval == 1:
        recruits = recruits + 3
        print("say your plan is smart and that they will to help. You now have " + str(recruits) + " recruits")
    else:
        print("ignored you. You have " + str(recruits) + " recruits")

def plan():
    global recruits, floor
    print("You and your " + str(recruits) + " recruits dig a hole through the wall down to the next floor.")
    if recruits > 5:
        floor = floor + 2
    elif recruits < 5:
        floor = floor + 1
    print("You are " +str(floor) + " floor(s) down")


#Main
print("You are on deathrow in a maxiumum security prison. You must escape before your execution in 10 days.")
while True:
    print("Choose an option for day: " + str(day))
    print("""1. Cafeteria
2.Workout
3.Plan
4.Give up""")
    activity = int(input("Option for today: "))
    if activity == 1:
        cafeteria()
        info()
    elif activity == 2:
        workout()
        info()
    elif activity == 3:
        plan()
        info()
    elif activity == 4:
        break

    if day == 10:
        break
    if floor == 4:
        break
    if recruits == 10:
        break
