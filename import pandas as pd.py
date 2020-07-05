import pandas as pd
import numpy as np

RawData =  pd.DataFrame(pd.read_excel("vbaTest_Candidate.xlsm","Data",usecols = "A"))

RawData = pd.DataFrame(RawData.iloc[ : , 0 ].str.split( ',').tolist())



Testit= RawData.iloc[0]

indices = [[1,0,2,3] , [4,0,5,6]]

indi = [1,0,2,3]
indi2 = [4,0,5,6]

e = np.array(Testit[indices[0]])
s = np.array(Testit[indi2])

#showme = np.stack((e,s))

#shw = pd.DataFrame(showme)


#dataframe=pd.DataFrame(e, columns=['a']) 

print(e)