class Phim:
    id:"P"+
    name: str
    dateStart: str
    ep: int
    TheLoai: str
    def __init__(self,id,name,dateStart,ep,Theloai):

        self.name=name
        self.dateStart=dateStart
        self.ep=ep
        if type=="TL001"+filter(lambda x:x.id==type,TheLoai):
            self.TheLoai=type
class TheLoai:
    id:str
    name:str
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)
n=int(input())
m=int(input())
for i in range(n):
   Phim.type=input()
