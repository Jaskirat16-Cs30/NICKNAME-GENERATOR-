#Jaskirat Singh
#NICKNAME GENERATOR ASSIGNMENT
import random
nickNam = ["Waffle","hero ","PapaSmurf","Pixels","HogButcher","Loser","Brave","Mammoth","Star","FearLeSS"]
#input
firstNam= input("What is your first name ")
lastNam= input("\n What is your last name ")
#menu
menu = True
while menu== True:
    print("\nMAIN MENU ( ",firstNam,lastNam,")")
    print("1.Change Name")
    print("2.Display a Random Nickname")
    print("3.Display All Nicknames")
    print("4.Add a Nickname")
    print("5.Remove a Nickname ")
    print("6.Exit")
    option =input("\noption = ")
#Change Name 
    if option == "1":
        firstNam= input("\nPlease enter first name: ")
        lastNam= input("Please enter last name: ")
        print ("Current name is",firstNam,lastNam)
#Display a Random Nickname
    elif option == "2":
        randName = random.choice(nickNam)
        print(firstNam,"'",randName,"'",lastNam)
#Display All Nicknames
    elif option =="3":
        for names in nickNam:
            print(firstNam,"'",names,"'",lastNam)
#Add a Nickname
    elif option == "4":
        newNam = input('\nPlease enter a nickname to add:')
        if newNam in nickNam:
            print(newNam," is already in the nickname list.")
        else:
             nickNam.append(newNam)
             print(newNam," added to the nickname list.")

    elif option == "6":
        print("\nExited")
        menu = False

   



