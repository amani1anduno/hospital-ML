import frames as frames
COLUMNS=[  
        ("age", int,[0,130,14,80]),
        ("height", int,[50,200,140,180]),
        ("weight", int,[30,300,45,70]),
        ("body fat %", int,[2,50,3,13]),
        ("sex",str,["m","f"]),
        ("Sneezing", bool,0),
         ("Coughing", bool,0),
         ("Stuffy nose", bool,0),
         ("Runny nose", bool,0),
         ("Breathlessness", bool,0),
         ("Vomiting", bool,0),
         ("Nausea", bool,0),
         ("Diarrhea", bool,0),
         ("Bloating", bool,0),
         ("Constipation", bool,0),
         ("Heart palpitations", bool,0),
         ("Fainting", bool,0),
         ("Edema", bool,0),
         ("Dyspnea", bool,0),
         ("Dizziness", bool,0),
         ("Persistent headache", bool,0),
         ("Loss of feeling", bool,0),
         ("Tingling", bool,0),
         ("loss of muscle strength.", bool,0),
         ("Lack of coordination", bool,0),
         ("Loss of sight", bool,0),
         ("double vision", bool,0),
         ("hypertension", bool,0),
         ("diabetic", bool,0),
         ("aesthetic", bool,0),
         ("Frequency of sickness per year", int,[1,10]),
         ("Headache", str,[ "Migraine headache","Tension headache",'Hypnic headache','Cluster headache']),
         ("pain",
          list,
        [("Pain level", int,[1,10]),
         ("Pain location", str,["head","upper abdomin","lower abdomin","chest","leg","arm","back"])
         ]),
         
         ("burn",list,[
          ("Burn degree", int,[1,3]),
         ("Burn size", int,[1,100]),
         ("Burn location", str,["head","upper abdomin","lower abdomin","chest","leg","arm","back"])]),
        ( "wound",list,
         [("Wound depth", str,["Superficial","Partial thickness","Full thickness"]),
         ("Wound location", str,["head","upper abdomin","lower abdomin","chest","leg","arm","back"]),
         ('Wound size %' , int,[1,100]),
         ("Wound contamination ", str,["clean","clean-contaminated","contaminated","dirty-infected"])]),
         ("fracture",list,
         [("fracture type", str,["Greenstick","Transverse","Spiral","Oblique","Comminuted","Segmental","Compression"]),
         ("fracture location", str,["skull","spine","ripcage","pelvise","leg","arm"])
         ])
         ,
         ("systolic blood pressure mmHg", int,[80,180,90,119]),
         ("diastolic  blood pressure mmHg", int,[20,140,60,79]),
         ("blood sugar level (mg/dL) ", int,[25,600,70,99]),
         ("respiration rate (breath/min)", int,[5,40,12,20]),
         ("heart rate (at rest)", int,[45,120,60 ,100]),
         
         ]

root= frames.avtivateGui(COLUMNS)

