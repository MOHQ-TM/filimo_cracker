#RuN -_-
import Color as c , Logo , Cambo , UseRL , UseR 
class Crack():
    def __init__(self):
        Logo.Logo()
        self.s=str(input(f"{c.C}RuN {c.R}({c.C}Cambo {c.G}Or {c.C}UseR_OnE {c.G}Or {c.C}UseRLeeCheR{c.R}) {c.G}=> {c.C}"))
        #Run
        self.CheCk()
    #Check
    def CheCk(self):
        if self.s=="Cambo":
            Cambo.CamBo().__init__()
        elif self.s == "UseR_OnE":
            UseR.UseR().__init__()
        elif self.s == "UseRLeeCheR":
            UseRL.UseRLeeCheR().__init__()
        else:
            print(f"{c.R}ErroR {c.G}-_-{c.W}\n")
            exit()
Crack()
