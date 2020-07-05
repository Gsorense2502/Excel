import pandas as pd
import numpy as np

RawData =  pd.DataFrame(pd.read_excel("vbaTest_Candidate.xlsm","Data",usecols = "A"))

RawData = pd.DataFrame(RawData.iloc[ : , 0 ].str.split( ',').tolist())

#print(RawData)


indices = [[1,0,2,3] , [4,0,5,6]]

df = pd.DataFrame(columns=['Total','=sum(D:D)'])


FinalData = []
TheEnd = pd.DataFrame( columns=['Profile','Date', 'Time','Score'])

def stackAndFrame(Data, Stacks):
    
    for s in Data.index:
        OneRawData = Data.iloc[s]

         
        cumSum = len(Stacks)

        i = 0 - cumSum

        while i < cumSum:
                

        

            
        
            v =  np.array(OneRawData[Stacks[i]])
            #v2 = np.array(OneRawData[Stacks[1]])
            i = i +1
            FinalData.append(v)
            #FinalData.append(v2)  
            return FinalData
         

        
        #np.array(Testit[indices[0]])
stackAndFrame(RawData, indices) 

Finalv = pd.DataFrame(FinalData,columns=['Profile','Date', 'Time','Score'])

Finalv["Date"] = pd.to_datetime(Finalv["Date"], errors='coerce')

Finalv = Finalv[Finalv['Date'].dt.strftime('%Y%m') != '201808']

Finalv['Date'] = Finalv['Date'].dt.strftime('%Y%m%d')



Finalv['Time'] = pd.to_datetime(Finalv["Time"], errors='coerce')

Finalv['Time'] = Finalv['Time'].dt.strftime('%H:%M:%S')

Finalv['Score'] = Finalv['Score'].astype(float)


                

                



writer = pd.ExcelWriter('TestBook.xlsx', engine='xlsxwriter')


Finalv.to_excel(writer,sheet_name='Completed',index=False)
df.to_excel(writer,sheet_name='Completed',startcol=5,index=False)  

writer.save()

workbook  = writer.book
worksheet = writer.sheets['Completed']




