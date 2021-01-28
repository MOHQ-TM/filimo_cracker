#-_-
import Color as c , Logo , LogiN
#///
class CamBo():
    def __init__(self):
        Logo.Logo()
        self.Cambo=open(input(f"{c.C}Cambo {c.R}=> {c.G}"),"r")
        self.Cm()
    #Cambo
    def Cm(self):
        for i in self.Cambo:
            i=i.strip()
            i=i.split(":")
            try:
                user=i[0]
                password=i[1]
            except:
                continue
            LogiN.LogiN().log(user,password)

