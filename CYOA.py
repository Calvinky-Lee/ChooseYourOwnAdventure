import time
import random

#introduction
def game_start():
    print("-" * 25)
    print("This CYOA project follows the life of a Falsely convicted prisoner, going through a ")
    print("10 day sentence at Boronto Correctional facility in hopes to escape. There is an crafting ")
    print("and trade system inbeded within as well as reputation and health meter you must maintain")
    print("The adventure will end if prison strikes = 5, reputation = 0, health = 0, day number = 10, or you find a way to escape")
    print("Good Luck!")
    print("-"*25)
    command = input("type start to continue : \n ").lower()
    print("-" * 25)

    if command == "start":
        begin()
    else:
        print("Hmmm, that didn't seem to work. Try again \n ")
        game_start()



#rollcall planned out
def begin():
    global day
    day = day + 1
    print("\n")
    print("-" * 25)
    print(f'Day #{day}')

    print("It was a dreamy night while you lying down in bed, suddenly waken up by an announcement stating 'ALL PRISONERS PRESENT TO ROLCALL'")
    print("You carefully wake up, questioning how many days are left in your sentence, before getting up off of your bed. \n what do you do?")

    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-"*25)
    print("Options:")
    print("attend - Follow the general vicinity with the prisoners to attend roll-call")
    print("skip - Skip rollcall to explore the prison and get new items ")
    print("-" * 25)
    command = input("Please enter your choice:\n ").lower()

    if command == "attend":
        rollcall()
    elif command == "skip":
        skiprollcall()
    else:
        print("Hmmm, that didn't seem to work. Try again")
        begin()


#choose to skip rollcall
def skiprollcall():
    global pstrike, health
    pstrike = pstrike + 1
    health = health - 15
    add_random_item()

    print("\n")
    print("-" * 25)
    print("Next:")
    print("You choose to dose of and find your place around the prison")
    print("as you wander around, you find a new area in the prison you haven't ever seen before, and find a brand new item to take back")
    print("jumping in exitement, you accidentally catching a guards attention, who starts charging and shouting at you ")
    print("tackling you over, adding a Prison strike to your name, and bringing you back into schedule")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print_inventory()


    time.sleep(6)
    random_activity()



def rollcall():
    print("\n")
    print("-"*25)
    print("Next:")
    print("you tiredly leave your cell, following other inmates towards the courtyard")
    print("the guards go through a large list of names, givig some time to socialize at the end\n")
    print("you awkwardly stand alone looking for options to do to pass the short amount of time ")
    print("what do you do?")
    print("-"*25)
    print("nothing - stand around and do nothing")
    print("attack - attack one of the inmates")
    print("talk - communicate with the other inmates")
    print("-"*25)
    choice = input("Input your option here:\n").lower()

    if choice == "nothing":
        roll_call_nothing()
    elif choice == "talk":
        roll_call_talk()
    elif choice == "attack":
        roll_call_attack()
    else:
        print("Hmmm, that didnt seem to work. Try again")
        rollcall()


def roll_call_nothing():
    global reputation
    reputation = reputation - 10
    print("\n")
    print("-" * 25)
    print("Next:")
    print("you decide to stand around and do nothing as other inmates notice you as an outcast")
    print("you wait in bordem until the guards indicate towards moving on to the next event of the day")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)
    time.sleep(2)
    random_activity()


def roll_call_talk():
    global reputation
    reputation = reputation + 10
    print("\n")
    print("-" * 25)
    print("Next:")
    print("you walk up to a group of inmates in attempts of socialization")
    print("you invest yourself in a deep conversation before being inturupted by the guards, moving onto the next event")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)
    time.sleep(2)
    random_activity()


