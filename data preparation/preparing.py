import pandas as pd

data = pd.read_csv("dataset.csv")
#adult average
tot=0
count=0
adltot=0
adlcount=0
for age in data['ptage']:
    if isinstance(age, str)and age.isnumeric():
        age= float(age)
        if not isinstance(age, str) :
            tot=tot+age
            count=count+1
            if age>=18:
                adltot=adltot+age
                adlcount=adlcount+1
average=round(tot/count,2)
averageadl=round(adltot/adlcount,2)

data["ptage"]=data["ptage"].str.lower()
data=data.replace("adult",averageadl)
data=data.replace("ad",averageadl)

data["ptage"]=data["ptage"].replace(pd.NA,average)
data["ptage"]=data["ptage"].replace("-",average)



for i in range(data["ptage"].last_valid_index()):
    if not isinstance(data["ptage"][i], float) and not data["ptage"][i].isnumeric():
        try: data["ptage"][i]=float(data["ptage"][i])
        except:pass
data['ptage']=data['ptage'].astype('str')
#a lot of problems would've been solved if I turned those values to strings from the
#get go

# now to fix sex
#there are 4 rows missing so I just replaced them with female
res =data[data["ptage"].str.contains("-")]
data=data.drop(res.index)
data["ptsex"]=data["ptsex"].replace(pd.NA,'F')

#special cases
#those cases are: indications, ultrasoundfindings
#handeling: seperate them into boolean features

data.indications=data.indications.astype('str')
#remeber to exclude quesion
for ele in data["indications"]:
    for sec in ele.split(","):
        if "Question" in sec or "?" in sec:
            data.indications=data.indications.str.replace(sec,"nan")

data.indications=data.indications.str.replace("; ",",")
data.indications=data.indications.str.replace(": ",",")

sf=pd.DataFrame()
for ele in data["indications"]:
    #creat a data frame add 
    #remeber to exclude quesions and "other"
    #add empty row
    for sec in ele.split(","):
        if not sec=="nan":
            print(sec)

data.to_csv("output.csv",index=True)