import random

choise_computer = ("piedra","papel","tijera")

rounds = 1
user_win = 0
computer_win = 0

while True:
    print("*" * 30 )
    print("           ROUND", rounds , "\n" )
    print("*" * 30)
    user = input("Ingresa tu eleccion: ").lower()
    print("\n")
    computer = random.choice(choise_computer)

    if user not in choise_computer:
        print("Eleccion invalida\n")
    else:
        if user == computer:
            print("draw\n")
        elif user == "piedra":
            if computer == "tijera":
                print("win user, rock beats scissors\n")
                user_win += 1
            else:
                print("win computer, Paper beats scissors\n")
                computer_win += 1
        elif user == "tijera":
            if computer == "papel":
                print("win user, sciccors beats paper\n")
                user_win += 1
            else:
                print("win computer, rock beats sciccors\n")
                computer_win += 1
        elif user == "papel":
            if computer == "piedra":
                print("win user, paper beats rock\n")
                user_win += 1
            else:
                print("win computer, scissors beats paper\n") 
                computer_win += 1
        if computer_win == 2:
            print("Computer WIN")
            break     
        if user_win == 2:
            print("USER WIN")
            break      
        rounds += 1                               
            
        
    
