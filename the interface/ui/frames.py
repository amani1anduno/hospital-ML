import customtkinter as ctk
from tkinter import PhotoImage
class frames:
    columns:list()
    datadict=dict()
    new_dict:dict()
    numaric=list()
    means:dict
    root:ctk.CTk
    def __init__(self,columns, means) -> None:
        self.columns:list()
        self.datadict=dict()
        self.new_dict:dict()
        self.numaric=list()
        self.root:ctk.CTk
        self.columns=columns
        self.means=means
        pass
    def varify(self,event,entry:ctk.CTkEntry):
        if event.char.isnumeric()==False:
            if(event.char=="."):
                return
            entry.delete(0,ctk.END)
        pass
    def refil(self,event,entry:ctk.CTkEntry):
        if len(entry.get())==0:
            entry.insert(0, entry._placeholder_text)
        if entry.get()[len(entry.get())-1]==".":
            entry.delete(len(entry.get())-1)
        entry._text_color("#000")
        pass
    def getCatFrame(self,root, options, name):
        var=ctk.StringVar()
        mycat=ctk.CTkOptionMenu(root, values=options,variable=var,width=165,button_color="#125",font=(None,11))
        mycat.set(name)
        self.datadict[name]=var
        return mycat
    def getnumaricalFrame(self,root, name):
        self.numaric.append(name)
        var=ctk.StringVar()
        self.datadict[name]=var
        mynu= ctk.CTkEntry(master=root,textvariable=var, placeholder_text=name,text_color="#aaa",width=165)
        mynu.insert(0, name)
        mynu.bind("<Button>", lambda event : mynu.delete(0,ctk.END))
        mynu.bind("<KeyRelease>", lambda event: self.varify(event,mynu))
        mynu.bind("<FocusOut>",lambda event: self.refil(event,mynu))
        return mynu
    def getboolentery(self,root, name):
        var=ctk.BooleanVar()
        self.datadict[name]=var
        return ctk.CTkCheckBox(master=root,text=name,variable=var,width=165,font=(None,11))
    def getName(self,root):
        namevar=ctk.StringVar()
        lastnamevar=ctk.StringVar()
        self.datadict["first name"]=namevar
        self.datadict["last name"]=lastnamevar
        myFrame=ctk.CTkFrame(root)
        name= ctk.CTkEntry(myFrame,placeholder_text="first name",textvariable=namevar)
        last_name= ctk.CTkEntry(myFrame,placeholder_text="last name",textvariable=lastnamevar)
        name.insert(0, "first name")
        last_name.insert(0, "last name")
        
        name.bind("<Button>", lambda event : name.delete(0,ctk.END))
        name.bind("<FocusOut>",lambda event: self.refil(event,name))
        
        last_name.bind("<Button>", lambda event : last_name.delete(0,ctk.END))
        last_name.bind("<FocusOut>",lambda event: self.refil(event,last_name))
        
        name.pack(side=ctk.LEFT)
        last_name.pack(side=ctk.RIGHT)
        return myFrame
        pass
    def getCoreframe(self,columns=None,root=None):
        if columns==None:
            columns=self.columns
        if root==None:
            root=self.root
        myframe =ctk.CTkFrame(root)
        listofenteries= list()
        complex_enteries= list()
        for c in columns:
            if (c[1]==int):
                listofenteries.append(self.getnumaricalFrame(myframe,c[0]))
                continue
            if (c[1]==str):
                listofenteries.append(self.getCatFrame(myframe,c[2],c[0]))
                continue
            if (c[1]==bool):
                listofenteries.append(self.getboolentery(myframe,c[0]))
                continue
            if (c[1]==list):
                listframe, enteries, filler =self.getCoreframe(c[2],myframe)
                label=ctk.CTkLabel(listframe,text=c[0])
                enteries.insert(0,label)
                complex_enteries.append((listframe,enteries))
                

                continue            
            pass
        return myframe,listofenteries,complex_enteries
    def getui(self):
        self.root=ctk.CTk()
        self.root.title("patient information")
        self.root.geometry("700x500")
        name_frame = self.getName(self.root)
        name_frame.pack()
        frame , infolist, complex_info = self.getCoreframe()
        for i in range(len(infolist)):
            infolist[i].grid(padx=2,pady=5, column=i%4, row=int(i/4))
        for com in complex_info:
            for i in range(len(com[1])):
                com[1][i].grid(padx=4,pady=4, column=i%4, row=int(i/4))
            com[0].grid(column=0, columns=4,pady=7)
        frame.pack()
        return self.root
    def avtivateGui(self):
        
        self.root=self.getui()
        Bframe = ctk.CTkFrame(self.root)
        button= ctk.CTkButton(Bframe,text="submit",command=self.getInfo)
        Bframe.pack(fill="x",side=ctk.BOTTOM)
        button.pack(side=ctk.RIGHT,pady=10,padx=10)
        self.root.mainloop()
    def getInfo(self):
        new_dict=dict()
        for key in self.datadict:
            new_dict[key]=self.datadict[key].get()
            if key==self.datadict[key].get() or self.datadict[key].get()=="":
                if key in self.numaric:
                    new_dict[key]=self.means[key]
                else:
                    new_dict[key]="none"
        for key in new_dict:
            if key in self.numaric:
                new_dict[key]=float(new_dict[key])
        #get result from model
        #send result to queue
        self.new_dict=new_dict
        self.root.quit()
        self.root.destroy()
        