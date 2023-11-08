print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are summoned infront of beautiful old cave! \n Once you enter the cave there is no turning back!!! \n Treasure Hunter Are you ready for the adventure\n!!")
a=input("Are you ready Type yes or no\n").lower()
if a == 'yes':
    print("You are entering the cave..!. You find yourself in the infront two road... \n ")
    b=input("which road do you wanna choose Type left or right...\n").lower()
    if b == 'left':
        c= input("You see a lake in the cave ? Do you wanna Swim or make a Boat.\n Type Swim or Boat\n").lower()
        if c == "swim":
            print("Crocdile eats you...\n... GAME OVER...")
        else:
            print("While you making the boat. you are dead by rock fallin on your head.\n GAME OVER")

    elif b == 'right':
        c1= input("You saw small gap you cant jump what will you do? you have a Log and a rope? Type log or Rope\n").lower()
        if c1 == 'log':
            print("You are adventurous you pass the gap and moves on\n")
            d= input("you find your self on a water fall Type jump or climb down\n").lower()
            if d =='jump':
                e=int(input("You jump and swim across the land. you find three door Type 1 or 2 or 3\n"))
                if e == 1:
                    f= input("Answer to this Question\n Abhishek is son of Amitabh’s father’s sister. Prakash is son of Teji who is mother of Vikash who is a male and grandmother of Amitabh. Harivansh is father of Neela and grandfather of Abhishek. Teji is wife of Harivansh. How is Abhishek related to Teji\n").lower()
                    if f == 'grandson':
                        print("you won the treasure and a Amazon voucher of $100\n")
                        g= input("Do you wanna use treasure or Amazon coupon Type Treasure or Coupon\n").lower
                        if g == 'coupon':
                            print(" you won the real treasure. You simple person. Being simple and humble. Makes you a man\n")
                        else:
                            print("You greedy wrothless human being Die B Die. Rock falls on your head and yopu die... Game Over...")
                    else:
                        print(" you are not inTelligent to be worthy for the treasure.. Arrow is shot your head and You Die \n ...GAME OVER..")
                elif e == 2:
                    j = input("Do you like Fire or water\n").lower
                    if j== 'fire':
                        print("you are killed using flame thrower.. LOL you are burnt and Die \n...GAME OVER...")
                    else:
                        print("you are drown to death...\n .. Game Over...")

                else:
                    print("A boulder rolled you down!! \n Game over")

            else:
                print("you slep and broke your neck!! You are dead\n ...GAME OVER...")
    
        else:
            print("You swing the rope to other side. It connects but breaks because of your weight GAME OVER... Nice Try Moron")

    else:
        print("You fell down on deep hole\n ...GAME OVER...")          
else:
    print("You stupid human being... You are no Treasure Hunter, You are Useless")