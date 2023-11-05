import pickle
import os
from datetime import date
from recordops import pacientRecord as pr
class hospitalqueue:
    waiting_room:list
    current:int
    record:int
    intervals:list
    path:str
    date:str
    def __init__(self,path) -> None:
        self.waiting_room=[set(),set(),set(),set(),set()]
        self.current=1
        self.intervals=[1,5,7,11,17]
        self.record=0
        self.path=path
        self.position()
        self.date=date.today().strftime("%d-%m-%y") 
        if (not os.path.exists(self.path)):
            print("file does not exist creating new file")
            self.export(self.path)
        else: self.load()
    def getstate(self):
        return self.waiting_room
    def add(self,id,mts:int):
        # if self.all_empty:
        #     print("all empty")
        #     self.current=mts
        #     print(self.current)
        self.waiting_room[mts-1].add(id)
        self.first_in_line()
        self.export()
        return self.waiting_room
    def first_in_line(self):
        for i in range(len(self.waiting_room)):
            if len(self.waiting_room[(i)])>0:
                self.current=(i+1)
                continue
            pass
    def next_in_line(self):
        self.current=(self.current+1)
        if self.current>5:
            self.current=1
        pass
    def sendoff(self):
        self.record=self.record+1
        self.pluck(self.current)
        self.move()
        print(self.current)
        while(len(self.waiting_room[(self.current-1)])==0):
            print("before nil",self.current)
            self.next_in_line()
            print("after nil",self.current)
            if self.all_empty():
                break
            pass
        print(self.current)
        self.export()
        return self.current
    def move(self):
        for i in range(len(self.intervals)):
            if(self.record%self.intervals[i]==0):
                self.current=i+1
        print("record:",self.record,",current:",self.current)
        pass
    def pluck(self,mts):
        if len(self.waiting_room[mts-1]):
            self.waiting_room[mts-1].remove(list(self.waiting_room[mts-1])[0])
    def export(self,path:str=""):
        if(path==""):
            path=self.path
        pickle.dump({"record":self.record,"waitingroom":self.waiting_room,"current":self.current,"date":self.date},open(path,"wb"))
        pass
    def load(self,path:str=""):
        if(path==""):
            path=self.path
        loaded:dict=pickle.load(open(path,"rb"))
        self.waiting_room=loaded["waitingroom"]
        self.record=loaded["record"]
        self.current=loaded["current"]
        if self.datechanged(loaded["date"]):
            self.empty_save()
        pass
    def position(self):
        for i in range(len(self.waiting_room)):
            if len(self.waiting_room)==0:
                continue
            self.current=i+1
            return
        self.current=1
        return
    def get_index(self):
        print(self.waiting_room[self.current-1],self.current)
        for e in self.waiting_room[self.current-1]:
            print(e)
            return e
        pass
    def empty(self):
        self.waiting_room=[set(),set(),set(),set(),set()]
    def empty_save(self):
        self.empty()
        self.export()
    def all_empty(self)->bool:
        length=0
        for room in self.waiting_room:
            length=length+len(room)
        print(self.path,self.getstate())
        
        return length==0
    def datechanged(self,d) ->bool:
        return not self.date==d
class deparments:
    names:list
    queues:dict
    def __init__(self,path) -> None:
        self.names=pickle.load(open(path,"rb"))
        self.queues=self.create_queues()
    def create_queues(self):
        ql={}
        for name in self.names:
            ql[name]=hospitalqueue("queue\\"+name+".pkt")
        return ql
    def add(self,direction,priority,id):
        self.queues[direction].add(id,priority)
    def getinfo(self, direction):
        index=self.queues[direction].get_index()
        record= pr()
        return record.get(index)
    def getstate(self,direction):
        return self.queues[direction].getstate()
        pass
    def getallstates(self):
        full=[]
        for name in self.queues:
            full.append(self.queues[name].getstate())
        return full 
        pass
    def get_index(self,direction):
        return self.queues[direction].get_index()
    def all_empty(self, direction)->bool:

        return self.queues[direction].all_empty()
    def sendOff(self, direction):
        self.queues[direction].sendoff()
    def load(self, direction):
        self.queues[direction].load()