def roll_call_attack():
    global reputation, pstrike

    if health >= 60:
        reputation = reputation + 10
        pstrike = pstrike + 1
        print("\n")
        print("-" * 25)
        print("Next:")
        print("you randomly start fighting another inmate, throwing and recieving punches, ultimately knocking him out")
        print("the fight is quickly dismantled by the guards awarding you a prison strike for starting the fight")
        print("the inmates roar in cheer, Viewing you as a higher authority figure not to mess with ")
        print("as a result of everyone's antics, the guard brings everyone in early, continuing the day with the assigned activity of the day")
        print("-" * 25)
        print(f'Health: {health}')
        print(f'Reputation : {reputation}')
        print(f'Prison Strikes: {pstrike}')
        print("-" * 25)

        time.sleep(6)

    elif health < 60:
        reputation = reputation - 20
        print("\n")
        print("-" * 25)
        print("Next:")
        print("you randomly start fighting another inmate, throwing a few punches, before falling down from one of his")
        print("your mind blurs out with the last thing you remember being the prisoners looking down at you")
        print("Some time later, you wake up to yourself surrounded by guards, continuing you on with the next")
        print("activity of the day")
        print("-" * 25)
        print(f'Health: {health}')
        print(f'Reputation : {reputation}')
        print(f'Prison Strikes: {pstrike}')
        print("-" * 25)

        time.sleep(6)

    random_activity()


def random_activity():
    command = random.randint(1, 4)
    if command == 1:
        food_time()
    elif command == 2:
        phone_call()
    elif command == 3:
        cell_confinment()
    elif command == 4:
        doctor_checkup()


#random activities
def food_time():
    print("\n")
    print("-" * 25)
    print("Activity: Cafeteria")
    print("\n")
    print("You transition with your inmates towards the cafeteria to gain your daily required nutrition.")
    print("as you enter into the long que for food, you are given a food stamp with different food options to eat")
    print("What would you like to eat?")
    print("-" * 25)
    print("beans and rice")
    print("chicken pot pie")
    print("hamburger")
    print("-" * 25)
    choice = input("Input your option here:\n").lower()

    if choice == "beans and rice":
        beans_and_rice()
    elif choice == "chicken pot pie":
        chicken_pot_pie()
    elif choice == "hamburger":
        hamburger()
    else:
        print("Whoops that didnt seem to work, try again")
        food_time()

def beans_and_rice():
    print("\n")
    print("-" * 25)
    print("You get your plate of beans and rice and walk towards the tables within the cafeteria")
    print("Which table would you like to sit?")
    print("-" * 25)
    print("table 1 : 3/6 people sitting")
    print("table 2 : 0/6 people sitting")
    print("-" * 25)
    choice = input("Input your option here:\n").lower()
    print("\n")

    if choice == "table 1":
        table_1_sit()
    elif choice == "table 2":
        table_2_sit()
    else:
        print("Whoops that didnt seem to work, try again")
        beans_and_rice()


def table_1_sit():
    global reputation, health
    health == health + 20
    reputation == reputation + 10
    print("\n")
    print("-" * 25)
    print("You aproach the table and take a seat, sparking mini conversations until break is over")
    print("the surrounding prisoners notice your new alies as a result")
    print("After some time passes, the guards start indicating towards everone to start heading in for lights out ")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)

    time.sleep(4)
    check_stats()


def table_2_sit():
    global reputation, health
    health == health + 20
    reputation == reputation - 10
    print("\n")
    print("-" * 25)
    print("The inmates question your decision to sit all alone by yourself, ultimately judging your antics")
    print("you casually eat your food and stare off into blank state until break is over.")
    print("After some time passes, the guards start to indicate for everyone to come back to their cells for the end of the day ")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)


    time.sleep(4)
    check_stats()


def chicken_pot_pie():
    print("\n")
    print("-" * 25)
    print("You grab your tray containing a minature chicken pot pie, siting down at a table, casually eating your food")
    print("that is when you notice a fight breaking out in the distance, you question weather you should get involved")
    print("What do you do?")
    print("-" * 25)
    print("yes: intefere with the fight")
    print("no: let them fight it out")
    print("-" * 25)
    command = input("Input your awnser here:\n").lower()

    if command == "yes":
        interfere_fight()
    elif command == "no":
        let_fight_out()
    else:
        print("Hmmm, that didnt seem to work. Try again")
        chicken_pot_pie()

def let_fight_out():
    global blue_dye
    blue_dye = blue_dye + 1
    print("\n")
    print("-" * 25)
    print("You watch in the distance as the inmates fight it out, while  the guards interfere")
    print("with the fight finding one prisoner knocked out. As a result the guards end food time early")
    print("as sneak in and  manage to grab a bottle of blue dye from the knocked out prisoners outfit.")
    print_inventory()

    time.sleep(6)
    check_stats()

