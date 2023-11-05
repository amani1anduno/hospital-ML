import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk
class Infobox:
    root:ctk.CTkFrame
    dicto:dict
    infoUI:ctk.CTkFrame
    def __init__(self,root:ctk.CTk()) -> None:
        self.root=ctk.CTkFrame(root)
        
        pass
    def addInfoIU(self,dicto):
        self.dicto=dicto
        i=0
        infoFrame=ctk.CTkFrame(self.root)
        for key in dicto:
            frame =ctk.CTkFrame(infoFrame,width=200,height=10)
            keyLabel= ctk.CTkLabel(frame,text=key,font=(None, 10, 'bold'))
            valueLabel= ctk.CTkLabel(frame,text=dicto[key],font=(None, 10))
            keyLabel.pack(padx=5, side=ctk.LEFT)
            valueLabel.pack(padx=5, side=ctk.RIGHT)
            frame.grid(column=i%4+1,row=int(i/4)+1, pady=2,padx=1)
            i=i+1
        infoFrame.pack()
        self.infoUI= infoFrame
    def addButton(self,func,new_info):
        frame = ctk.CTkFrame(self.root)
        bottun = ctk.CTkButton(frame,text="call next patient", command=lambda: self.buttomfunc(func,new_info))
        bottun.pack(side=ctk.RIGHT,pady=10,padx=10)
        frame.pack(side=ctk.BOTTOM,pady=10,padx=10)
        ## add function for the buttom
        pass
    def buttomfunc(self,func,new_info):
        self.infoUI.destroy()
        #remove info
        #insert new info
        #
        self.addInfoIU()
        pass
    def waitUI(self):
        img= PhotoImage("images\\doctor icon.png")
        waitFrame= ctk.CTkFrame(master=self.root,image = img)
        waitFrame.pack()
    def addUI(self,info,root:ctk.CTk()):
                    
        self.root=ctk.CTkFrame(root)
        if info=="":
            self.waitUI
            pass
        else:
            self.addInfoIU(info)          
        self.root.pack(fill="y")
    def distroy(self):
        self.root.destroy()