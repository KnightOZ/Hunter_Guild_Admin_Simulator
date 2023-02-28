import os       # importing os for system realism and the cleansing of terminal
import time     # importing time for system realism

class Hunter():
    ID = ""
    rank = ''
    role = 0
    name = ""
    spec = ""
    wepn = ""
    loc  = "GT00"

    def hntrCard(self):  # return details of Hunter chosen
        card = "-Hunter Card-\n| ID: %s\n| Rank: %s\n| Role: %d\n| Name: %s\n| Class: %s\n| Weapon: %s\n" % (self.ID,self.rank,self.role,self.name,self.spec,self.wepn)
        return card

    def hntrID(self):    # return hunter ID
        return self.ID
    
    def hntrName(self):  # return hunter Name
        return self.name

    def hntrRank(self):  # return hunter Rank
        return self.rank

    def hntrRole(self):  # return hunter Role
        return self.role

    def hntrGate(self) : # return hunter Location
        return self.loc

def returnHunter(hdb, inp): # find and return Gate Obj
    try:
        for x in hdb:
            if x.hntrID() == inp.upper():
                return x
    except:
        print("| Error00: Hunter '%s' wasn't found or isn't recognised by our system." % inp)

def returnLocations(lsdb): # return all current hunter locations
    for a, b in lsdb.items():
        print(a, b)


def findID(hdb, hoc): # find Hunter by ID, have to be precise via a given database.
    count = 0 # counter for error checker
    try:
        for x in hdb:
            if x.hntrID() == hoc.upper():
                count+=1
                return count

        if count == 0:
            return count

    except:
        print("| Error86: Input contains incorrect format. Contact supervisor if error repeats.")
        return count

def getHunter(hdb, inp): # return Hunter Card by ID, used in menus
    try:
        for x in hdb:
            if x.hntrID() == inp.upper():
                print(x.hntrCard())
    except:
        print("| Error24: Hunter '%s' wasn't found or isn't recognised by our system." % inp)

def findName(hdb, inp): # find Hunter by Name, have to be precise via a given database.
    try:
        for x in hdb:
            if x.hntrName().upper() == inp.upper():
                print(x.hntrCard())
    except:
        print("| Error02: ID '%s' wasn't found or isn't recognised by our system." % inp)

def findRole(hdb, rol): # find tank, dd or healer hunters via a given database.
    count = 0 # counter for error checker
    for x in hdb:
        if x.hntrRole() == 1 and x.hntrRole() == rol: # TANK ROLE
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(),x.hntrRank()))
            count+=1

        if x.hntrRole() == 2 and x.hntrRole() == rol: # DAMAGE DEALER ROLE
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(),x.hntrRank()))
            count+=1

        if x.hntrRole() == 3 and x.hntrRole() == rol: # HEALER ROLE
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(),x.hntrRank()))
            count+=1

    if count == 0:
        print("| Error03: Role '%s' wasn't found or isn't recognised by our system." % rol)
        return

    print("\n| '%s' Role(s) found: %d " % (rol, count))

def findRank(hdb, rnk): # function to find specific ranks in the Hunter's Guild via a given database.
    count = 0 # counter for error checker
    for x in hdb:
        if x.hntrRank() == 'S+' and x.hntrRank() == rnk.upper(): # S+ RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1

        elif x.hntrRank() == 'S' and x.hntrRank() == rnk.upper():  # S RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1
        
        elif x.hntrRank() == 'A' and x.hntrRank() == rnk.upper():  # A RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1

        elif x.hntrRank() == 'B' and x.hntrRank() == rnk.upper():  # B RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1

        elif x.hntrRank() == 'C' and x.hntrRank() == rnk.upper():  # C RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1

        elif x.hntrRank() == 'D' and x.hntrRank() == rnk.upper():  # D RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1

        elif x.hntrRank() == 'E' and x.hntrRank() == rnk.upper():  # E RANK
            print("|| ID: %s || Name: %s, Role: %d, Rank: %s" % (x.hntrID(),x.hntrName(),x.hntrRole(), x.hntrRank()))
            count+=1
        
    if count == 0:
        print("| Error04: Rank '%s' wasn't found or isn't recognised by our system." % rnk)
        return

    print("\n| %s Rank(s) found: %d " % (rnk, count))
        
# hunter database - contains all hunters registered with the Hunters Guild (only contains the objects)
hntr_db = []