def interfere_fight():
    print("\n")
    print("-" * 25)
    print("you start to walk up to interfere with the fight, only to be stopped by one of the inmates fighting")
    print("he tells you to back off and to get off his back")
    print("What do you do?")
    print("-" * 25)
    print("fight: proceed with your intentions and attack him")
    print("back off: decide that fighting isnt for you and walk away")
    print("-" * 25)
    command = input("what option would you like to pick\n").lower()

    if command == "fight":
        kitchen_fight()
    elif command == "back off":
        back_off()
    else:
        print("hmmm that didnt seem to work, please try again")
        interfere_fight()

def kitchen_fight():
    global health, reputation, blue_dye, pstrike
    health = health - 15
    reputation = reputation + 15
    blue_dye = blue_dye + 1
    pstrike = pstrike + 1

    print("\n")
    print("-" * 25)
    print("You start picking a fight with the opposing inmate, throwing down a few punches, overall knocking him out. ")
    print("Soon enough, the fight ends with the guards breaking everyone up quickly, giving you a prison strike, ")
    print("returning everyone back to their cells.  Prisoners gain respect for you as a result and one gives ")
    print("you a bottle of blue dye as a result.")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)
    print_inventory()

    time.sleep(6)
    check_stats()


def back_off():
    global reputation
    reputation = reputation - 15

    print("\n")
    print("-" * 25)
    print("You start to walk away, letting them fight it out, your antics are perceived to show a lack of confidence,")
    print("and with other inmates looking down upon you. You sit back down and let time pass until the guards ushers")
    print("everyone inside, nearing lights out.")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)

    time.sleep(6)
    check_stats()


def hamburger():
    print("\n")
    print("-" * 25)
    print("You grab your hamburger and start heading towards a table, until you feel a tap on your shoulder")
    print("You turn around and find an inmate asking to share foods")
    print("What do you do?")
    print("-" * 25)
    print("share food: split your burger half-half with the other inmate")
    print("dont share food: decide that you want the burger to yourselve and dont share")
    print("-" * 25)
    command = input("what option would you like to pick\n").lower()

    if command == "share food":
        share_food()
    elif command == "dont share food":
        dont_share_food()
    else:
        print("Hmmm, seems like that didn't work, try again")
        hamburger()

def share_food():
    global battery, health, reputation
    battery = battery + 1
    health = health + 10
    reputation = reputation + 5

    print("\n")
    print("-" * 25)
    print("You reluclantly agree to split your foods half-half as you both find a table to sit down at.")
    print("As a result the prisoner thanks you and gives a battery from his pocket in return.")
    print("You both finish your food before being signified by the guards to go back to your cells.")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)
    print_inventory()

    time.sleep(6)
    check_stats()

def dont_share_food():
    global health, reputation
    health = health + 25
    reputation = reputation - 10
    print("\n")
    print("-" * 25)
    print("The prisoner grungily walks away from your antics annoyed over your decision, you casually find a place to sit")
    print("while slowly eating your food while waiting for the guards to escort everyone back to their cells")
    print("nearing the end of the day.")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)

    time.sleep(6)
    check_stats()


def phone_call():
    print("\n")
    print("-" * 25)
    print("Activity: Phone call")
    print("\n")
    print("What would you like to do?")
    print("-" * 25)
    print("call random number: enter in a random number and hope for the best")
    print("call mom: call your mom's number")
    print("call sister: call your sister's number")
    print("take parts: attempt to take parts from the telephone")
    print("-" * 25)
    command = input("enter your option here: \n").lower()

    if command == "call random number":
        call_random_number()
    elif command == "call mom":
        call_mom()
    elif command == "call sister":
        call_sister()
    elif command == "take parts":
        steal_part()
    else:
        print("hmmm that didnt seem to work, Try again")
        phone_call()



def call_random_number():
    global metal
    metal = metal + 1

    print("\n")
    print("-" * 25)
    print("You call a random number,  connecting with a random person who owns a junk yard. You as for a simple request")
    print("for some leftover metal to be sent to you, as he reluctantly agrees, ignorant to the fact you are a prisoner.")
    print("After your phone call, the guards raise suspission before returning you to your cell")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)

    time.sleep(6)
    check_stats()

def call_mom():
    global white_outfit
    white_outfit = white_outfit + 1

    print("\n")
    print("-" * 25)
    print("you dial your moms phone as  she instantly picks up in joy expressing how much she misses you.")
    print("As you guys converse, your mom agrees to send a White outfit to help you with your own comfortibility,")
    print("you hang up after a hearty conversation followed by the guards escorting you to your cell")
    print_inventory()

    time.sleep(6)
    check_stats()

