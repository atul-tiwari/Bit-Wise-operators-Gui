class Store:

    # .. Convert To Binary ..
    def to_binary(self):
        li = []
        temp = int(self.dic['Number'])
        while temp > 0:
            li.append(temp%2)
            temp=temp//2
        self.dic['Binary']=li
        self.dic['count']=len(li)

    # .. Convert To Decimal ..
    def to_decimal(self,li):
        sum=0
        for x in range(len(li)):
            sum+=li[x]*(2**x)
        return sum

    # .. fill Rest of reming list with 0's .. 
    def complete(self):
        li =  self.dic['Binary']
        for x in range (self.dic['count'],10):
            li.append(x*0)
        self.dic['Binary']=li

    def __init__(self,num):
        self.dic = {}
        self.IsNull = True
        self.dic['Number']= num
        self.to_binary()
        self.complete()
        print(self.dic)
    
    def get_num(self):
        return self.dic