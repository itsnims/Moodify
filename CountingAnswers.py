#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:47:45 2018

@author: Nimra
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:50:32 2018

@author: Nimra
"""
import pandas as pd

Task1 = pd.read_csv('f1271004.csv')
Reasons1 = Task1.iloc[:,18:19]

Task1Chart =pd.DataFrame(index= ['Melody','Lyrics','Voice','Beat'],columns=['Counter'])

Task2 = pd.read_csv('task2.csv')
Reasons2 = Task2.iloc[:,13:14]

Task2Chart = pd.DataFrame(index= ['Melody','Lyrics','Voice','Beat'],columns=['Counter'])

Reasons1.columns = ['reason']
Task1Chart.set_value('Melody','Counter',Reasons1.reason.value_counts()['melody']/200)
Task1Chart.set_value('Lyrics','Counter',Reasons1.reason.value_counts()['lyrics']/200)
Task1Chart.set_value('Voice','Counter',Reasons1.reason.value_counts()['voice']/200)
Task1Chart.set_value('Beat','Counter',Reasons1.reason.value_counts()['beat']/200)



Reasons2.columns = ['reason']
Melody = ['tune','sound','atmosphere','melody','tone','light','heavy']
Lyrics = ['about','topic','issue','lyrics']
Voice = ['singer','voice','female','male']
Beat = ['instruments','rhythm','beat','tempo','slow','fast']

CounterM = 0
CounterL = 0
CounterV = 0
CounterB = 0

Outliner = 'Because the song its really slowly, its a female voice in the song and the mood its really obvious'
OutCounter = 0

index = 1
while index < 120:
    tester = Reasons2['reason'][index].split() #splits into many little one words
    if tester == Outliner.split():
        OutCounter = OutCounter +1
        index = index + 1
    
    else:
    
        m = 0
        l = 0
        v = 0
        b = 0
        
        for word in tester:
            if word in Melody:
                m = m + 1
            elif word in Lyrics:
                l = l + 1
            elif word in Voice:
                v = v + 1
            elif word in Beat:
                b = b + 1
                
        point = max(m,l,v,b)
        if point == m:
            CounterM = CounterM + 1
        elif point == l:
            CounterL = CounterL + 1
        elif point == v:
            CounterV = CounterV + 1
        elif point == b:
            CounterB = CounterB + 1
        
        
        index = index + 1
        
Task2Chart.set_value('Melody','Counter',CounterM/86)
Task2Chart.set_value('Lyrics','Counter',CounterL/86)
Task2Chart.set_value('Voice','Counter',CounterV/86)
Task2Chart.set_value('Beat','Counter',CounterB/86)


Task1Chart.to_csv('OccurencesOfReasonsFixedSize.csv')
Task2Chart.to_csv('OccurencesOfReasonsOpenSize.csv')