def call_sister():
    print("\n")
    print("-" * 25)
    print("You call your sister in joy, as she reluctantly picks up, you attempt to make small talk")
    print("before hearing the tone fade out as your sister hangs up on you.")
    print( "The guards signify that as the end of your call and take you back to your cell")
    print("-" * 25)

    time.sleep(6)
    check_stats()


def steal_part():
    global circuit_board
    circuit_board = circuit_board + 1

    print("\n")
    print("-" * 25)
    print("You walk up to the telephone and notice a ripped off section contained, you pretend to call someone")
    print(" using it as a distraction to take a piece of the circuit board and stuff it in your pocket")
    print("the guards do not notice anything out of touch as they escort you back to your cell")
    print_inventory()

    time.sleep(6)
    check_stats()


def cell_confinment():
    print("\n")
    print("-" * 25)
    print("Activity: cell_confinment")
    print("\n")
    print("What would you like to do?")
    print("-" * 25)
    print("talk : talk to your cellmate")
    print("trade: trade items with your cellmate")
    print("-" * 25)
    command = input("enter your option here: \n").lower()

    if command == "talk":
        talk_cellmate()
    elif command == "trade":
        trade_cellmate()
    else:
        print("hmmm that didnt seem to work, Try again")
        cell_confinment()

def talk_cellmate():
    print("\n")
    print("-" * 25)
    print("In Bordem, You casually engage in a conversation with your cell mate ")
    print("eventaully leading you towards a heated dissagrement about Politics")
    print("how will you settle this disagreement?")
    print("-" * 25)
    print("disregard : disregard the conversation in attempts to switch topics")
    print("attack : settle your dissagrement by attacking him")
    print("-" * 25)
    command = input("what option would you like to pick\n").lower()

    if command == "disregard":
        disregard_convo()
    elif command == "attack":
        convo_attack()
    else:
        print("Hmmm, seems like that didn't work, try again")
        talk_cellmate()

def disregard_convo():
    global reputation
    reputation = reputation + 15

    print("\n")
    print("-" * 25)
    print("You and your cellmate manage to settle out a conversation after your expressed dissagrements")
    print("switching topics and chatting until the night goes down.")
    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)


    time.sleep(6)
    check_stats()
def convo_attack():
    global health, pstrike, reputation
    print("\n")
    print("-" * 25)
    print("You make a move by setting in a few punches, you shocks your cellmate eventually reciprocating himself")

    if health <= 50:
        health = health - 45
        pstrike = pstrike + 1


        print("His impactful punches causes you to be immediatly be knocked out, hitting hard on the ground")
        print("Guards eventually swarm the cell, with you regaining your consciousness, the officers give both")
        print("you and your cellmate are both given prison strikes, followed by the guards determining its lights out")
        print("locking down all the cells.")
    elif health > 50:
        pstrike = pstrike + 1
        health = health - 15
        reputation = reputation + 30

        print("With rage fueling yourself, you set in a attack that knocks him down, ultimately  winning the fight")
        print("standing as the victor. While hearing the cell block roar with cheers from all the other inmates")
        print("you enjoy your quick jolt of fame, before being tackled by a set of guards rushing into the cell.")
        print("As a result, the guards give both of you a prison strike, begining lights out early")

    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)


    time.sleep(6)
    check_stats()


def trade_cellmate():
    global circuit_board, metal, battery, stick, white_outfit

    print("\n")
    print("-" * 25)
    print("In Bordem, you ask your cellmate to trade owned items to pass time ")
    print("He reluctulantly agrees while proprosing a few trades for you")
    print("-" * 25)
    print_inventory()
    print("-" * 25)
    print("one : give metal, get circuit board")
    print("two: give battery, get Metal")
    print("three: give stick, get white outfit")
    print("back : nevermind I dont want to trade")
    print("-" * 25)
    command = input("what option would you like to pick\n").lower()

    if command == "one" and metal > 0:
        metal = metal - 1
        circuit_board = circuit_board + 1

        print("-" * 25)
        print("Your cellmate agrees with your decision and gives you the item of choice")
        print("you store away your new item in your compartment, potentially to use later in the night ")
        print("-" * 25)
    elif command == "two" and battery > 0:
        battery = battery - 1
        metal = metal + 1

        print("-" * 25)
        print("Your cellmate agrees with your decision and gives you the item of choice")
        print("you store away your new item in your compartment, potentially to use later in the night ")
        print("-" * 25)
    elif command == "three" and stick > 0:
        stick = stick - 1
        white_outfit = white_outfit + 1

        print("-" * 25)
        print("Your cellmate agrees with your decision and gives you the item of choice")
        print("you store away your new item in your compartment, potentially to use later in the night ")
        print("-" * 25)
    elif command == "back":
        cell_confinment()
    else:
        print("Hmmm, seems like that didn't work, try again")
        trade_cellmate()

    print_inventory()
    time.sleep(6)
    check_stats()

