## Module that contains data on what gate the current Hunters are present in
# Designed to assist AdminPanel with transferring Hunters from gate a to gate b vice versa
import os       # importing os for system realism and the cleansing of terminal
import time     # importing time for system realism

import Hunters as h
import Gates as g

# hoc = Hunter of Choice | goc = Gate of Choice
def checkHunter(lsdb, hdb, hoc, goc): # check if hunter is not already in the same gate
    hntTemp = h.returnHunter(hdb, hoc)
    for hid, gid in lsdb.items():
        if hid == hntTemp.ID:
            if gid != goc:  # check if hunter is not already in the Gate of Choice
                return True # hunter is eligible to travel
    return False # hunter is NOT eligible to travel

def checkGateCap(gatedb, goc): # check a gate's capacity to prevent limit exceeding
    gate = g.returnGate(gatedb, goc)
    if gate.gatePop() < gate.gateCap():
        return True
    else:
        return False

def checkRank(hntrdb, gatedb, hoc, goc): # check goc rank and hoc rank to ensure the hunter is qualified
    gate   = g.returnGate(gatedb, goc)   # store goc rank x
    hunter = h.returnHunter(hntrdb, hoc) # store hoc rank x
    gateNum = 0 # to store logic flag for qualification | gate
    hntrNum = 0 # to store logic flag for qualification | hunter

    try:
        for rnk, rnkNum in rnks.items(): # obtain gateNum
            if gate.gateRank() == rnk:
                gateNum = rnkNum
                break

        for rnk, rnkNum in rnks.items(): # obtain hntrNum
            if hunter.hntrRank() == rnk:
                hntrNum = rnkNum
                break

        if hntrNum >= gateNum: # check if hunter qualified to enter gate.
            return True

        else:
            return False
    
    except:
         print("| Error99: Issue with checking qualification eligibility. Contact Supervisor.")

def updateWorld(lsdb, hdb, gtdb, hoc, goc): # update Hunter of Choice to Gate of Choice
    gateTemp   = g.returnGate(gtdb, goc)    # store goc object
    hunterTemp = h.returnHunter(hdb, hoc)   # store hoc object
    currentLoc = g.returnGate(gtdb, hunterTemp.hntrGate()) # store hoc goc

    for hid, gid in lsdb.items():  # transferring hunter of choice to gate of choice
        if hid == hoc:
            g.minusPop(currentLoc) # - 1 pop to current location of hunter
            hunterTemp.loc = goc   # changing the hunters location in goc population
            lsdb[hoc] = goc        # changing the hunters location in lockstat db for verificaiton later
            g.addPop(gateTemp)     # + 1 pop to goc
            break
    
    return hunterTemp

def gateHop(hntrdb, gatedb, lsdb, hoc, goc): # transfer hunters from one gate to another, requires ID
    if h.findID(hntrdb, hoc) == 1: # check if hunter is valid in database
        if g.findGate(gatedb, goc) == 1: # check if gate is valid in database
            if checkHunter(lsdb, hntrdb, hoc, goc) == True: # check if the hoc is valid and can travel to goc
                if checkGateCap(gatedb, goc) == True: # check gateCap is exceeded
                    if checkRank(hntrdb, gatedb, hoc, goc) == True:
                        updateWorld(lsdb, hntrdb, gatedb, hoc, goc)
                        print("Hunter '%s' successfully transferred to gate '%s'." % (hoc, goc))
                    else:
                        print("| Hunter '%s' is not qualified to enter gate '%s'." % (hoc, goc))
                else:
                    print("| Gate '%s' capacity is has already been exceeded." % goc)
            else:          
                print("| Hunter '%s' is already present in gate '%s'. Try a different gate." % (hoc, goc))
        else:
            print("| Gate '%s' wasn't found or isn't recognised by our system." % goc)
    else:
        print("| Hunter '%s' wasn't found or isn't recognised by our system." % hoc)

lockStat = {   # lockStat, short for location status - dictionary to keep track of hunters and their current lock stat
    h.hntr1.hntrID() : h.hntr1.hntrGate(),
    h.hntr2.hntrID() : h.hntr2.hntrGate(),
    h.hntr3.hntrID() : h.hntr3.hntrGate(),
    h.hntr4.hntrID() : h.hntr4.hntrGate(),
    h.hntr5.hntrID() : h.hntr5.hntrGate(),
    h.hntr6.hntrID() : h.hntr6.hntrGate(),
    h.hntr7.hntrID() : h.hntr7.hntrGate(),
    h.hntr8.hntrID() : h.hntr8.hntrGate(),
    h.hntr9.hntrID() : h.hntr9.hntrGate(),
    
    h.hntr10.hntrID() : h.hntr10.hntrGate(),
    h.hntr11.hntrID() : h.hntr11.hntrGate(),
    h.hntr12.hntrID() : h.hntr12.hntrGate(),
    h.hntr13.hntrID() : h.hntr13.hntrGate(),
    h.hntr14.hntrID() : h.hntr14.hntrGate(),
    h.hntr15.hntrID() : h.hntr15.hntrGate(),
    h.hntr16.hntrID() : h.hntr16.hntrGate(),
    h.hntr17.hntrID() : h.hntr17.hntrGate(),
    h.hntr18.hntrID() : h.hntr18.hntrGate(),
    h.hntr19.hntrID() : h.hntr19.hntrGate(),

    h.hntr20.hntrID() : h.hntr20.hntrGate(),
    h.hntr21.hntrID() : h.hntr21.hntrGate(),
    h.hntr22.hntrID() : h.hntr22.hntrGate(),
    h.hntr23.hntrID() : h.hntr23.hntrGate(),
    h.hntr24.hntrID() : h.hntr24.hntrGate(),
    h.hntr25.hntrID() : h.hntr25.hntrGate(),
    h.hntr26.hntrID() : h.hntr26.hntrGate(),
    h.hntr27.hntrID() : h.hntr27.hntrGate(),
    h.hntr28.hntrID() : h.hntr28.hntrGate(),
    h.hntr29.hntrID() : h.hntr29.hntrGate(),

    h.hntr30.hntrID() : h.hntr30.hntrGate(),
}

