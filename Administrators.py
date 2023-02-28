import time     # importing time for system realism
import os       # importing os for system realism and the cleansing of terminal
import pwinput as pw # importing pwinput for password masking

import Hunters as h
import Gates as g
import Backend as b

class Admin():
    usern = ""
    passw = ""
    acc_lvl = 0

    def get_user(self):         # return self.username
        return self.usern

    def get_password(self):     # return self.password
        return self.passw

    def get_acclvl(self):
        return self.acc_lvl     # return self.acc_lvl

def findUser(adlist, username):   # find the desired user and return them in object form.
    for usr in adlist:
        if usr.usern == username:
            return usr
    return None

def checkUser(adlist, username):  # check if the username provided is in the database (adminList)
    try:
        for usr in adlist:
            if usr.usern == username:
                return True
    except:
        return False
    
def checkPass(adlist, password):  # check if the password provided is in the database (adminList)
    try:
        for pas in adlist:
            if pas.passw == password:
                return True
    except:
        return False

def checkAccLvl(adlist, admin):     # function to return
    try:
        acclvl = admin.get_acclvl()

        if acclvl == 1:
            return 1

        if acclvl == 3:
            return 3
    except:
        print("| Access level Error: seek advice from software provider.")

def adminLogin(adlist): # function for the admin to login to the simulation
    while True:
        os.system('cls')
        usrn = input("|| Username: ")
        pasw = pw.pwinput("|| Password: ")

        if checkUser(adlist, usrn) == True:
            if checkPass(adlist, pasw) == True:
                os.system('cls')
                print("| Welcome back %s." % (usrn))
                time.sleep(2)
                os.system('cls')
                return findUser(adlist, usrn)

            else:
                print("| Username or password doesn't exist in our system. Please try again.")
                time.sleep(2)
        else:
            print("| Username or password doesn't exist in our system. Please try again.")
            time.sleep(2)

def adminLogout(adlist): # function for the admin to logout of the simulation
    adminLogin(adlist)

a1 = Admin() # default details
a1.usern = "ADMIN01"
a1.passw = "0"
a1.acc_lvl  = 1

headAdmin = Admin()
headAdmin.usern = "HEADADMIN"
headAdmin.passw = "1"
headAdmin.acc_lvl = 3

adminList = []

adminList.append(a1)
adminList.append(headAdmin)

##########################################################################################
####################      Functions Regarding Acc Lvl Admins      ########################
##########################################################################################

# To keep access level in a business secure, employees should only be able to see and do what is 
# permitted to their access level. They should NOT be able to view what a higher access level can do
# this is for security reasons within an organisation and ties with the Data Protection Act.
def regPanel(admin, acclvl): # Menu Permitted to Access Level 1
    try:
        choice = ''
        if acclvl == 1:
            while choice != 'q':
                menu = """
                | Hunter's Guild Admin System |
                | 1. Hunters
                | 2. Gates
                | 3. Hunter Gate Transfer
                |
                | q. Logout
                """
                print(menu)
                choice = input("|| Admin: ")

                if choice == '1': 
                    os.system('cls')
                    b.hunterMenu_1()
                elif choice == '2': 
                    os.system('cls')
                    b.gateMenu_1()
                elif choice == '3': 
                    os.system('cls')
                    b.transferMenu_1()
                elif choice.lower() == 'q':
                    os.system('cls')
                    print("| Logging out...")
                    time.sleep(1.5)
                else:
                    print("| That option doesn't exist. Try again.")
                    time.sleep(1.5)
                    os.system('cls')
    except:
        print("| Panel error01: seek advice from software provider.")

def headPanel(admin, acclvl):
    try:
        if acclvl == 3:
            while True:
                pass
    except:
        print("| Panel error02: seek advice from software provider.")