def doctor_checkup():
    global health

    print("\n")
    print("-" * 25)
    print("Activity: Doctor Checkup")
    print("\n")
    print("Which doctor would you like to be checked by")
    print("-" * 25)
    print("dr.lidia")
    print("dr.calvin")
    print("dr.emily")
    print("dr.hank")
    print("-" * 25)
    command = input("enter your option here: \n").lower()

    if command == "dr.lidia":
        health = health + 35

        print("-" * 25)
        print("You go up to dr.Lidia whereas she goes through a extensive set of medication assigning you to a set of daily pills")
        print("to help with general health, you walk back to your cell block feeling better then ever"
              "")
    elif command == "dr.calvin":
        health = health + 5
        print("-" * 25)
        print("You line up to be checked up my Dr. Calvin whereas he goes through a simple heart rate check")
        print("before deeming good to go. overall having little impact on your health, you grudgily walk back to your cell block feeling much the same")

    elif command == "dr.emily":
        health = health +25
        print("-" * 25)
        print("upon walking up to get checked by Dr.Emily, she glances at your file before providing polio ")
        print("and covid vaccinations missing, before deeming you good to go. you walk back to your cell block ")
        print("with a sore arm, knowing its for the better")
    elif command == "dr.hank":
        dr_hank()

    else:
        print("hmmm that didnt seem to work, Try again")
        doctor_checkup()

    print("-" * 25)
    print(f'Health: {health}')
    print(f'Reputation : {reputation}')
    print(f'Prison Strikes: {pstrike}')
    print("-" * 25)

    time.sleep(6)
    check_stats()
    #check stats


def dr_hank():
    global health
    print("-" * 25)
    print("Upon entering the room for check up, Dr. Hank presents a blue formula newly created aiding general health.")
    print("Do you take it?")
    print("-" * 25)
    print("yes")
    print("no")
    print("-" * 25)
    option = input("enter your option here: \n").lower()

    if option == "yes":
        health = health + 50
        print("-" * 25)
        print( "You gulp down the newly created blue formula, feeling as sence of increased mood and strength, helping tremendously.")
        print("Dr.Hank deems you good to go, letting you out of his office")
        print("You start to walk back to your cell block feeling better than ever")
    elif option == "no":
        health = health + 5
        print("-" * 25)
        print("Dr.hank understands you choice and proceeds with a  general hearbeat, ear checkup before assigning you good to go")
        print("you think to yourself that the assesment did not help that much, whhile making your way back to your cell block")
    else:
        print("hmmm that didnt seem to work, Try again")
        dr_hank()

def check_stats():
    if day == 10:
        sentence_finished()
    elif reputation == 0:
        rep0_end()
    elif pstrike == 5:
        solitary_confinment()
    elif health == 0:
        death_end()
    else:
        lights_out()


def sentence_finished():
    print("\n")
    print("-" * 25)
    print("End of Day : 10")
    print("After what feels like the longest 10 days of your life, you finally notice that sentence has come to and end.")
    print("During the night, the guards unlock your cell while saying 'your time is done, its time to go home' ")
    print(" you walk out of the cell, following his path towards the front entrance, where he unlocks the door to the begining of freedom once again")
    print("*"*25)
    print("The End")
    print("*"*25)

def rep0_end():
    print("\n")
    print("-" * 25)
    print("Reputation : 0")
    print("On your way back to your cell you look down, questioning the days left until freedom.")
    print("Before reaching your cell block, you notice yourself surrounded by a set of following inmates who have")
    print("reached a general disliking towards you due to your reputation status,")
    print("suddenly you get tackeled on the ground by the inmates who show no remorse, as your vision fades into nothingness ")
    print("*"*25)
    print("The End")
    print("*"*25)


