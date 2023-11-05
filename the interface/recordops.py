import os
import pandas as pd
from datetime import date
import numpy as np
import openpyxl
class pacientRecord:
    todaysArrivals:str
    path:str
    df:pd.Series
    def __init__(self) -> None:
        self.path= self.generateFileName()
        self.createFileIfNotExist()
    def generateFileName(self) -> str:
        return "pacients\\arrivals"+date.today().strftime("%d-%m-%y")+".xlsx"
    def createFileIfNotExist(self):
        if (not os.path.exists(self.path)):
            wb = openpyxl.Workbook()
            wb.save(self.path)
    def recieveNewPacient(pinfo):
        print(pinfo)
        pass
    def getLast(self):
        df= pd.read_excel(self.path)
        last_element= df.iloc[-1]
        last_index= df.shape[0]
        return last_element, last_index
    def insertLast(self,info:pd.DataFrame):
        
        df= pd.read_excel(self.path)
        df =pd.concat((df,info),ignore_index=True)
        df= df.reset_index(drop=True)
        css_alt_rows = 'background-color: powderblue; color: black;'
        css_indexes = 'background-color: steelblue; color: white;'
        (df.style.apply(lambda col: np.where(col.index % 2, css_alt_rows, None))
         .applymap_index(lambda _: css_indexes, axis=0)
         .applymap_index(lambda _: css_indexes, axis=1)
         ).to_excel(self.path,index=False, engine='openpyxl')        
    def getFileName(self):
        return self.path
    def get(self,i:int):
        df= pd.read_excel(self.path)
        wanted_element= df.iloc[i-1]
        return wanted_element
    
    