#-_-
import requests as r , Logo , Color as c , re
#•_•
class UseRLeeCheR():
    #Session
    req=r.session()
    def __init__(self):
        Logo.Logo()
        self.s=str(input(f"{c.C}RuN UseRLeeCheR On {c.R}({c.G}Defulte {c.C}Or {c.G}Client{c.R}) {c.C}=> {c.G}"))
        self.UseR()
    #UseR
    def UseR(self):
        if self.s == "Defulte":
            url="https://www.filimo.com/"
            #Req
            req=UseRLeeCheR.req.get(url).text
            #-_-
            ok=re.findall('https://www.filimo.com/m/\w{5}',req)
            #•=•
            link=set(ok)
            #For 
            for i in link:
                #Req
                req=UseRLeeCheR.req.get(i).text
                #-_-
                user=re.findall('"name": "(.*)"',req)
                #•|•
                for num in user:
                    #__
                    open("File/UseR_Def.txt","a+").write(f"{num}\n")
        elif self.s == "Client":
            f=open(input(f"{c.C}UrL_LisT {c.R}=> {c.G}"),"r")
            for i in f:
                req=UseRLeeCheR.req.get(i.strip()).text
                user=re.findall('"name": "(.*)"',req)
                user=user.strip()
                open("File/Cli_UseR.txt","r").write(f"{user}\n")
        else:
            print(f"{c.R}ErroR {c.G}-_-\n{c.W}")
            exit()


