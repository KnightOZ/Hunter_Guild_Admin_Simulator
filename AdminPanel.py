# main application
import Administrators as a
import Hunters as h
import Gates as g
import Backend as b

admin  = a.adminLogin(a.adminList)  # Log the ADMIN/USER into the system | store the ADMIN's object into admin
acclvl = a.checkAccLvl(a.adminList, admin)

if acclvl == 1:
    a.regPanel(admin, acclvl)

if acclvl == 3:
    a.headPanel(admin, acclvl)
