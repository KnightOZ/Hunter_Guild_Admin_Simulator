import os       # importing os for system realism and the cleansing of terminal
import time     # importing time for system realism

class Gate():
    gate_ID   = ""
    gate_rank = ''
    gate_name = ""
    gate_type = ''
    gate_cap  = 0
    gate_pop  = 0

    def gateData(self):
        data = "-Gate Data-\n|ID: %s\n|Rank: %s\n|Name: %s\n|Type: %s\n|Capacity: %d\n|Population: %d" % (self.gate_ID,self.gate_rank,self.gate_name,self.gate_type,self.gate_cap,self.gate_pop)
        return data

    def gateID(self):   # return gate ID
        return self.gate_ID
    
    def gateRank(self): # return gate rank
        return self.gate_rank

    def gateName(self): # return gate type
        return self.gate_name

    def gateType(self): # return gate type
        return self.gate_type
    
    def gateCap(self):  # return gate cap
        return self.gate_cap

    def gatePop(self):
        return self.gate_pop
    
def gatesNum(gdb):  # returns how many gates are recorded in gate_db
    counter = 0 # counter for gates

    for x in gdb: # loop through gdb and iterate the num of gates stored inside
        counter+=1

    print("| Gates stored in database: %s" % counter)

def allGateData(gdb):  # returns how many gates are recorded in gate_db
    for x in gdb:
        print(x.gateData(), "\n")

def returnGate(gdb, inp): # find and return Gate Obj
    try:
        for x in gdb:
            if x.gateID() == inp.upper():
                return x
    except:
        print("| Error86: Gate '%s' wasn't found or isn't recognised by our system." % inp)

def findGate(gdb, inp): # find Gate by ID, have to be precise via a given database.
    count = 0 # counter for error checker
    try:
        for x in gdb:
            if x.gateID() == inp.upper():
                count+=1
                return True
            
        if count == 0:
            return False

    except:
        print("| Error86: Input contains incorrect format. Contact supervisor if error repeats.")

def getGate(gdb, inp): # return Gate Data by ID, used in menus
    try:
        for x in gdb:
            if x.gateID() == inp.upper():
                print(x.gateData())
    except:
        print("| Error83: Gate '%s' wasn't found or isn't recognised by our system." % inp)

def gatesPop():
    for x in gate_db:
        print(x.gatePop())

def addPop(goc):   # add (+1) to the population of the gate of choice
    goc.gate_pop += 1
    return goc # return the sum

def minusPop(goc): # minus (-1) to the population of the gate of choice
    goc.gate_pop -= 1

    if goc.gate_pop < 0: # preventing the population from being less than 0 as that makes 0 sense :)
        goc.gate_pop = 0
    return goc # return the sum

# gate database - contains all gates that the Hunters Guild are aware of
gate_db = []

# creating gates
g0 = Gate()
g0.gate_ID = "GT00"
g0.gate_rank = "N/A"
g0.gate_name = "Hunter's Guild - Seoul"
g0.gate_type = 'N/A'
g0.gate_cap  = 100
g0.gate_pop  = 30

g1 = Gate()
g1.gate_ID   = "GT01"
g1.gate_rank = 'A'
g1.gate_name = "Minato District - Tokyo"
g1.gate_type = 'Du'
g1.gate_cap  = 8
g1.gate_pop  = 0

g2 = Gate()
g2.gate_ID   = "GT02"
g2.gate_rank = 'E'
g2.gate_name = "Downtown - New York"
g2.gate_type = 'Du'
g2.gate_cap  = 5
g2.gate_pop  = 0

g3 = Gate()
g3.gate_ID   = "GT03"
g3.gate_rank = 'B'
g3.gate_name = "Ogimi - Okinawa"
g3.gate_type = 'Du'
g3.gate_cap  = 5
g3.gate_pop  = 0

g4 = Gate()
g4.gate_ID   = "GT04"
g4.gate_rank = 'E'
g4.gate_name = "Jeju - Jeju-Do"
g4.gate_type = 'Du'
g4.gate_cap  = 5
g4.gate_pop  = 0

g5 = Gate()
g5.gate_ID   = "GT05"
g5.gate_rank = 'C'
g5.gate_name = "Rio De Janerio - Brazil"
g5.gate_type = 'Du'
g5.gate_cap  = 8
g5.gate_pop  = 0

g6 = Gate()
g6.gate_ID   = "GT06"
g6.gate_rank = 'D'
g6.gate_name = "Gothenburg - Sweden"
g6.gate_type = 'Ra'
g6.gate_cap  = 10
g6.gate_pop  = 0

g7 = Gate()
g7.gate_ID   = "GT07"
g7.gate_rank = 'B'
g7.gate_name = "London - United Kingdom"
g7.gate_type = 'Du'
g7.gate_cap  = 10
g7.gate_pop  = 0

g8 = Gate()
g8.gate_ID   = "GT08"
g8.gate_rank = 'S'
g8.gate_name = "Kyoto - Japan"
g8.gate_type = 'Ra'
g8.gate_cap  = 15
g8.gate_pop  = 0

g9 = Gate()
g9.gate_ID   = "GT09"
g9.gate_rank = 'S'
g9.gate_name = "Moscow - Russia"
g9.gate_type = 'Du'
g9.gate_cap  = 8
g9.gate_pop  = 0

gate_db.append(g0)
gate_db.append(g1)
gate_db.append(g2)
gate_db.append(g3)
gate_db.append(g4)
gate_db.append(g5)
gate_db.append(g6)
gate_db.append(g7)
gate_db.append(g8)
gate_db.append(g9)
