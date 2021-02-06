# Operational Class
class convert:

    #  NAND Gate
    def Nand_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(1 if num1[x] == 0 or num2[x]== 0 else 0)
        return temp

    #  NOR Gate
    def Nor_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(1 if num1[x] == 0 and num2[x]== 0 else 0)
        return temp

    #  XOR Gate
    def Xor_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(0 if num1[x] == num2[x] else 1)
        return temp

    #  XNOR Gate
    def XNor_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(1 if num1[x] == num2[x] else 0)
        return temp

    #  AND Gate
    def And_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(1 if num1[x] == 1 and num2[x]== 1 else 0)
        return temp

    #  OR Gate
    def OR_gate(self,num1,num2):
        temp = []
        for x in range (0,max(self.C1,self.C2)):
            temp.append(1 if num1[x] == 1 or num2[x]== 1 else 0)
        return temp

    #  NOT Gate
    def Not_gate(self,num1):
        temp = []
        for x in range (0,self.C1):
            temp.append(1 if num1[x] == 0 else 0)
        return temp
   
    def __init__(self,num1,num2,opr,c1,c2):

       
        self.C1=c1   # Length of num1 till binary MSB(Most Significant Bit)
        self.C2=c2   # Length of num2 till binary MSB(Most Significant Bit)
        if opr == 1:
            Ans = self.Nand_gate(num1,num2)
        elif opr == 2:
            Ans = self.Nor_gate(num1,num2)
        elif opr == 3:
            Ans = self.Xor_gate(num1,num2)
        elif opr == 4:
            Ans = self.XNor_gate(num1,num2)
        elif opr == 5:
            Ans = self.And_gate(num1,num2)
        elif opr == 6:
            Ans = self.OR_gate(num1,num2)
        elif opr == 7:
            Ans = self.Not_gate(num1)
        self.result = Ans

    # RESULT RTURN
    def get_result(self):
        return self.result