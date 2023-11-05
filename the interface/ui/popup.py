import customtkinter as ctk
from tkinter import PhotoImage
class popup:
    windom:ctk.CTk
    recordpath:str
    list_of_models:list()
    def close(self):
        self.window.quit()
        self.window.destroy()
        pass
    def open_excel(self,filename):
        import os
        os.system("start EXCEL.EXE "+filename)
    def __init__(self,recordpath:str,presictions:list=["model not ready yet"],list_of_models:list=["dumb model"]) -> None:
        self.recordpath=recordpath
        self.window= ctk.CTk()
        self.window.geometry("400x200")
        self.window.title("results")
        coreframe = ctk.CTkFrame(self.window)
        self.list_of_models=list_of_models
        print(self.list_of_models)
        resultes=list()
        for i in range(len(self.list_of_models)):
            frame =ctk.CTkFrame(coreframe)
            resultes.append([frame,[ctk.CTkLabel(frame,text=self.list_of_models[i]),ctk.CTkLabel(frame,text=presictions[i])]])
            pass
        coreframe.pack()
        Bframe = ctk.CTkFrame(self.window)
        button= ctk.CTkButton(Bframe,command=self.close,text="ok")
        ebutton= ctk.CTkButton(Bframe,command=lambda: self.open_excel(self.recordpath),text="open")
        
        Bframe.pack(fill="x",side=ctk.BOTTOM)
        for result in resultes:
            for elemet in result[1]:
                elemet.grid()
                pass
            result[0].pack()
            pass
        button.pack(side=ctk.RIGHT,pady=10,padx=10)
        ebutton.pack(side=ctk.LEFT,pady=10,padx=10)
        self.window.mainloop()
        pass