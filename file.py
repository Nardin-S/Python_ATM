import tkinter
import time


#global variables
counter = 0
flag = 1
var=0    
#FFlag = 0
Newpass= 0 
NotMatch = 0
#-----------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------#
     
def UserOptions():
    
    
     def Cash():
        #Top_Cash_Window()
        Cash_Service = tkinter.Toplevel()
        Cash_Service.title("Cash Service")
        Cash_Service.geometry("600x450+150+150")
        Cash_Service.configure(background = "steelblue")
        Cash_Service.resizable(False,False)
        
        Label = tkinter.Label(Cash_Service , font=("Times New Roman", 14),text = "Enter Cash Amount: " , width = 20 , bg = "steelblue" )
        Label.place(x = 90, y = 140)
        
        CashAmount = tkinter.Entry( Cash_Service,font=("Times New Roman", 12),bg = "steelblue" )
        CashAmount.place(x =170, y =180)
        CashAmount.place(width = 180, height =30)
        def ATM_Actuator_Out(Cash_amoutt):
            print("Please , Wait for the money to be out")
            
        def Check_Balance():
            if ((int(CashAmount.get())) <= CustomersInfo[CurrentID][2]) and ((int(CashAmount.get()))%100 == 0) and ((int(CashAmount.get())) < 5000) :
                    
                    ATM_Actuator_Out((int(CashAmount.get())))
                    file = open('Data.txt' , 'r+')
                    update = file.readlines()
                    #print(update)
                    file.close()
                    print(iterator)
                    var = int(update[iterator + 24]) - int(CashAmount.get())
                    CustomersInfo[CurrentID][2] = var
                    update[iterator + 24] = str(var) 
                    file = open('Data.txt' , 'w')
                    file.writelines( update)
                    file.close()
                    ThankYou()
                            
            elif(((int(CashAmount.get())) > CustomersInfo[CurrentID][2]) ):
                
                Insuffficient = tkinter.Toplevel()
                Insuffficient.title("Message")
                Insuffficient.geometry("600x450+150+150")
                Insuffficient.configure(background = "steelblue")
                Insuffficient.resizable(False,False)
                
        
                Label = tkinter.Label(Insuffficient , font=("Times New Roman", 17),text = "** Insufficient Balance ** " , width = 20 , bg = "steelblue" )
                Label.place(x = 140, y = 140)
                Button= tkinter.Button(Insuffficient ,text="Back",command = HomeWindow  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
                Button.place(x =220 , y =240)
                
                
                            
                    
            else :
                Label = tkinter.Label(Cash_Service , font=("Times New Roman", 17),text = "This Value is not Allowed  " , width = 40 , bg = "steelblue" )
                Label.place(x = 30, y = 100)
                Label = tkinter.Label(Cash_Service , font=("Times New Roman", 14),text = "Please, Re-enter Cash Value : " , width = 40 , bg = "steelblue" )
                Label.place(x = 70, y = 140)
       #------------------------------------------------------------------------------------------------------------------------------------------#         
        def ThankYou() :
        
              EndWindow = tkinter.Toplevel()
              EndWindow.title("Thank you")
              EndWindow.geometry("600x450+150+150")
              EndWindow.configure(background = "steelblue")
              EndWindow.resizable(False,False)
    
              LabelEnd1 = tkinter.Label(EndWindow , font=("Times New Roman", 18),text = "**  Operation is Successfully Done ** " , width = 40 ,bg = "steelblue" )
              LabelEnd1.place(x = 50, y = 100)
              LabelEnd = tkinter.Label(EndWindow , font=("Times New Roman", 17),text = ".. Thank you .." , width = 20 ,bg = "steelblue" )
              LabelEnd.place(x = 150, y = 200)
    
              Button= tkinter.Button(EndWindow ,text="Back",command = HomeWindow ,font=(17), width= 7 , height = 1 , bg = "lightblue")
              Button.place(x =420 , y =340)
                
       #------------------------------------------------------------------------------------------------------------------------------------------#     
        Button= tkinter.Button(Cash_Service , text="OK",command = Check_Balance  ,font=(10), width= 7 , height = 1 , bg = "lightblue")
        Button.place(x =180 , y =240)
                                  
        Button= tkinter.Button(Cash_Service , text="Cancel",command = HomeWindow  ,font=(10), width= 7 , height = 1 , bg = "lightblue")
        Button.place(x =300 , y =240)
        
       # Cash_Service.mainloop()
    #------------------------------------------------------------------------------------------------------------------------------------------
    # ******************************************************************************************************************************************#     
     def PassChange():
            
            ChangePass = tkinter.Toplevel()
            ChangePass.title("Change Password")
            ChangePass.geometry("600x450+150+150")
            ChangePass.configure(background = "steelblue")
            ChangePass.resizable(False,False)
            title = tkinter.Label(ChangePass , font=("Modern", 25),text = "__** Change Password **__" , width = 40 , bg = "steelblue" )
            title.place(x = 30, y = 50)
            def Enter2():
                global NotMatch
                global Newpass
                print(Newpass)
                print("Hey2")
                if (int(EnterNewPW1.get()) == Newpass) :
                    NotMatch =0
                    file = open('Data.txt' , 'r+')
                    update = file.readlines()
                    #print(update)
                    file.close()
                    print(iterator)
                    CustomersInfo[CurrentID][1] = Newpass
                    update[iterator + 16] = str(Newpass)+'\n'
                    file = open('Data.txt' , 'w')
                    file.writelines( update)
                    file.close()
                    #print("tmam")  
                    for widget in ChangePass.winfo_children():
                                widget.destroy()
                    title = tkinter.Label(ChangePass , font=("Times New Roman", 20),text = "** Password is successully changed ** " , width = 40 , bg = "steelblue" )
                    title.place(x = 20, y = 150)
                    ButtonBack= tkinter.Button(ChangePass ,text="Back",command = HomeWindow  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
                    ButtonBack.place(x =250 , y =340)
                else :
                    #global NotMatch
                    NotMatch =1
                    PassChange()
                    
            def Enter1():
                if (len(EnterNewPW1.get()) == 4) : 
                    global Newpass
                    print(Newpass)
                    print("Hey")
                    Newpass = int(EnterNewPW1.get())
                    EnterNewPW1.delete(0, 'end')
                else :
                   title = tkinter.Label(ChangePass , font=("Times New Roman", 17),text = "** Invalid length of password ** " , width = 40 , bg = "steelblue" )
                   title.place(x = 20, y = 110)
                   return
                
                print(Newpass)
                #ChangePass.destroy()
                title = tkinter.Label(ChangePass , font=("Times New Roman", 17),text = "Re-Enter New password " , width = 20 , bg = "steelblue" )
                title.place(x = 20, y = 170)
                Button= tkinter.Button(ChangePass ,text="Enter",command = Enter2  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
                Button.place(x =190 , y =300)
                
            if(NotMatch == 1):
                title = tkinter.Label(ChangePass , font=("Times New Roman", 20),text = "Entries are not Matched,Enter Again" , width = 40 , bg = "steelblue" )
                title.place(x = 20, y = 110)
                
            title = tkinter.Label(ChangePass , font=("Times New Roman", 17),text = "New Password : " , width = 20 , bg = "steelblue" )
            title.place(x = 20, y = 170)
            Button= tkinter.Button(ChangePass ,text="Enter",command = Enter1  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
            Button.place(x =190 , y =300)
            ButtonBack= tkinter.Button(ChangePass ,text="Back",command = HomeWindow  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
            ButtonBack.place(x =350 , y =300)
            #LLIMIT Entry input
            var = tkinter.StringVar()
            max_len = 4
            #observe input
            def on_write(*args):
                s = var.get()
                if len(s) > max_len:
                    var.set(s[:max_len])
            var.trace_variable("w", on_write)
            EnterNewPW1 = tkinter.Entry( ChangePass, textvariable=var , show = '*')
            EnterNewPW1.place(x =200, y =230)
            EnterNewPW1.place(width = 180, height =25)
           
    

            
         
            print("CHANGE")
    #------------------------------------------------------------------------------------------------------------------------------------------
    # ******************************************************************************************************************************************#      
     def BalanceInquiry():
            print("1000")
            BalanceInquiry = tkinter.Toplevel()
            BalanceInquiry.title("Message")
            BalanceInquiry.geometry("600x450+150+150")
            BalanceInquiry.configure(background = "steelblue")
            BalanceInquiry.resizable(False,False)
            title = tkinter.Label(BalanceInquiry , font=("Modern", 25),text = "__Balance__" , width = 40 , bg = "steelblue" )
            title.place(x = 10, y = 100)
            fullName = tkinter.Label(BalanceInquiry , font=("Times New Roman",23),text = CustomersInfo[CurrentID][0] , width = 30 , bg = "steelblue" )
            fullName.place(x =12, y = 160)
            Balance = tkinter.Label(BalanceInquiry , font=("Times New Roman",17),text = "Your Balance : " + str(CustomersInfo[CurrentID][2])+" L.E" , width = 25 , bg = "steelblue" )
            Balance.place(x = 100, y = 250)
            Button= tkinter.Button(BalanceInquiry ,text="OK",command = HomeWindow  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
            Button.place(x =270 , y =340)
            #BalanceInquiry.destroy()
                
            
          
    #------------------------------------------------------------------------------------------------------------------------------------------
    # ******************************************************************************************************************************************#       
     def FFawry():
         print("which")
         FAWRY = tkinter.Toplevel()
         FAWRY.title("Options List")
         FAWRY.geometry("600x450+150+150")
         FAWRY.configure(background = "steelblue")
         FAWRY.resizable(False,False)
         
         title = tkinter.Label(FAWRY , font=("Modern", 25),text = "__Choose Fawry Service__" , width = 40 , bg = "steelblue" )
         title.place(x = 10, y = 50)

         def FawryFunction():
               def GO_Check():
                  if (len(EnterPhone.get()) == 11) : 
                    if ((int(EnterBalance.get())) <= CustomersInfo[CurrentID][2]) :
                        Data = open('Data.txt' , 'r+')
                        B_update = Data.readlines()
                        #print(update)
                        Data.close()
                        print(iterator)
                        var = int(B_update[iterator + 24]) - int(EnterBalance.get())
                        CustomersInfo[CurrentID][2] = var
                        B_update[iterator + 24] = str(var) 
                        Data = open('Data.txt' , 'w')
                        Data.writelines( B_update)
                        Data.close()
                        FAWRY.destroy()
                        EndWindow = tkinter.Toplevel()
                        EndWindow.title("Thank you")
                        EndWindow.geometry("600x450+150+150")
                        EndWindow.configure(background = "steelblue")
                        EndWindow.resizable(False,False)
    
                        LabelEnd1 = tkinter.Label(EndWindow , font=("Times New Roman", 18),text = "**  Operation is Successfully Done ** " , width = 40 ,bg = "steelblue" )
                        LabelEnd1.place(x = 50, y = 100)
                        LabelEnd = tkinter.Label(EndWindow , font=("Times New Roman", 17),text = ".. Thank you .." , width = 20 ,bg = "steelblue" )
                        LabelEnd.place(x = 150, y = 200)
    
                        Button= tkinter.Button(EndWindow ,text="Back",command = HomeWindow ,font=(17), width= 7 , height = 1 , bg = "lightblue")
                        Button.place(x =420 , y =340)
                    
                        
                    else :
                        BalanceInsuff = tkinter.Toplevel()
                        BalanceInsuff.title("Options List")
                        BalanceInsuff.geometry("600x450+150+150")
                        BalanceInsuff.configure(background = "steelblue")
                        BalanceInsuff.resizable(False,False)
                        LabelB = tkinter.Label(BalanceInsuff , font=("Times New Roman", 17),text = "Insufficient Balance to complete this operation " , width = 40 , bg = "steelblue" )
                        LabelB.place(x = 5, y = 140)
                        BackButton= tkinter.Button(BalanceInsuff ,text="Back",command = HomeWindow  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
                        BackButton.place(x =220 , y =340)
                  else :
                      EnterPhone.delete(0, 'end')
                      title = tkinter.Label(FAWRYSer , font=("Times New Roman", 17),text = "** Invalid length of Phone Number, Reenter it ** " , width = 40 , bg = "steelblue" )
                      title.place(x = 40, y = 300)
                      return
               
               FAWRYSer = tkinter.Toplevel()
               FAWRYSer.title("Services List")
               FAWRYSer.geometry("600x450+150+150")
               FAWRYSer.configure(background = "steelblue")
               FAWRYSer.resizable(False,False)
               if (Fawwry.get() == 1):
                   title = tkinter.Label(FAWRYSer , font=("Modern", 25),text = "__ Orange Service __" , width = 40 , bg = "steelblue" )
                   title.place(x = 10, y = 50)
               elif  (Fawwry.get() == 2):
                    title = tkinter.Label(FAWRYSer , font=("Modern", 25),text = "__ Etisalat Service __" , width = 40 , bg = "steelblue" )
                    title.place(x = 10, y = 50)
               elif  (Fawwry.get() == 3):
                    title = tkinter.Label(FAWRYSer , font=("Modern", 25),text = "__ Vodafone Service __" , width = 40 , bg = "steelblue" )
                    title.place(x = 10, y = 50)
               else :
                   title = tkinter.Label(FAWRYSer , font=("Modern", 25),text = "__ WE Service __" , width = 40 , bg = "steelblue" )
                   title.place(x = 10, y = 50)
                   
                
               
               Phonenum = tkinter.Label(FAWRYSer , font=("Times New Roman", 18),text = "Phone Number :" , width = 20 , bg = "steelblue" )
               Phonenum.place(x = 10, y = 100)
               #LLIMIT Entry input
               phone_Num = tkinter.StringVar()
               max_len = 11
                #observe input
               def on_write(*args):
                    s = phone_Num.get()
                    if len(s) > max_len:
                        phone_Num.set(s[:max_len])
               phone_Num.trace_variable("w", on_write)
               EnterPhone = tkinter.Entry( FAWRYSer,textvariable = phone_Num)
               EnterPhone.place(x =250, y =110)
               EnterPhone.place(width = 180, height =25)
               
               BalanceEnter = tkinter.Label(FAWRYSer , font=("Times New Roman", 18),text = "Balance :" , width = 20 , bg = "steelblue" )
               BalanceEnter.place(x = 10, y = 200)
               EnterBalance = tkinter.Entry( FAWRYSer)
               EnterBalance.place(x =250, y =210)
               EnterBalance.place(width = 180, height =25)
               Button= tkinter.Button(FAWRYSer ,text="Enter",command =GO_Check ,font=(17), width= 7 , height = 1 , bg = "lightblue")
               Button.place(x =270 , y =340)
               
                     
               
         def OrangeFunction():
            FawryFunction()
         def EtFunction():
            FawryFunction()
         def VodFunction():
            FawryFunction()
         def WEFunction():
            FawryFunction()
            
        
            #command = GO_Check
         Fawwry = tkinter.IntVar()
     
         OrangeButton = tkinter.Radiobutton(FAWRY, text = "Orange Recharge ", bg = "steelblue",font=("Times New Roman", 15), command = OrangeFunction, value = 1, variable = Fawwry)
         OrangeButton.place(x =80, y =100)

         EtislatButton = tkinter.Radiobutton(FAWRY, text = "Etisalat Recharge", bg = "steelblue", font=("Times New Roman", 15),command = EtFunction, value = 2, variable = Fawwry)
         EtislatButton.place(x =80, y =150)

         VodafoneButton = tkinter.Radiobutton(FAWRY, text = "Vodafone Recharge", bg = "steelblue",font=("Times New Roman", 15),command = VodFunction, value = 3, variable = Fawwry)
         VodafoneButton.place(x =80, y =200)

         WEButton = tkinter.Radiobutton(FAWRY, text = "We Recharge. ",bg = "steelblue",font=("Times New Roman", 15),command =WEFunction, value = 4, variable = Fawwry)
         WEButton.place(x =80, y =250)

     
         
    #------------------------------------------------------------------------------------------------------------------------------------------
    # ******************************************************************************************************************************************#       
     def Exit():
          UserWindow.destroy()
    #------------------------------------------------------------------------------------------------------------------------------------------
    # ****************************************************************************************************************************************** 
     def HomeWindow():
         UserWindow.destroy()
         UserOptions()
    #--------------------------------------------------------------------------------------------------------------------#    
     UserWindow = tkinter.Tk()
     UserWindow.title("Options List")
     UserWindow.geometry("600x450+150+150")
     UserWindow.configure(background = "steelblue")
     UserWindow.resizable(False,False)
     
     title = tkinter.Label(UserWindow , font=("Modern", 25),text = "___* Services *___" , width = 40 , bg = "steelblue" )
     title.place(x = 10, y = 60)

     options = tkinter.IntVar()
     
     CashButton = tkinter.Radiobutton(UserWindow, text = "Cash ", bg = "steelblue",font=("Times New Roman", 15), command = Cash, value = 1, variable = options )
     CashButton.place(x =370, y =170)

     ChangePassButton = tkinter.Radiobutton(UserWindow, text = "Password Change", bg = "steelblue", font=("Times New Roman", 15),command = PassChange, value = 2, variable = options )
     ChangePassButton.place(x =370, y =250)

     BalanceButton = tkinter.Radiobutton(UserWindow, text = "Balance Inquiry", bg = "steelblue",font=("Times New Roman", 15),command = BalanceInquiry, value = 3, variable = options )
     BalanceButton.place(x =140, y =170)

     FawryServicesButton = tkinter.Radiobutton(UserWindow, text = "Fawry Services ",bg = "steelblue",font=("Times New Roman", 15),command =FFawry, value = 4, variable =options )
     FawryServicesButton.place(x =140, y =250)

     ExitButton = tkinter.Radiobutton(UserWindow, text = "Exit", bg = "steelblue", font=("Times New Roman", 15),command = Exit, value = 5, variable = options )
     ExitButton.place(x =290, y =300)
     
     UserWindow.mainloop()


#-----------------------------------------------------------------------------------#           



           
#-----------------------------------------------------------------------------------#
def lockedWindow():
    
        LockedAccount = tkinter.Toplevel()
        LockedAccount.title("Message")
        LockedAccount.geometry("600x450+150+150")
        LockedAccount.configure(background = "steelblue")
        LockedAccount.resizable(False,False)
       
        def Exit():
               AccountNum.destroy()
        MSG = tkinter.Label(LockedAccount , font=("Times New Roman", 20),text = "Your Account is Locked ," , width = 40 , bg = "steelblue" )
        MSG.place(x = 5, y = 140)
        MSG = tkinter.Label(LockedAccount , font=("Times New Roman", 20),text = "Please go to the Branch " , width = 40 , bg = "steelblue" )
        MSG.place(x = 5, y = 200)
        
        ButtonBack= tkinter.Button(LockedAccount ,text="Close",command = Exit  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
        ButtonBack.place(x =350 , y =300)
        
    
#-----------------------------------------------------------------------------------#
def Password() :
    global counter
    global flag
    global iterator
    
    
    def Check_PW() :
        global counter
        global flag
   
        while(counter < 3) :
        
            if ((int(EnterPW.get())) ==  CustomersInfo[CurrentID][1]):
                flag = 0
                AccountNum.destroy()
                UserOptions()
                #print("done")
                break
            
            else :
                counter += 1 
               # print("Wrong")
               # print(counter)
                Password_Window.destroy()
                Password()
                break
                #PASSWORD_MSG.place(x = 120, y = 170)
                
    
            #print(counter)    
    Password_Window = tkinter.Toplevel()
    Password_Window.title("PASSWORD")
    Password_Window.geometry("600x450+150+150")
    Password_Window.configure(background = "steelblue")
    Password_Window.resizable(False,False)    
    
    if (counter > 0) :
        PASSWORD_MSG = tkinter.Label(Password_Window , font=("Arial", 15),text = "Incorrect Password, Try again"  , width = 40 , bg = "steelblue" )
        PASSWORD_MSG.place(x = 90, y = 130)
        PASSWORD_MSG = tkinter.Label(Password_Window , font=("Arial", 13),text = "Enter your Password "  , width = 40 , bg = "steelblue" )
        PASSWORD_MSG.place(x = 90, y = 170)
        
    else : 
        PASSWORD_MSG = tkinter.Label(Password_Window , font=("Arial", 15),text = "Welcome.. "+((CustomersInfo[int(EnterNumber.get())][0]))  , width = 40 , bg = "steelblue" )
        PASSWORD_MSG.place(x = 90, y = 130)
        PASSWORD_MSG = tkinter.Label(Password_Window , font=("Arial", 13),text = "Please ,Enter your Password "  , width = 40 , bg = "steelblue" )
        PASSWORD_MSG.place(x = 120, y = 170)
    passchar = tkinter.StringVar()
    max_len = 4
    #observe input
    def on_write(*args):
        s = passchar.get()
        if len(s) > max_len:
            passchar.set(s[:max_len])
    passchar.trace_variable("w", on_write)
           
    EnterPW = tkinter.Entry( Password_Window,show = '*',textvariable =passchar )
    EnterPW.place(x =200, y =200)
    EnterPW.place(width = 180, height =25)
    Button= tkinter.Button(Password_Window , text="OK",command = Check_PW ,font=(10), width= 8 , height = 1 , bg = "lightblue")
    Button.place(x =240 , y =240)
    print(counter)
    
    if (counter == 3) : 
        
        Password_Window.destroy()
        lockedWindow()    
        file = open('AccoutStatus.txt' , 'r+')
        edit = file.readlines()
        #print(edit)
        file.close()
        edit[iterator] = "Locked\n"
        file = open('AccoutStatus.txt' , 'w')
        file.writelines(edit )
        
        #LockedAccount.destroy()
        

        return 
 
    
   # global CurrentID
   
#-----------------------------------------------------------------------------------#
def Check_AccountNum():
    
    global iterator
    global CurrentID

    iterator = 0
    
    #for writing in Status file later---------
   
    for x in CustomersInfo :                 #
        if ((int(EnterNumber.get()))== x ):  #
            break                            #
        else:                                #
            iterator+=1                      #iterator = 8 if ID not exist
    # -------------------------------------- # 
    print("iterator"+str(iterator))
    #print(CurrentID) 
    def Exit():
          AccountNum.destroy()      
    if (int(EnterNumber.get())) in CustomersInfo :
        
        CurrentID = int(EnterNumber.get())
        if (Accountstatus[CurrentID] == "Locked") :
            print("locked")
            LockedAccount = tkinter.Toplevel()
            LockedAccount.title("Message")
            LockedAccount.geometry("600x450+150+150")
            LockedAccount.configure(background = "steelblue")
            LockedAccount.resizable(False,False)
            
       
            MSG = tkinter.Label(LockedAccount , font=("Arial", 20),text = "Your Account is Locked ," , width = 40 , bg = "steelblue" )
            MSG.place(x = 5, y = 140)
            MSG = tkinter.Label(LockedAccount , font=("Arial", 20),text = "Please go to the Branch " , width = 40 , bg = "steelblue" )
            MSG.place(x = 5, y = 200)
            
            ButtonBack= tkinter.Button(LockedAccount ,text="Close",command = Exit  ,font=(17), width= 7 , height = 1 , bg = "lightblue")
            ButtonBack.place(x =350 , y =300)
            
        else :
            
            #print(Accountstatus[CurrentID])
            Password()
            #print(counter)
    else :
        EnterNumber.delete(0, 'end')
        Acount_Number = tkinter.Label(AccountNum , font=("Arial", 15),text = "The Entered Account Number is Incorrect" , width = 40 , bg = "steelblue" )
        Acount_Number.place(x = 100, y = 100)
        Acount_Number = tkinter.Label(AccountNum ,font=("Arial", 15), text = "Please , Enter it Again" , width = 40 , bg = "steelblue" )
        Acount_Number.place(x = 100, y = 140)
        
        
        return
    #print(CurrentID)
    #print(iterator)
#-----------------------------------------------------------------------------------#
        
#-------------------------------------- MAIN --------------------------------------#
#Informations Dict. List :
#CustomersInfo = {ID : [NAME , Password, Balance] }
#Accountstatus = {Open / locked}
Accountstatus = {}
CustomersInfo  = {} 
CurrentID = 0
iterator = 0

#CuurentID = 0 

file = open('Data.txt' , 'r+')
AccountS = open('AccoutStatus.txt' , 'r+')

for i in range(8):
    x= file.readline()
    Accountstatus[int(x)] = []
    CustomersInfo[int(x)] = []
j=0
content = file.read().splitlines()
Locked = AccountS.read().splitlines()
for x in CustomersInfo :
     CustomersInfo[x] = [str(content[j]) , int(content[j+8]) , int(content[j+16])]
     Accountstatus[x] = Locked[j]
     j+=1
#print(Accountstatus)
#print(CustomersInfo)

#-------------------------------------------------------------------------------------------------------------------------#
# Main window #
AccountNum = tkinter.Tk()
AccountNum.title("MAIN")
AccountNum.geometry("600x450+150+150")
AccountNum.configure(background = "steelblue")
AccountNum.resizable(False,False)

#LABEL : Enter Account Number
Acount_Number = tkinter.Label(AccountNum , text = "Please , Enter Account Number " , font=("Arial", 15), width = 40 , bg = "steelblue" )
Acount_Number.place(x = 100, y = 140)

#Entry : To get input from User
EnterNumber= tkinter.Entry( AccountNum)
EnterNumber.place(x =220, y =190)
EnterNumber.place(width = 180, height =25)

#On enter : go to check input account number
Button= tkinter.Button(AccountNum , text="Enter",command =Check_AccountNum ,font=(10), width= 10 , height = 2 , bg = "lightblue")
Button.place(x =260 , y =240)


AccountNum.mainloop()

#__________________________________________________________________________________________________________________________________#
#----------------------------------------------------------------------------------------------------------------------------------#