def Wrong():
    print("Please Type the Correct option and start the game again")

z = "(You Lose, Try again later)"
userAns = input("Do you want to play this text game at our own Risk? Type[Y/N]: ")

if userAns == 'Y':
    flag = True
    print("Thats Good Let's Start\n")
    userAns = input("So you were getting chased by police officers and you have a muddy road on left and Airport in Right were Do you want to go? Type[Left/Right]: ")

    if userAns == 'Right':
        print("Thats a good choice, lets go to the Airport to catch a flight.....\n")
        print("Congo,..You are in a flight\n")
        userAns = input("oh Shit your flight have been Crashed in cold Mountain Range, What is your next step?: Type[Sky Dive / Stay in Plane]: ")

        if userAns == 'Stay in Plane':
            print("Your Decision was Right and Hence  after a Crash, Your are safe inside a plane body with other Passengers\n")
            userAns = input("You were Shivering of Cold, would you take wool from plane seats? Type[Yes/No]: ")
            if userAns == 'Yes':
                print("Ok Lets take Wool and lets fight with cold\n")
                userAns = input("Five Days Passed and You were hungry and there is no food, your last option to eat dead passengers, would you do that? Type[Yes/No]: ")
                if userAns == 'Yes':
                    print("Its Disgusting but its last option for surviewal...\n")
                    userAns = input("Its been 1 Month for crash but there is no help, what is your next move? would like to go on search for help or you wait in plane for help, Type[Search / Wait]: ")
                    if userAns == 'Search':
                        print("Nice Decision, Hence You got Help and your surviewed....\n")
                        print("Congratulations you Finished Your Game......")
                    elif userAns == 'Wait':
                        print("Sorry there no Help, Hence you didn't Surviewed..... "+z)
                    else:
                        Wrong()

                elif userAns == 'No':
                    print("Oh no you died of cold...., "+z)
                else:
                    Wrong()
            elif userAns == 'No':
                ("Oh no, You Died of Cold,... "+z)
            else:
                Wrong()

        elif userAns == 'Sky Dive':
            print("Oh no, After Skydiving you landed on Mountain Alone and its so cold, Hence You Died!!! "+z)
        else:
            Wrong()
    elif userAns == 'Left':
        print("Sorry you were stuck on Mud and Got Arrested by Police "+z)
    else:
        Wrong()
else:
    print("Come on dont be a Loser!!!(Type correct option and start the game)")