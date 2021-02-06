from tkinter import *
from Conversion import convert
from Store_num import Store

class Mdule2:

    def Display_str(self,L1,Lmax):
        temp=" "
        for x in range(Lmax-1,-1,-1):
            temp = temp + str(L1[x]) +" "
        return temp
    
    def Draw_Table(self,window,opr):

        for x in range (3):
            DFrame = Frame (window , bg = "#ffb400"  ,width=45, height=45,highlightbackground="black", highlightthickness=1 )
            DFrame.grid(row = 0 , column= x)
            DFrame.pack_propagate(False)
            l1 = Label(DFrame , bg = "#ffb400" ,font=("Arial Rounded MT bold",22))
            if(x==0):
                l1.configure(text="A")
            elif(x==1):
                l1.configure(text="B")
            else:
                l1.configure(text="Y")
            l1.pack(expand =1)

        for x in range (4):
            a = 0 if x < 2 else 1
            b = 0 if x%2==0 else 1
            ans = convert([a],[b],opr,1,1) 
            for y in range(3):
                DFrame = Frame (window , bg = "#ffd656"  ,width=45, height=45,highlightbackground="black", highlightthickness=1 )
                DFrame.grid(row = x+1 , column= y)
                DFrame.pack_propagate(False)
                l2 = Label (DFrame,bg = "#ffd656" ,font=("Arial Rounded MT ",20))
                if(y==0):
                    l2.configure(text=str(a))
                elif(y==1):
                    l2.configure(text=str(b) if opr != 7 else "-")
                else:
                    l2.configure(text=str(ans.result[0]))
                l2.pack(expand =1)
                
                
    def Grid_Complete(self, gr,x,y,w,h):
       
        #F1 = Frame (gr , bg = "#d6d5c9"  ,width=130*w, height=60*h,highlightbackground="green", highlightcolor="green", highlightthickness=1 )
        F1 = Frame (gr , bg = "#d6d5c9"  ,width=130*w, height=60*h)
        F1.grid(row = y , column= x,stick=W,rowspan=h,)
        F1.pack_propagate(False)
        return F1


    def __init__ (self, Window ,opr,num1,num2,Res):


        print (num1.dic['Number'],num2.dic['Number'],Res.dic['Number'])
        print(num2)

        Window.configure (bg = "#d6d5c9")

        Window.geometry("900x500")

        Window.resizable(False,False)

        self.Listr = ['NAND','NOR','XOR','XNOR','AND','OR','NOT']

        # .. Top ...
        Top_Header = Label(Window, text = "Explanation Logic", bg="#591f0a" ,fg ="#efa00b", font=("Britannic bold",26), pady = 10)
        Top_Header.pack(fill = X)


        # ... BODY ... 
        self.Body = Frame (Window ,bg = "#d6d5c9")
        self.Body.pack(fill='both')

        
        self.L1 = Label (self.Grid_Complete(self.Body,0,0,2,1), text="Number 1 : "+num1.dic['Number'],font=("Britannic bold",18),bg = "#d6d5c9" ) 
        self.L1.pack( expand = 1)
        
        self.NLF1 = Frame(self.Grid_Complete(self.Body,0,1,2,1), highlightbackground="black" , highlightthickness=1 )
        self.NLF1.pack(side = RIGHT)
        self.NL1 = Label (self.NLF1 , text=self.Display_str(num1.dic['Binary'],max(num1.dic['count'],num2.dic['count'])),font=("Britannic bold",16),bg = "#FFFFFF")  
        self.NL1.pack( expand = 1)

        self.NLF2 = Frame(self.Grid_Complete(self.Body,0,2,2,1), highlightbackground="black" , highlightthickness=1 )
        self.NLF2.pack(side = RIGHT )
        self.NL2 = Label (self.NLF2 , text=self.Display_str(num2.dic['Binary'],max(num1.dic['count'],num2.dic['count']))if opr != 7 else "0",font=("Britannic bold",16),bg = "#FFFFFF") 
        self.NL2.pack( )

        self.L2 = Label (self.Grid_Complete(self.Body,0,3,2,1), text="Number 2 : "+num2.dic['Number'],font=("Britannic bold",18),bg = "#d6d5c9" ) 
        self.L2.pack( side = TOP)

        self.photo1 = PhotoImage(file = r"images\arrow.png")
        self.arrow1 = Label(self.Grid_Complete(self.Body,1,1,1,1),image=self.photo1 ,bg="#d6d5c9")
        self.arrow1.pack(expand = 1)

        self.arrow2 = Label(self.Grid_Complete(self.Body,1,2,1,1),image=self.photo1 ,bg="#d6d5c9")
        self.arrow2.pack(expand = 1)

        self.arrow3 = Label(self.Grid_Complete(self.Body,3,1,1,2),image=self.photo1 ,bg="#d6d5c9")
        self.arrow3.pack(expand = 1)

        temp =  "images/"+  self.Listr[opr-1] + ".png"
        
        self.ICimg = PhotoImage(file = temp)
        self.Board = Label (self.Grid_Complete(self.Body,2,1,1,2), image=self.ICimg ,bg="#d6d5c9" ) 
        self.Board .pack( )
        
        self.NLF3 = Frame(self.Grid_Complete(self.Body,4,1,2,2), highlightbackground="black" , highlightthickness=1 )
        self.NLF3.pack(expand =1)
        self.NL3 = Label (self.NLF3 , text=self.Display_str(Res.dic['Binary'],max(num1.dic['count'],num2.dic['count'])),font=("Britannic bold",16),bg = "#FFFFFF") 
        self.NL3.pack( expand =1)

        self.L3 = Label (self.Grid_Complete(self.Body,4,0,1,1), text="Result :",font=("Britannic bold",18),bg = "#d6d5c9" ) 
        self.L3.pack( expand = 1)

        F1 = Frame (self.Grid_Complete(self.Body,4,3,2,4) , bg = "#FFFFFF"  ,width=135, height=225)
        F1.pack(expand=1)

        self.L3 = Label (self.Grid_Complete(self.Body,0,4,2,1), text="Final Result :",font=("Britannic bold",18),bg = "#d6d5c9" ) 
        self.L3.pack( expand = 1)
        self.Draw_Table(F1,opr)

        self.L4 = Label (self.Grid_Complete(self.Body,1,3,1,1), text="Truth Table :",font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L4.pack( expand = 1)

        self.L5 = Label (self.Grid_Complete(self.Body,2,3,1,1), text=self.Listr[opr-1]+" Gate",font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L5.pack( expand = 1)

        self.L6 = Label (self.Grid_Complete(self.Body,1,4,1,1), text =" Decimal => ",font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L6.pack( expand = 1)
        self.L7 = Label (self.Grid_Complete(self.Body,2,4,1,1), text = Res.dic['Number'],font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L7.pack( expand = 1)

        self.L8 = Label (self.Grid_Complete(self.Body,1,5,1,1), text =" Binary => ",font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L8.pack( expand = 1)
        self.L9 = Label (self.Grid_Complete(self.Body,2,5,1,1), text = self.Display_str(Res.dic['Binary'],Res.dic['count']),font=("Britannic bold",16),bg = "#d6d5c9" ) 
        self.L9.pack( expand = 1)

