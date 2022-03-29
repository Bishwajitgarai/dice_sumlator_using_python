import random

r = input("Type yes to roll the dice : ")
x="y"
while(x=="y"):
    no = random.randint(1,6)
    if no==1:
        print("      ")
        print("  o   ")
        print("      ")
    elif no == 2:
        print(" o     ")
        print("       ")
        print("     o ")
    elif no == 3:
        print(" o     ")
        print("   o   ")
        print("     o ")
    elif no == 4:
        print(" o    o ") 
        print("        ") 
        print(" o    o ") 
        
    elif no == 5:
        print(" o    o ") 
        print("   o    ") 
        print(" o    o ") 
        
    elif no == 6:
        print(" o  o  o")
        print("        ")
        print(" o  o  o")
    x =str( input("Press  y to roll the dice again and n to exit : "))
    print("\n")