# creating Hunter objects/cards
hntr1 = Hunter()
hntr1.ID = "HNTR01"
hntr1.rank = 'S+'
hntr1.role = 1
hntr1.name = "Mikael Frostwolf"
hntr1.spec = "Knight"
hntr1.wepn = "Greatsword"

hntr2 = Hunter()
hntr2.ID = "HNTR02"
hntr2.rank = 'S'
hntr2.role = 2
hntr2.name = "Zia"
hntr2.spec = "Brawler"
hntr2.wepn = "Gauntlets"

hntr3 = Hunter()
hntr3.ID = "HNTR03"
hntr3.rank = 'S'
hntr3.role = 2
hntr3.name = "Zed"
hntr3.spec = "Assassin"
hntr3.wepn = "Daggers"

hntr4 = Hunter()
hntr4.ID = "HNTR04"
hntr4.rank = 'C'
hntr4.role = 3
hntr4.name = "Nora"
hntr4.spec = "Woman"
hntr4.wepn = "Dishwasher"

hntr5 = Hunter()
hntr5.ID = "HNTR05"
hntr5.rank = 'E'
hntr5.role = 2
hntr5.name = "Mima-moon"
hntr5.spec = "Medic"
hntr5.wepn = "Bandage"

hntr6 = Hunter()
hntr6.ID = "HNTR06"
hntr6.rank = 'S+'
hntr6.role = 1
hntr6.name = "Jaeju"
hntr6.spec = "Knight"
hntr6.wepn = "Single Sword"

hntr7 = Hunter()
hntr7.ID = "HNTR07"
hntr7.rank = 'E'
hntr7.role = 3
hntr7.name = "Melissa Mochi"
hntr7.spec = "Priest"
hntr7.wepn = "Holy Book"

hntr8 = Hunter()
hntr8.ID = "HNTR08"
hntr8.rank = 'E'
hntr8.role = 2
hntr8.name = "Burza Konis"
hntr8.spec = "Warrior"
hntr8.wepn = "AR"

hntr9 = Hunter()
hntr9.ID = "HNTR09"
hntr9.rank = 'B'
hntr9.role = 2
hntr9.name = "Tyo"
hntr9.spec = "Ranger"
hntr9.wepn = "LMG"

hntr10 = Hunter()
hntr10.ID = "HNTR10"
hntr10.rank = 'E'
hntr10.role = 3
hntr10.name = "Sung Jin Woo"
hntr10.spec = "Squire"
hntr10.wepn = "Longsword"

hntr11 = Hunter()
hntr11.ID = "HNTR11"
hntr11.rank = 'A'
hntr11.role = 1
hntr11.name = "Rude"
hntr11.spec = "Knight"
hntr11.wepn = "Tower Shield"

hntr12 = Hunter()
hntr12.ID = "HNTR12"
hntr12.rank = 'S'
hntr12.role = 2
hntr12.name = "Copege Mercury"
hntr12.spec = "Axemaster"
hntr12.wepn = "Great Axe"

hntr13 = Hunter()
hntr13.ID = "HNTR13"
hntr13.rank = 'A'
hntr13.role = 3
hntr13.name = "Utoki"
hntr13.spec = "Priest"
hntr13.wepn = "Staff"

hntr14 = Hunter()
hntr14.ID = "HNTR14"
hntr14.rank = 'A'
hntr14.role = 2
hntr14.name = "Renji "
hntr14.spec = "Ronin"
hntr14.wepn = "Katana"

hntr15 = Hunter()
hntr15.ID = "HNTR15"
hntr15.rank = 'B'
hntr15.role = 3
hntr15.name = "Mess"
hntr15.spec = "Support"
hntr15.wepn = "Boomerang"

hntr16 = Hunter()
hntr16.ID = "HNTR16"
hntr16.rank = 'S+'
hntr16.role = 2
hntr16.name = "Rudeus"
hntr16.spec = "Wizard"
hntr16.wepn = "Staff"

hntr17 = Hunter()
hntr17.ID = "HNTR17"
hntr17.rank = 'C'
hntr17.role = 1
hntr17.name = "Huet"
hntr17.spec = "Warrior"
hntr17.wepn = "Great Sword"

hntr18 = Hunter()
hntr18.ID = "HNTR18"
hntr18.rank = 'C'
hntr18.role = 2
hntr18.name = "Schizskai Rentio"
hntr18.spec = "Assassin"
hntr18.wepn = "Daggers"

