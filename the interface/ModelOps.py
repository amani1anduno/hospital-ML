import pickle
from sklearn.base import BaseEstimator
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os
import recordops
from sklearn.preprocessing import StandardScaler
import numpy as np
from hospitalqueue import hospitalqueue as hq
class ModelContainer:
    
    filler_df:pd.DataFrame()
    model:BaseEstimator
    categorical:list()
    scaler:StandardScaler
    potentialvalues:list
    def __init__(self,path,scaler_path,categorical,potentialvalues) -> None:
        self.model= pickle.load(open(path,"rb"))
        self.scaler= pickle.load(open(scaler_path,"rb"))
        self.categorical=categorical
        self.potentialvalues=potentialvalues
        self.filler_df= self.fillFiller(self.potentialvalues)
        pass

    def fillFiller(self,potentialvalues):
        df= pd.DataFrame()
        for i in range(10):
            row= {}
            for c in potentialvalues:
                if(c[1]==str):
                    row[c[0]]=c[2][i%len(c[2])]
                if(c[1]==int):
                    row[c[0]]=0
                if(c[1]==bool):
                    row[c[0]]=False
            df =pd.concat((df,pd.DataFrame.from_records([row])), ignore_index=True,axis=0)
        return df

    def one_hot_encoder(self,dataframe, categorical_columns, nan_as_category=False):
        original_columns = list(dataframe.columns)
        new_dataframe = pd.get_dummies(dataframe, columns=categorical_columns,
                                dummy_na=nan_as_category, drop_first=True)
        new_columns = [col for col in new_dataframe.columns if col not in original_columns]
        return new_dataframe
    def encode_data(self,data:pd.DataFrame):
        encoded=self.one_hot_encoder(data,categorical_columns=self.categorical)
        return encoded  
    def scaleData(self,dataframe):
        data=self.scaler.transform(dataframe)
        return pd.DataFrame(data,columns=dataframe.columns)
    def reduceData(self,dataframe:pd.DataFrame):
        return dataframe[[val for i,val in enumerate(dataframe.columns) if val in self.model.feature_names_in_]]
    def removeAccents(self,df):
        mapping = {'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u',
            'ñ': 'n',
            'â':'a'}
        return df.replace(mapping, regex=True)
    def toBool(self,df:pd.DataFrame):
        df2=df
        for c in df.columns:
            if "F" in df[c].unique():
                df2[c]=df2[c].replace('f',False)
                df2[c]=df2[c].replace('F',False)
                df2[c]=df2[c].replace('v',True)
                df2[c]=df2[c].replace('V',True)
        return df2
    def toLowerCase():
        pass
    def predict(self,dataframe:pd.DataFrame):
        self.scaler.feature_names_in_
        df = pd.concat([self.filler_df,dataframe],ignore_index=True)
        df =self.removeAccents(df)
        encoded= self.encode_data(df)
        scaled=self.scaleData(encoded[self.scaler.feature_names_in_])
        return self.model.predict(scaled[-1:])
    
class deparments:
    names:list
    queues:dict
    def __init__(self,path) -> None:
        names=pickle.load(open(path,"rb"))
        self.create_queues()
    def create_queues(self):
        for name in self.queues:
            self.queues[name]=hq("queue\\"+name+".pkt")
    def add(self,direction,priority,id):
        self.queues[direction].add(id,priority)
        