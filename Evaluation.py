#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:37:20 2018

@author: Nimra
"""

from __future__ import division #used 2.7 python
import pandas as pd

workerinfo = 0
workerinfo = pd.read_csv('workset1271004.csv') #rreading the data
workerinfo= workerinfo.loc[workerinfo["judgments_count"]>0] #only workers which have a count higher 0
workerinfo = workerinfo[["worker_id","judgments_count"]] #only stuff I might need later
workerscount= len(workerinfo)
actualid = (list(workerinfo["worker_id"]))


csv2 = pd.read_csv('a1271004.csv')
judgments = csv2[["_unit_id","to_what_mood_would_you_categorize_the_song","what_is_your_age","what_is_your_gender","what_is_your_o_c_e_a_n_personality","what_makes_you_think_that_it_belongs_in_your_chosen_mood","whats_the_gender_of_the_singer","name"]]


csv3 = pd.read_csv('f1271004.csv')
judgments2 = csv3.iloc[:,:26]
del judgments2["_created_at"]
del judgments2["_golden"]
del judgments2["_missed"]
del judgments2["_started_at"]
del judgments2["_tainted"]
del judgments2["_channel"]
del judgments2["_trust"]
del judgments2["_country"]
del judgments2["_region"]
del judgments2["_city"]
del judgments2["_ip"]
del judgments2["orig__golden"]
del judgments2["link"]
del judgments2["orig__unit_id"]
del judgments2["orig__created_at"]
del judgments2["_updated_at"]
ages = ["under","above","young","old"]

#in the workerinfo add the age, gender, and personality type so that we have an easy acces too it.


ind = 0
workerinformation = pd.DataFrame(index= range(workerscount),columns=["id","age","sex","personality","total","%dark","darkasked","%relaxedcalm","relaxedasked","%goodvibes","goodasked","%melancholia","melancholiaasked"])
ids= []

for index, row in workerinformation.iterrows():
    for i, r in judgments2.iterrows():
        if r["_worker_id"] not in ids and r["_worker_id"] in actualid :
            if r["what_is_your_age"] in ages:
                ids.append(r["_worker_id"])
                workerinformation.set_value(ind,"id",r["_worker_id"])
                workerinformation.set_value(ind,"age",r["what_is_your_age"])
                workerinformation.set_value(ind,"sex",r["what_is_your_gender"])
                workerinformation.set_value(ind,"personality",r["what_is_your_o_c_e_a_n_personality"])
                
                ind +=1
                
workerinformation.to_csv('allworkerinformation.csv')
solutions = pd.read_csv('songsandmoods_updated.csv')

for index,row in workerinformation.iterrows():

    totalcorrect = 0
    happycorrect = 0
    relaxedcorrect = 0
    darkcorrect = 0
    melcorrect = 0
    
    happyasked = 0
    relaxedasked = 0
    darkasked = 0
    melasked = 0
    total = 0
    
    
    for i,r in judgments2.iterrows():
        if r["_worker_id"]== row["id"]:
    
            name = r["name"]
            given = r["to_what_mood_would_you_categorize_the_song"]
            guessgender = r["whats_the_gender_of_the_singer"]
            
            for index3, row3 in solutions.iterrows():
                if row3["name"]== name: #checking in csv where the song name appears
                    solution = row3["mood"]
                    solutiongender = row3["gendersinger"]
                    if solution == "dark_stormy":
                        darkasked = darkasked + 1
                    if solution == "melancholia":
                        melasked = melasked + 1
                    if solution == "relaxed_calm":
                        relaxedasked = relaxedasked +1 
                        #print(" the worker " + str(row["id"])+ " gave the answer  to the song " + name + " where actually it is " + str(relaxedasked))
                    if solution == "happy_vibes":
                        happyasked = happyasked +1
                
            if given == solution and guessgender == solutiongender:
                totalcorrect = totalcorrect + 1
                if given == "dark_stormy":
                    darkcorrect = darkcorrect + 1
                if given == "melancholia":
                    melcorrect = melcorrect + 1
                if given == "relaxed_calm":
                    relaxedcorrect = relaxedcorrect + 1
                    #print(" the worker " + str(row["id"])+ " gave the answer  to the song " + name + " where the end counter actually it is " + str(relaxedcorrect))
                if given == "happy_vibes":
                    happycorrect = happycorrect + 1
                
                        
                    
     
        workerinformation.set_value(index,"goodasked",happyasked)
        workerinformation.set_value(index,"melancholiaasked",melasked)
        workerinformation.set_value(index,"relaxedasked",relaxedasked)
        workerinformation.set_value(index,"darkasked",darkasked)
        
        if happyasked == 0:
            workerinformation.set_value(index,"%goodvibes",None)
        else: 
            workerinformation.set_value(index,"%goodvibes",happycorrect/happyasked)
            
        if darkasked == 0:
            workerinformation.set_value(index,"%dark",None)
        else:
            workerinformation.set_value(index,"%dark",darkcorrect/darkasked)
        
        if melasked == 0:
            workerinformation.set_value(index,"%melancholia",None)
        else:
            workerinformation.set_value(index,"%melancholia",melcorrect/melasked)
            
        if relaxedasked == 0:
            workerinformation.set_value(index,"%relaxedcalm",None)
        else:
            workerinformation.set_value(index,"%relaxedcalm",relaxedcorrect/relaxedasked)
            
        
        workerinformation.set_value(index,"total",happyasked + darkasked + melasked + relaxedasked)
        
        
##we only went through the very first file thee are two so do the same for the other        

agecomparison = pd.DataFrame(index= ["Under 18","18-24","25-34","Above 34"],columns=["%dark","%relaxedcalm","%goodvibes","%melancholia"])

rows1 = workerinformation.loc[workerinformation['age'] == "under"]
rows2 = workerinformation.loc[workerinformation['age'] == "young"]
rows3 = workerinformation.loc[workerinformation['age'] == "old"]
rows4 = workerinformation.loc[workerinformation['age'] == "above"]

def ageevaluate(row):
    dark = 0.0
    happy = 0.0
    mel = 0.0
    relaxed = 0.0
    
    counterd = 0
    counterh = 0
    counterm = 0
    counterr = 0
    for index, row in row.iterrows():
        if row["%dark"] == None:
            pass
        else:    
            dark = dark + row["%dark"]
            counterd = counterd + 1
            
        if row["%goodvibes"] == None:
            pass
        else:
            happy = happy + row["%goodvibes"]
            counterh = counterh + 1
            
        if row["%melancholia"] == None:
            pass
        else:  
            mel = mel + row["%melancholia"]
            counterm = counterm + 1
            
        if row["%relaxedcalm"]== None:
            pass
        else:
            relaxed = relaxed + row["%relaxedcalm"]
            counterr = counterr + 1
    

    if row["age"]== "under":
        if counterd == 0:
            agecomparison.set_value("Under 18","%dark", 0)
        else:
            agecomparison.set_value("Under 18","%dark", dark/counterd)
            
        if counterh == 0:
            agecomparison.set_value("Under 18","%goodvibes", 0)
        else:
            agecomparison.set_value("Under 18","%goodvibes", happy/counterh)
            
        if counterr == 0:
            agecomparison.set_value("Under 18","%relaxedcalm", 0)
        else:
            agecomparison.set_value("Under 18","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            agecomparison.set_value("Under 18","%melancholia", 0)
        else:
            agecomparison.set_value("Under 18","%melancholia", mel/counterm)
        
    if row["age"]== "young":
        
        if counterd == 0:
            agecomparison.set_value("18-24","%dark", 0)
        else:
            agecomparison.set_value("18-24","%dark", dark/counterd)
            
        if counterh == 0:
            agecomparison.set_value("18-24","%goodvibes", 0)
        else:
            agecomparison.set_value("18-24","%goodvibes", happy/counterh)
            
        if counterr == 0:
            agecomparison.set_value("18-24","%relaxedcalm", 0)
        else:
            agecomparison.set_value("18-24","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            agecomparison.set_value("18-24","%melancholia", 0)
        else:
            agecomparison.set_value("18-24","%melancholia", mel/counterm)
    
    if row["age"]== "old":
        if counterd == 0:
            agecomparison.set_value("25-34","%dark", 0)
        else:
            agecomparison.set_value("25-34","%dark", dark/counterd)
            
        if counterh == 0:
            agecomparison.set_value("25-34","%goodvibes", 0)
        else:
            agecomparison.set_value("25-34","%goodvibes", happy/counterh)
            
        if counterr == 0:
            agecomparison.set_value("25-34","%relaxedcalm", 0)
        else:
            agecomparison.set_value("25-34","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            agecomparison.set_value("25-34","%melancholia", 0)
        else:
            agecomparison.set_value("25-34","%melancholia", mel/counterm)
    
        
    
    if row["age"]== "above":
        
        if counterd == 0:
            agecomparison.set_value("Above 34","%dark", 0)
        else:
            agecomparison.set_value("Above 34","%dark", dark/counterd)
            
        if counterh == 0:
            agecomparison.set_value("Above 34","%goodvibes", 0)
        else:
            agecomparison.set_value("Above 34","%goodvibes", happy/counterh)
            
        if counterr == 0:
            agecomparison.set_value("Above 34","%relaxedcalm", 0)
        else:
            agecomparison.set_value("Above 34","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            agecomparison.set_value("Above 34","%melancholia", 0)
        else:
            agecomparison.set_value("Above 34","%melancholia", mel/counterm)
    
        
        
    


ageevaluate(rows1)
ageevaluate(rows2)
ageevaluate(rows3)
ageevaluate(rows4)

agecomparison.to_csv('agesevaluated.csv')


rowsm = workerinformation.loc[workerinformation['sex'] == "male"]
rowsf = workerinformation.loc[workerinformation['sex'] == "female"]
sexcomparison = pd.DataFrame(index= ["Female","Male"],columns=["%dark","%relaxedcalm","%goodvibes","%melancholia"])
def sexevaluate(row):
    dark = 0.0
    happy = 0.0
    mel = 0.0
    relaxed = 0.0
    
    counterd = 0
    counterh = 0
    counterm = 0
    counterr = 0
    for index, row in row.iterrows():
        if row["%dark"] == None:
            pass
        else:    
            dark = dark + row["%dark"]
            counterd = counterd + 1
            
        if row["%goodvibes"] == None:
            pass
        else:
            happy = happy + row["%goodvibes"]
            counterh = counterh + 1
            
        if row["%melancholia"] == None:
            pass
        else:  
            mel = mel + row["%melancholia"]
            counterm = counterm + 1
            
        if row["%relaxedcalm"]== None:
            pass
        else:
            relaxed = relaxed + row["%relaxedcalm"]
            counterr = counterr + 1
    
    if row["sex"]== "female":
        if counterd == 0:
            sexcomparison.set_value("Female","%dark", 0)
        else:
            sexcomparison.set_value("Female","%dark", dark/counterd)
            
        if counterh == 0:
            sexcomparison.set_value("Female","%goodvibes", 0)
        else:
            sexcomparison.set_value("Female","%goodvibes", happy/counterh)
            
        if counterr == 0:
            sexcomparison.set_value("Female","%relaxedcalm", 0)
        else:
            sexcomparison.set_value("Female","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            sexcomparison.set_value("Female","%melancholia", 0)
        else:
            sexcomparison.set_value("Female","%melancholia", mel/counterm)
            
    if row["sex"]== "male":
        if counterd == 0:
            sexcomparison.set_value("Male","%dark", 0)
        else:
            sexcomparison.set_value("Male","%dark", dark/counterd)
            
        if counterh == 0:
            sexcomparison.set_value("Male","%goodvibes", 0)
        else:
            sexcomparison.set_value("Male","%goodvibes", happy/counterh)
            
        if counterr == 0:
            sexcomparison.set_value("Male","%relaxedcalm", 0)
        else:
            sexcomparison.set_value("Male","%relaxedcalm", relaxed/counterr)
            
        if counterm == 0:
            sexcomparison.set_value("Male","%melancholia", 0)
        else:
            sexcomparison.set_value("Male","%melancholia", mel/counterm)
            
    
sexevaluate(rowsm) 
sexevaluate(rowsf)  
sexcomparison.to_csv("sexevaluation.csv")  

rowso = workerinformation.loc[workerinformation['personality'] == "openness"]
rowsc = workerinformation.loc[workerinformation['personality'] == "conscientiousness"]
rowse = workerinformation.loc[workerinformation['personality'] == "extraversion"]
rowsa = workerinformation.loc[workerinformation['personality'] == "agreeableness"]
rowsn = workerinformation.loc[workerinformation['personality'] == "neuroticism"]
perscomparison = pd.DataFrame(index= ["Openness","Conscientiousness","Extraversion","Agreeableness","Neuroticism"],columns=["%dark","%relaxedcalm","%goodvibes","%melancholia"])


def persevaluate(row):
    dark = 0.0
    happy = 0.0
    mel = 0.0
    relaxed = 0.0
    
    counterd = 0
    counterh = 0
    counterm = 0
    counterr = 0
    for index, row in row.iterrows():
        if row["%dark"] == None:
            pass
        else:    
            dark = dark + row["%dark"]
            counterd = counterd + 1
            
        if row["%goodvibes"] == None:
            pass
        else:
            happy = happy + row["%goodvibes"]
            counterh = counterh + 1
            
        if row["%melancholia"] == None:
            pass
        else:  
            mel = mel + row["%melancholia"]
            counterm = counterm + 1
            
        if row["%relaxedcalm"]== None:
            pass
        else:
            relaxed = relaxed + row["%relaxedcalm"]
            counterr = counterr + 1
    
    if row["personality"] == "openness":
        if counterd == 0:
            perscomparison.set_value("Openness","%dark",0)
            
        else:
            perscomparison.set_value("Openness","%dark",dark/counterd)
            
        if counterh == 0:
            perscomparison.set_value("Openness","%goodvibes",0)
            
        else:
            perscomparison.set_value("Openness","%goodvibes",happy/counterh)
            
        if counterm == 0:
            perscomparison.set_value("Openness","%melancholia",0)
            
        else:
            perscomparison.set_value("Openness","%melancholia",mel/counterm)
            
        if counterr == 0:
            perscomparison.set_value("Openness","%relaxedcalm",0)
            
        else:
            perscomparison.set_value("Openness","%relaxedcalm",relaxed/counterr)
    
    if row["personality"] == "conscientiousness":
            if counterd == 0:
                perscomparison.set_value("Conscientiousness","%dark",0)
                
            else:
                perscomparison.set_value("Conscientiousness","%dark",dark/counterd)
                
            if counterh == 0:
                perscomparison.set_value("Conscientiousness","%goodvibes",0)
                
            else:
                perscomparison.set_value("Conscientiousness","%goodvibes",happy/counterh)
                
            if counterm == 0:
                perscomparison.set_value("Conscientiousness","%melancholia",0)
                
            else:
                perscomparison.set_value("Conscientiousness","%melancholia",mel/counterm)
                
            if counterr == 0:
                perscomparison.set_value("Conscientiousness","%relaxedcalm",0)
                
            else:
                perscomparison.set_value("Conscientiousness","%relaxedcalm",relaxed/counterr)
    
   
    if row["personality"] == "extraversion":
            if counterd == 0:
                perscomparison.set_value("Extraversion","%dark",0)
                
            else:
                perscomparison.set_value("Extraversion","%dark",dark/counterd)
                
            if counterh == 0:
                perscomparison.set_value("Extraversion","%goodvibes",0)
                
            else:
                perscomparison.set_value("Extraversion","%goodvibes",happy/counterh)
                
            if counterm == 0:
                perscomparison.set_value("Extraversion","%melancholia",0)
                
            else:
                perscomparison.set_value("Extraversion","%melancholia",mel/counterm)
                
            if counterr == 0:
                perscomparison.set_value("Extraversion","%relaxedcalm",0)
                
            else:
                perscomparison.set_value("Extraversion","%relaxedcalm",relaxed/counterr)
                
    if row["personality"] == "neuroticism":
            if counterd == 0:
                perscomparison.set_value("Neuroticism","%dark",0)
                
            else:
                perscomparison.set_value("Neuroticism","%dark",dark/counterd)
                
            if counterh == 0:
                perscomparison.set_value("Neuroticism","%goodvibes",0)
                
            else:
                perscomparison.set_value("Neuroticism","%goodvibes",happy/counterh)
                
            if counterm == 0:
                perscomparison.set_value("Neuroticism","%melancholia",0)
                
            else:
                perscomparison.set_value("Neuroticism","%melancholia",mel/counterm)
                
            if counterr == 0:
                perscomparison.set_value("Neuroticism","%relaxedcalm",0)
                
            else:
                perscomparison.set_value("Neuroticism","%relaxedcalm",relaxed/counterr)
                
    if row["personality"] == "agreeableness":
            if counterd == 0:
                perscomparison.set_value("Agreeableness","%dark",0)
                
            else:
                perscomparison.set_value("Agreeableness","%dark",dark/counterd)
                
            if counterh == 0:
                perscomparison.set_value("Agreeableness","%goodvibes",0)
                
            else:
                perscomparison.set_value("Agreeableness","%goodvibes",happy/counterh)
                
            if counterm == 0:
                perscomparison.set_value("Agreeableness","%melancholia",0)
                
            else:
                perscomparison.set_value("Agreeableness","%melancholia",mel/counterm)
                
            if counterr == 0:
                perscomparison.set_value("Agreeableness","%relaxedcalm",0)
                
            else:
                perscomparison.set_value("Agreeableness","%relaxedcalm",relaxed/counterr)
            
            
            
        
            
persevaluate(rowso)
persevaluate(rowsc)
#persevaluate(rowse)
persevaluate(rowsa)
persevaluate(rowsn) 

perscomparison.to_csv('personalityevaluated.csv')        


    
    
    
    
    




    

    























