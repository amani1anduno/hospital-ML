
import ui.frames as frames
import ui.popup as popup
from ModelOps import ModelContainer
from recordops import pacientRecord
import pandas as pd
from recordops import pacientRecord
from hospitalqueue import hospitalqueue as hq
from hospitalqueue import deparments as dp

import pickle
columns:list=pickle.load(open("DandC\\columns.pkl","rb"))
means:dict=pickle.load(open("DandC\\means.pkl","rb"))
print(columns)
columns.remove(('priorite', int))
columns.remove(('direction', int))

to_encode=["sexe","Emplacement de la douleur","Emplacement de la brûlure","Profondeur de la blessure","Emplacement de la blessure","Contamination de la blessure",
           "Type de fracture","Localisation de la fracture"]

lgr= ModelContainer(path="prioritymodels//lgr_tuned.pkl",scaler_path="scalers//scaler.pkl",categorical=to_encode,potentialvalues=columns)
vc= ModelContainer(path="prioritymodels//vc_tuned.pkl",scaler_path="scalers//scaler.pkl",categorical=to_encode,potentialvalues=columns)
pr=pacientRecord()
directions=pickle.load(open("DandC\\directions.pkl","rb"))
dep= dp("DandC\\directions.pkl")
print(dep.names)
while(True):
    PR=pacientRecord()
    myframe= frames.frames(columns,means)
    myframe.avtivateGui()
    info =myframe.new_dict
    for numarical in myframe.numaric:
        info[numarical]=float(info[numarical])
    #get models
    print(info)
    data =pd.Series(info)
    df=pd.DataFrame()
    df =pd.concat((df,pd.DataFrame.from_records([data])), ignore_index=True,axis=0)
    
    prediction_p = lgr.predict(df)[0]
    prediction_d = vc.predict(df)[0]
    #get prdiction
    #add to today's list
    df["priority"]=prediction_p
    df["direction"]=prediction_d
    pr.insertLast(df)
    last, i =pr.getLast()
    dep.add(prediction_d,prediction_p,i)
    #add to queue
    pop= popup.popup(PR.generateFileName(),[prediction_p,prediction_d],["priority","direction"])

    
    pass