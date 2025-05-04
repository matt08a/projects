print(r'''
*******************************************************************************
 .-------------------------------------------------------------.
'------..-------------..----------..----------..----------..--.|
|       \\            ||          ||          ||          ||  ||
|        \\           ||          ||          ||          ||  ||
|    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||
|    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||
|_.------"''----------''----------''----------''----------''--'|
 |)|      |       |Phelan | City  |Bus |         |      ||==|  |
 | |      |  _-_  |       |       |    |  .-.    |      ||==| C|
 | |  __  |.'.-.' |   _   |   _   |    |.'.-.'.  |  __  | "__=='
 '---------'|( )|'----------------------'|( )|'----------""
             '-'                          '-'
*******************************************************************************
''')
print("Welcome to Bus Stop Madness.")
print("Your mission is to reach all the stops.")
print("A bus has arrived at the stop. Do you get on this bus or wait for another?")
bus1 = input("type on or wait: ")
damage = 0
while damage < 3:
    if bus1.lower() == "on":
        print("There are 2 available seats, 1: behind the driver\n2: in the back corner.\nWhich seat do you take?")
        seat = input("type 1 or 2: ")
        if seat == "1":
            damage += 1
            print("The driver has passed gas in your direction. Damage taken.")
        else:
            print("You witness a hate crime, but take no damage.")
        print("The bus reached the next stop and a new traveler has boarded. You can either:\n1: Offer them your seat\n2: Stay in your seat")
        seat2 = input("Type 1 or 2: ")
        if seat2 == "1" and seat == "1":
            print("You move to the other seat. The new traveler takes flatulence damage and blames you. You are punched and take damage.")
            damage += 1
        elif seat2 == "1" and seat == "2":
            print("You move to the other seat. The new traveler witnesses a hate crime and commits suicide.")
        elif seat2 == "2" and seat == "1":
            print("You do not give up your seat. The new traveler witnesses a hate crime and commits suicide.")
        else:
            print("You do not give up your seat. The new traveler takes damage when the bus driver passes gas on him.\nThe new traveler blames you and punches you. You take damage")
            damage += 1
        print("The bus reached the next stop. Do you:\n1: Get off\n2: Stay on")
        stop = input("Type 1 or 2: ")
        if stop == "2":
            print("The bus is in a terrible accident and you do not survive.")
            damage += 3
        else:
            print("you won")
            break
    else:
        print("Game Over")
        break
if damage >= 3:
    print("You succumbed to your injuries.\nGame Over")
else:
    print("Thank you for playing!")