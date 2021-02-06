from tkinter import *
from Store_num import Store
from Conversion import convert
from Module_GUI2 import Mdule2

class Module1_GUI:

    # Status Bar Text Change function
    def status_change(self,s1):
        self.status.configure(text = "Status : "+s1)

    # Validation Function
    def number_changed(self,str1):
        if str1.isdigit() == True:
            Temp_number = int(str1)
            if Temp_number <= 1000 and Temp_number >=0:
                return True
            else:
                self.status_change("Error out of range (0-1000)")
                return False
        else:
            self.status_change("Error plz enter an Integer")
            return False
        self.fresult.config(text ="-")

    #Event for Number 1       
    def for_num1(self,event):
        if self.number_changed(str(self.V1.get()))==True:
            self.status_change("1st Number Updated")
            self.lnum1.configure(text="1st number : "+str(self.V1.get()))
            self.n1 = Store(self.V1.get())
            self.n1.IsNull=False
        else :
            self.lnum1.configure(text="Enter 1st Number")
            self.V1.set("")
            self.n1.IsNull=True

    #Event for Number 2
    def for_num2(self,event):
        if self.number_changed(str(self.V2.get()))==True:
            self.status_change("2st Number Updated")
            self.lnum2.configure(text="2and number : "+str(self.V2.get()))
            self.n2 = Store(self.V2.get())
            self.n2.IsNull=False
        else :
            self.lnum2.configure(text="Enter 2and Number")
            self.V2.set("")
            self.n2.IsNull=True
    
    # Result Calculation
    def Cal_Result(self):
        if self.n1.IsNull==True or self.n2.IsNull==True :
            self.status_change("Error plz enter The numbers")
        else :
            c1 = convert(self.n1.dic['Binary'],self.n2.dic['Binary'],int(self.data.get()),self.n1.dic['count'],self.n2.dic['count'])
            self.res = Store(self.n1.to_decimal(c1.get_result()))
            self.fresult.config(text = self.res.dic['Number'])
            self.status_change("Done .... Result has benn Calculated")

    # OPen Explation Module
    def Explain(self):
        if self.n1.IsNull==True or self.n2.IsNull==True :
            self.status_change("Error plz enter The numbers")
        else:
            New_win = Toplevel(self.Module1)
            Exp = Mdule2(New_win,int(self.data.get()),self.n1,self.n2,self.res)
            #exp=Mdule2(New_win,1,1,1,1)
            New_win.mainloop()

    # Status OF Gates
    def Radio_change (self):
        if self.data.get() == 7 :
            self.num2.configure(state=DISABLED)
            self.status_change("Entry Box 2 is DISABLED for NOT Gate")
            self.V2.set(0)
            self.n2 = Store(0)
        else:
            self.num2.configure(state=NORMAL)
            self.status_change(self.Listr[int(self.data.get())-1] + " Gate selected")
        print(self.data.get())

    def __init__ (self,Module1):


        Module1.geometry("620x620")
        Module1.title("Logic Micro Operation")
        Module1.configure(bg="#b8c8c8")
        Module1.resizable(False,False)
        
        self.Module1 = Module1
        self.V1 = StringVar()
        self.V2 = StringVar()
        self.data = IntVar()
        self.data.set(1)
        self.Listr = ['NAND','NOR','XOR','XNOR','AND','OR','NOT']

        self.n1 = Store(0)
        self.n2 = Store(0)
        
        #..... LOGO .....
        self.phlo = PhotoImage(file = r"images\logical-operations-logo.PNG")
        self.logo = Label(Module1,image=self.phlo,bg="#c8c0c0")
        self.logo.pack(fill=X)

        # .... BODY ......
        self.Body = Frame(Module1,bg="#b8c8c8")
        self.Body.pack(fill='both',expand=1)

        #Row 1
        self.num1 = Entry(self.Body,relief=FLAT,justify= CENTER,font=("Broadway",16),bg="#405858",fg="white", textvariable=self.V1)
        self.num1.bind("<Return>",self.for_num1)
        self.num1.bind("<Tab>",self.for_num1)
        self.num1.bind("<Button-1>",self.for_num2)
        self.num1.grid(row=0,column=0,columnspan=2,padx=(15, 10),pady=(15, 15))
        self.num2 = Entry(self.Body,relief=FLAT,justify= CENTER,font=("Broadway",16),bg="#405858",fg="white",textvariable=self.V2)
        self.num2.grid(row=0,column=2,columnspan=2,padx=(10, 15),pady=(15, 15))
        self.num2.bind("<Return>",self.for_num2)
        self.num2.bind("<Tab>",self.for_num2)
        self.num2.bind("<Button-1>",self.for_num1)

        #Row 2
        self.lnum1 = Label(self.Body,font=("Britannic bold",16),bg="#b8c8c8",text="Enter 1st Number")
        self.lnum1.grid(row=1,column=0,columnspan=2,padx=(15, 10),pady=(15, 15))
        self.lnum2 = Label(self.Body,text="Enter 2and Number ",font=("Britannic bold",16),bg="#b8c8c8")
        self.lnum2.grid(row=1,column=2,columnspan=2,padx=(15, 10),pady=(15, 15))

        # Row 3
        self.Nand_gate = Radiobutton(self.Body,text="NAND",bg="#b8c8c8",font=("Century bold",13),value=1, variable=self.data,command=self.Radio_change)
        self.Nand_gate.grid(row=2,column=0,padx=(15, 10),pady=(15, 10))

        self.Nor_gate = Radiobutton(self.Body,text="NOR",bg="#b8c8c8",font=("Century bold",13),value=2, variable=self.data,command=self.Radio_change)
        self.Nor_gate.grid(row=2,column=1,padx=(15, 10),pady=(15, 10))

        self.Xor_gate = Radiobutton(self.Body,text="XOR",bg="#b8c8c8",font=("Century bold",13),value=3, variable=self.data,command=self.Radio_change)
        self.Xor_gate.grid(row=2,column=2,padx=(15, 10),pady=(15, 10))

        self.XNor_gate = Radiobutton(self.Body,text="XNOR",bg="#b8c8c8",font=("Century bold",13),value=4, variable=self.data,command=self.Radio_change)
        self.XNor_gate.grid(row=2,column=3,padx=(15, 10),pady=(15, 10))

        # Row 4
        self.And_gate = Radiobutton(self.Body,text="AND",bg="#b8c8c8",font=("Century bold",13),value=5, variable=self.data,command=self.Radio_change)
        self.And_gate.grid(row=3,column=0,padx=(15, 10),pady=(15, 15))

        self.OR_gate = Radiobutton(self.Body,text="OR",bg="#b8c8c8",font=("Century bold",13),value=6, variable=self.data,command=self.Radio_change)
        self.OR_gate.grid(row=3,column=1,padx=(15, 10),pady=(15, 15))

        self.Not_gate = Radiobutton(self.Body,text="NOT",bg="#b8c8c8",font=("Century bold",13),value=7, variable=self.data,command=self.Radio_change)
        self.Not_gate.grid(row=3,column=2,padx=(15, 10),pady=(15, 15))

        #Row 5
        self.Result_btn = Button(self.Body,text= " Result ",font=("Britannic bold",16),command=self.Cal_Result)
        self.Result_btn.grid(row=4,column=0,columnspan=2,padx=(15, 10),pady=(15, 15))

        self.Explanation_btn = Button(self.Body,text=" Explanation ",font=("Britannic bold",16),command=self.Explain)
        self.Explanation_btn.grid(row=4,column=2,columnspan=2,padx=(15, 10),pady=(15, 15))

        #Row 6
        self.lresult = Label(self.Body,font=("Britannic bold",16),bg="#b8c8c8",text="Result is : ")
        self.lresult.grid(row=5,column=0,columnspan=2,padx=(15, 10),pady=(15, 15),stick=E)

        self.fresult = Label(self.Body,font=("Britannic bold",16),bg="#b8c8c8",text=" - ")
        self.fresult.grid(row=5,column=2,columnspan=2,padx=(15, 10),pady=(15, 15),stick=W)

        self.Body.bind("<Button-1>",self.for_num1)
        self.Body.bind("<Button-1>",self.for_num2)

        # .... Status Bar .....
        self.status = Label(Module1,text="Status : ",bd=1,relief=SUNKEN,anchor=W,bg="#202840",fg="white",font=("Consolas", 15))
        self.status.pack(side=BOTTOM,fill=X)   