hdb  = h.hntr_db
gdb  = g.gate_db
rnks = h.rankDict

##########################################################################################
###################      Function(s) Regarding Acc Lvl Admins      #######################
##########################################################################################

def hunterMenu_1():
    c_choice = ''
    try:
        while c_choice != 'b':
            menu = """
            | Hunter Menu |
            | 1. Location of all Hunters
            | 2. Find Hunter by ID
            | 3. Find Hunter by Name
            | 4. Find Role Specific Hunters
            | 5. Find Rank Specific Hunters
            |
            | b. Back
            """
            print(menu)
            c_choice = input("|| You: ")

            if c_choice == '1': # Location of all Hunters - 1
                os.system('cls')
                h.returnLocations(lockStat)
            elif c_choice == '2': # Find a Hunter by ID - 2
                os.system('cls')
                c_choice = input("|| Hunter ID: ")
                h.getHunter(h.hntr_db, c_choice)
            elif c_choice == '3': # Find a Hunter by Name - 3
                os.system('cls')
                print("")
                c_choice = input("|| Hunter's FULL NAME (as presented on card): ")
                h.findName(h.hntr_db, c_choice)
            elif c_choice == '4': # Find Role Specific Hunters - 4
                os.system('cls')
                c_choice = input("|| Role (1-TNK, 2-DPS, 3-SUP): ")
                h.findRole(h.hntr_db, int(c_choice))
            elif c_choice == '5': # Find Rank Specific Hunters - 5
                os.system('cls')
                print("""
                | Ranks:
                | S+
                | S
                | A
                | B
                | C
                | D
                | E
                """)
                c_choice = input("|| Rank: ")
                h.findRank(hdb, c_choice)

            elif c_choice.lower() == 'b': # Back to main menu - B
                os.system('cls')
            else:
                print("| That option doesn't exist. Try again.")
                time.sleep(1.5)
                os.system('cls')
                    
    except:
        print("| Panel error03: seek advice from software provider.")

def gateMenu_1():
    c_choice = ''
    try:
        while c_choice != 'b':
            menu = """
            | Gate Menu |
            | 1. All Gate Data
            | 2. Find Gate by ID
            | 3. Stored Gates in database
            |
            | b. Back
            """
            print(menu)
            c_choice = input("|| You: ")

            if c_choice == '1': # print all gate data - 1
                os.system('cls')
                g.allGateData(g.gate_db)
            elif c_choice == '2': # find a stored gate via ID - 2
                os.system('cls')
                c_choice = input("|| Gate ID: ")
                g.getGate(g.gate_db, c_choice)
            elif c_choice == '3': # print num of all gates stored in database - 3
                os.system('cls')
                g.gatesNum(g.gate_db)

            elif c_choice.lower() == 'b': # Back to main menu
                os.system('cls')
            else:
                print("| That option doesn't exist. Try again.")
                time.sleep(1.5)
                os.system('cls')
                    
    except:
        print("| Panel error04: seek advice from software provider.")

def transferMenu_1():
    h_inp = "" # store hunter of choice
    g_inp = "" # store gate of choice
    c_choice = ''
    try:
        while c_choice != 'b':
            menu = """
            | Gate Transfer |
            | 1. Insert/Change Hunter ID
            | 2. Insert/Change Gate ID
            | 
            | Hunter: %s
            | Gate: %s
            |
            | T. Transfer Hunter
            |
            | b. Back
            """ % (h_inp, g_inp)

            print(menu)
            c_choice = input("|| You: ")

            if c_choice == '1': # print all gate data - 1
                os.system('cls')
                h_inp = input("|| Insert Hunter ID: ")
            elif c_choice == '2': # find a stored gate via ID - 2
                os.system('cls')
                g_inp = input("|| Insert Gate ID: ")
                g.getGate(g.gate_db, c_choice)
            elif c_choice.upper() == 'T': # print num of all gates stored in database - 3
                os.system('cls')
                gateHop(h.hntr_db, g.gate_db, lockStat, h_inp, g_inp)

            elif c_choice.lower() == 'b': # Back to main menu
                os.system('cls')
            else:
                print("| That option doesn't exist. Try again.")
                time.sleep(1.5)
                os.system('cls')
                    
    except:
        print("| Panel error05: seek advice from software provider.")