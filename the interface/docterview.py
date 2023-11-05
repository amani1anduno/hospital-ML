import customtkinter as ctk
from ui.call import Infobox
from hospitalqueue import hospitalqueue as hq
import pickle
from hospitalqueue import deparments as dp
from recordops import pacientRecord as pd
from tkinter import PhotoImage
def moveOn():
    if(not dep.all_empty(depVar.get())):
        dep.sendOff(depVar.get())
        refresh()
    pass
par=pd()
def refresh():
    dep.load(depVar.get())
    IB.distroy()
    if dep.all_empty(depVar.get()):
        IB.addUI("",root)
    else:
        id=dep.get_index(depVar.get())
        
        IB.addUI(par.get(id).to_dict(),root)
    pass

root = ctk.CTk()
root.geometry("850x500")
root.title("arrivals")
ib=Infobox(root)
wait_img=PhotoImage("ui/images/bench.png")


directions=pickle.load(open("DandC\\directions.pkl","rb"))
dep= dp("DandC\\directions.pkl")
departments=["generale","immédiat","chirurgie"]
options_menu=ctk.CTkFrame(root)
depVar= ctk.StringVar()
departmentlist=ctk.CTkOptionMenu(options_menu, values=directions,variable=depVar)
refresh_button= ctk.CTkButton(options_menu,text="refresh",command=lambda: refresh())
departmentlist.pack(side = ctk.LEFT,padx=3)
refresh_button.pack(side = ctk.LEFT,padx=3)
options_menu.pack()
IB=Infobox(root)

next_frame=ctk.CTkFrame(root)
next_button=ctk.CTkButton(next_frame,text="next",command=lambda: moveOn())
next_frame.pack(side=ctk.BOTTOM,fill="x")
next_button.pack(side=ctk.RIGHT)
root.mainloop()