def solitary_confinment():
    print("\n")
    print("-" * 25)
    print("Prison strike : 5")
    print("On your way back to your cell. you are suddenly stopped by a group of guards who start lecturing you about your antics.")
    print("The guards continue on exclaiming how solitary confinment punishment was required for reaching 5 strikes")
    print("suddenly handcuffing you, leading you towards a dark alley of rooms, which would house your next future days")
    print("*"*25)
    print("The End")
    print("*"*25)


def death_end():
    print("\n")
    print("-" * 25)
    print("Health : 0")
    print("as you are walking back to your cell, you feel a sudden jolt of pain")
    print("you realise this was your bodys way of communicating that it couldnt function in its condition.")
    print("You attempt to find a guard, in hopes to see medical attention, in the process collapsing on the ground,")
    print("ending your journey")
    print("*"*25)
    print("The End")
    print("*"*25)


#lights out
def lights_out():
    print("\n")
    print("-" * 25)
    print("Next:")
    print("you grudgily cell walk back to your cell, preparing for lights out")
    cell_time()


def cell_time():
    print("\n")
    print("sitting down on your bed, looking around, you question what to do next ")
    print("what would you like to do?")
    print("-" * 25)
    print("craft - craft items to escape prison")
    print("escape - attempt to escape prison")
    print("sleep - get a good nights rest to prepare for the same day tomorrow")
    print("-" * 25)
    choice = input("Input your option here\n").lower()

    if choice == "craft":
        craft_items()
    elif choice == "escape":
        escape_options()
    elif choice == "sleep":
        next_day()
    else:
        print("Hmmm, that didn't seem to work. Try again")
        lights_out()

#crafting

def craft_items():
    print("\n")
    print("-" * 25)
    print("What would you like to craft?")
    print_inventory()
    print("crowbar: metal + metal")
    print("shovel: Stick + metal")
    print("guard outfit: White outfit + Blue dye")
    print("keycard: Circuit board + battery")
    print("back : nevermind i dont want to craft anything")
    print("-"*25)
    command = input("Insert option here: \n").lower()

    if command == "crowbar" and metal > 1:
        craft_crowbar()
    elif command == "shovel" and metal > 0 and stick > 0:
        craft_shovel()
    elif command == "guard outfit" and white_outfit > 0 and blue_dye > 0:
        craft_guard_outfit()
    elif command == "keycard" and circuit_board > 0 and battery > 0:
        craft_keycard()
    elif command == "back":
        cell_time()
    else:
        print("hmmm, seems like that option isn't available to craft, try again")
        craft_items()


def craft_crowbar():
    global metal, crowbar
    metal = metal - 2
    crowbar = True
    print("\n")
    print("-"*25)
    print("You successfully manage to craft a crowbar \n")
    cell_time()


def craft_shovel():
    global shovel, stick, metal
    metal = metal - 1
    stick = stick - 1
    shovel = True

    print("\n")
    print("-"*25)
    print("You successfully manage to craft a shovel")
    print("-" * 25)

    cell_time()


def craft_guard_outfit():
    global blue_dye, white_outfit, guard_outfit
    blue_dye = blue_dye - 1
    white_outfit = white_outfit - 1
    guard_outfit = True

    print("\n")
    print("-"*25)
    print("You successfully manage to craft a guard outfit")
    print("-" * 25)

    cell_time()


def craft_keycard():
    global circuit_board, battery, keycard
    circuit_board = circuit_board - 1
    battery = battery - 1
    keycard = True

    print("\n")
    print("-"*25)
    print("You successfully manage to craft a keycard ")
    print("-" * 25)

    cell_time()


def escape_options():
    print("\n")
    print("-" * 25)
    crafted_inventory()
    print("Next:")
    print("you decide that tonight is the night to strike and take action and escape")
    print("what method of escape will you use ")
    print("-"*25)
    print("crowbar: requires a crafted crowbar")
    print("keycard: requires a crafted keycard")
    print("shovel: requires a crafted shovel")
    print("guard outfit: requires a crafted guard outfit")
    print("riot : requires a reputation of 100")
    print("back: nevermind I change my mind")
    print("-"*25)

    user = input("Input your method of escape here:\n")

    print("-"*25)
    if user == "crowbar" and crowbar == True:
        crowbar_escape()
    elif user == "keycard" and keycard == True:
        keycard_escape()
    elif user == "shovel" and shovel == True:
        shovel_escape()
    elif user == "guard_outfit" and guard_outfit == True:
        outfit_escape()
    elif user == "riot" and reputation > 99:
        riot_escape()
    elif user == "back":
        cell_time()
    else:
        print("Hmmm, seems like you didnt have the item for that escape. Please try again")
        escape_options()

