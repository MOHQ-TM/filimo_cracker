#•_|•
import Logo , Color as c , LogiN
#-_-
class UseR():
    def __init__(self):
        Logo.Logo()
        self.user=str(input(f"{c.C}UseRNamE {c.R}=> {c.G}"))
        self.User()
    #UseR
    def User(self):
        pas=open(input(f"{c.C}Password {c.R}=> {c.G}"),"r")
        for i in pas:
            i=i.strip()
            LogiN.LogiN().log(self.user,i)

