import os
import time
import sys
import random
a = "1"
if a == "1":
    ld = 0
    for x in range(0, 5):
        ld = ld + 1
        ld2 = ("Loading" + "." * ld)
        sys.stdout.write('\r' + ld2)
        time.sleep(0.5)
    print()

    men = True
    while men == True:
        print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print ("            Welcome to the dice game!")
        print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        b = input("Main menu. 1. Sign up, 2. Play game, 3. Leaderboard, 4. Settings, 5. Exit. Enter corresponding number ")
        print ("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        """)
        if b == "1":
            print ("Sign up selected.")
            s1 = input ("Are you sure you would like to create a new account? y/n ")
            if s1 == "y":
                print ("Sign up started.")
                username1 = input ("Enter your username. ")
                password1 = input ("Enter your password. Use atleast 5 characters. ")
                while len(password1) < 5:
                    print ("Not long enough")
                    password1 = input("Enter your password. Use atleast 5 characters. ")
                else:
                    file = open("dieaccounts.txt", "a")
                    file.write(username1)
                    file.write(",")
                    file.write(password1)
                    file.write("\n")
                    file.close()
                    print ("Account created. Welcome,",username1,)
                    print ("Returning to menu...")
                    print ("")
            else:
                print ("Returning to menu...")
                print ("")


        elif b == "2":
            print ("Play game selected.")
            print ("PLAYER 1 LOGIN")
            supplied_username = input ("Enter your username ")
            supplied_password = input ("Enter your password ")
            player1 = supplied_username
            logged_in = False
            with open('dieaccounts.txt', 'r') as file:
                for line in file:
                    username, password = line.split(',')
                    if username == supplied_username:
                        logged_in = password == supplied_password
                        logged_in = True
                        break

            if logged_in == True:
                print ("Credentials accepted.")
                print ("PLAYER 2 LOGIN")
                supplied_username = input("Enter your username ")
                supplied_password = input("Enter your password ")
                player2 = supplied_username
                logged_in = False
                with open('dieaccounts.txt', 'r') as file:
                    for line in file:
                        username, password = line.split(',')
                        if username == supplied_username:
                            logged_in = password == supplied_password
                            logged_in = True
                            break
                if logged_in == True:
                    print ("Credentials accepted")
                    print ("Starting game")
                    time.sleep(1)
                    print ("-----------------------------------")
                    print ("Your roll,", player1)
                    print ("")
                    p1d1 = random.randint(1, 10)
                    p1d2 = random.randint(1, 10)
                    time.sleep(1)
                    print ("Roll 1:",p1d1)
                    print ("")
                    time.sleep(1)
                    print ("Roll 2:",p1d2)
                    print ("")
                    if p1d1 != p1d2:
                        sp1 = p1d1 + p1d2
                    else:
                        p1d3 = random.randint(1, 10)
                        print ("Doubles bonus! Rolling third dice...")
                        print ("")
                        time.sleep(1)
                        print("Roll 3:",p1d3)
                        print ("")
                        sp1 = p1d3 + p1d2 + p1d1
                    if sp1 % 2 == 0: #mod, % checks if remainder = 0
                        print("Even bonus! +10 points")
                        print ("")
                        time.sleep(1)
                        sp1 = sp1 + 10
                    if sp1 < 0:
                        sp1 = 0
                    time.sleep(1)
                    print ("You scored,",sp1 )
                    print("-----------------------------------")
                    print ("")





                    print ("Your roll,", player2)
                    print("-----------------------------------")
                    print("Your roll,", player2)
                    print("")
                    p2d1 = random.randint(1, 10)
                    p2d2 = random.randint(1, 10)
                    time.sleep(1)
                    print("Roll 1:", p2d1)
                    print("")
                    time.sleep(1)
                    print("Roll 2:", p2d2)
                    print("")
                    if p2d1 != p2d2:
                        sp2 = p2d1 + p2d2
                    else:
                        p2d3 = random.randint(1, 10)
                        print("Doubles bonus! Rolling third dice...")
                        print("")
                        time.sleep(1)
                        print("Roll 3:", p2d3)
                        print("")
                        sp2 = p2d3 + p2d2 + p2d1
                    if sp2 % 2 == 0:  # mod, % checks if remainder = 0
                        print("Even bonus! +10 points")
                        print("")
                        time.sleep(1)
                        sp2 = sp2 + 10
                    if sp2 < 0:
                        sp2 = 0
                    time.sleep(1)
                    print("You scored,", sp2)
                    print("-----------------------------------")
                    print("")

                else:
                    print("Invalid.")
                    print("Returning to menu...")
                    time.sleep(1)

            else:
                print ("Invalid.")
                print ("Returning to menu...")
                time.sleep(1)

        elif b == "3":
            print ("Leaderboard selected")
            os.startfile('N:\IT\leaderboard.txt')

        elif b == "4":
            print ("Settings selected")
            sa = input ("1. Enter dev code 2.  ")
            if sa == "1":
                print ("Dev code selected")
                dvc = input("Enter devcode ")
                if dvc == "AccessAccount":
                    print ("Code accepted")
                    os.startfile('N:\IT\dieaccounts.txt')
                else:
                    print ("Invalid.")

            #make scret setting option, if you input code you can acess accounts database.

        elif b == "5":
            print ("Exit selected.")
            print ("Goodbye.")
            men = False