#escape options


def crowbar_escape():
    print("\n")
    print("-"*25)
    print("You begin to start wedging your crowbar against the window bars, hoping for an easy path to victory ")
    print("while in the process, you accidentally catch one of the guards attention due to the sound of scraping metal.")
    print("Alarms start blaring, as you start to panic guards rush into your cell, immediatly dragging you to solitary")
    print("confinment for the rest of your sentence, you question if you made the right decision, siting in a room of nothingness")
    print("*"*25)
    print("The End")
    print("*"*25)


def keycard_escape():
    print("\n")
    print("-" * 25)
    print("before the cells lock up and lights turn off, you take your handcrafted keycard with you in your pocket.")
    print("Entering the main foyer, you attempt to act casually, while aproaching your destination of the back gates.")
    print("Abruptly you start to make a run for it opening doors with your keycard, outpacing guards ")
    print("following in pursuit. Successfully escaping from the prison.")
    print("*"*25)
    print("The End")
    print("*"*25)


def shovel_escape():
    print("\n")
    print("-" * 25)
    print("A few hours after lights go out, you grab your shovel and get to digging your way out of the prison. ")
    print("upon hours of grueling work, you finally manage to dig a hole leading past the prison boundaries")
    print("nearing sunrise.Successfully escaping the prison.")
    print("*"*25)
    print("The End")
    print("*"*25)


def outfit_escape():
    print("\n")
    print("-" * 25)
    print("While no guards looking around, you quickly change into your guard outfit as your cellmate wishes you luck")
    print("walking out, you blend in with the rest of the guards,calmly walking outwards the front gates and exiting without suspicions")
    print("*"*25)
    print("The End")
    print("*"*25)


def riot_escape():
    print("\n")
    print("-" * 25)
    print("out of nowhere, you and the inmates start chanting towards forming a riot")
    print("with the others looking up to you as lead, you start a fury of fighting, outnumbering the guards.")
    print("After some time passes, you start to lead the inmates towards the front gates where everyone")
    print("collectivly breaks the entrance, successfully escaping the prison")
    print("*"*25)
    print("The End")
    print("*"*25)


def next_day():
    print("\n")
    print(" -" * 25)
    print("you decide to immediately go sleep, jumping into bed covering")
    print("yourselves with warm fuzzy sheets. Awaiting for tomorrow's adventure")

    time.sleep(3)
    print("-"*25)
    begin()


#inventory commands

def add_random_item():
    global metal, circuit_board, battery, white_outfit, blue_dye, stick
    pick_item = random.randint(1, 6)
    if pick_item == 1:
        metal = metal + 1
    elif pick_item == 2:
        circuit_board = circuit_board + 1
    elif pick_item == 3:
        battery = battery + 1
    elif pick_item == 4:
        white_outfit = white_outfit + 1
    elif pick_item == 5:
        blue_dye = blue_dye + 1
    elif pick_item == 6:
        stick = stick + 1


def print_inventory():
    print("-" * 25)
    print("Inventory:")
    print(f'Metal : {metal}')
    print(f'Circuit board: {circuit_board}')
    print(f'Battery: {battery}')
    print(f'White Outfit: {white_outfit}')
    print(f'Blue Dye: {blue_dye}')
    print(f'Stick: {stick}')
    print("-" * 25)

def crafted_inventory():
    print("-" * 25)
    print("Inventory:")
    print(f'Crowbar : {crowbar}')
    print(f'Shovel: {shovel}')
    print(f'Keycard: {keycard}')
    print(f'Guard Outfit: {guard_outfit}')

    print("-" * 25)

#main

#trackers:
global health, reputation, pstrike, day
health = 60
reputation = 50
pstrike = 0
day = 0

#items

global metal, circuit_board, battery, white_outfit, blue_dye, stick
metal = 0
circuit_board = 0
battery = 0
white_outfit = 0
blue_dye = 0
stick = 1

##craftable items
global crowbar, shovel, keycard, guard_outfit
crowbar = False
shovel = False
keycard = False
guard_outfit = False

game_start()