hntr19 = Hunter()
hntr19.ID = "HNTR19"
hntr19.rank = 'D'
hntr19.role = 2
hntr19.name = "William Turner"
hntr19.spec = "Pirate"
hntr19.wepn = "Scimitar"

hntr20 = Hunter()
hntr20.ID = "HNTR20"
hntr20.rank = 'C'
hntr20.role = 2
hntr20.name = "Jack Sparrow"
hntr20.spec = "Pirate"
hntr20.wepn = "Flintlock"

hntr21 = Hunter()
hntr21.ID = "HNTR21"
hntr21.rank = 'D'
hntr21.role = 3
hntr21.name = "Joseph"
hntr21.spec = "Priest"
hntr21.wepn = "Holy Book"

hntr22 = Hunter()
hntr22.ID = "HNTR22"
hntr22.rank = 'D'
hntr22.role = 2
hntr22.name = "Saskia"
hntr22.spec = "Ranger"
hntr22.wepn = "Bow and Arrows"

hntr23 = Hunter()
hntr23.ID = "HNTR23"
hntr23.rank = 'C'
hntr23.role = 2
hntr23.name = "Kara"
hntr23.spec = "Assassin"
hntr23.wepn = "Daggers"

hntr24 = Hunter()
hntr24.ID = "HNTR24"
hntr24.rank = 'D'
hntr24.role = 2
hntr24.name = "Jun Dokja"
hntr24.spec = "Swordsman"
hntr24.wepn = "Dual Swords"

hntr25 = Hunter()
hntr25.ID = "HNTR25"
hntr25.rank = 'D'
hntr25.role = 1
hntr25.name = "Becca Prentice"
hntr25.spec = "Knight"
hntr25.wepn = "Sword and Shield"

hntr26 = Hunter()
hntr26.ID = "HNTR26"
hntr26.rank = 'D'
hntr26.role = 2
hntr26.name = "Carla"
hntr26.spec = "Ninja"
hntr26.wepn = "Daggers"

hntr27 = Hunter()
hntr27.ID = "HNTR27"
hntr27.rank = 'E'
hntr27.role = 1
hntr27.name = "David"
hntr27.spec = "Knight"
hntr27.wepn = "Sword and Shield"

hntr28 = Hunter()
hntr28.ID = "HNTR28"
hntr28.rank = 'E'
hntr28.role = 1
hntr28.name = "Rees Jenkins"
hntr28.spec = "Warrior"
hntr28.wepn = "Greataxe"

hntr29 = Hunter()
hntr29.ID = "HNTR29"
hntr29.rank = 'E'
hntr29.role = 2
hntr29.name = "Jane"
hntr29.spec = "Banshee"
hntr29.wepn = "Mouth"

hntr30 = Hunter()
hntr30.ID = "HNTR30"
hntr30.rank = 'E'
hntr30.role = 2
hntr30.name = "Loki"
hntr30.spec = "Martial Artist"
hntr30.wepn = "Gauntlets"

rankDict = { # rank dictionary to assist with logic with rank checking function(s)
    "S+" : 7,
    "S"  : 6,
    "A"  : 5,
    "B"  : 4,
    "C"  : 3,
    "D"  : 2,
    "E"  : 1
}

# appending Hunter objects/cards to hntr_db
hntr_db.append(hntr1)
hntr_db.append(hntr2)
hntr_db.append(hntr3)
hntr_db.append(hntr4)
hntr_db.append(hntr5)
hntr_db.append(hntr6)
hntr_db.append(hntr7)
hntr_db.append(hntr8)
hntr_db.append(hntr9)

hntr_db.append(hntr10)
hntr_db.append(hntr11)
hntr_db.append(hntr12)
hntr_db.append(hntr13)
hntr_db.append(hntr14)
hntr_db.append(hntr15)
hntr_db.append(hntr16)
hntr_db.append(hntr17)
hntr_db.append(hntr18)
hntr_db.append(hntr19)

hntr_db.append(hntr20)
hntr_db.append(hntr21)
hntr_db.append(hntr22)
hntr_db.append(hntr23)
hntr_db.append(hntr24)
hntr_db.append(hntr25)
hntr_db.append(hntr26)
hntr_db.append(hntr27)
hntr_db.append(hntr28)
hntr_db.append(hntr29)
hntr_db.append(hntr30)
