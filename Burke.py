import pandas as pd
import numpy as np

RawData = pd.DataFrame(pd.read_excel("vbaTest_Candidate.xlsm","Data",usecols = "A")).squeeze

ls = []

ls = RawData.columns

#RawData.rename(columns={RawData.columns[0]: "Raw Data" }, inplace = True)

new = RawData.str.split(",", n = 7, expand = True) 

new.stack([1,2,3],[4,5,6])
 

print(new)

####MegaList = (FirstProfile = new[[1,0,2,3]],
#####SecondProfile = new[[4,0,5,6]])


def rename(dataset) :
    
        dataset.rename(columns={ dataset.columns[0]: 'Profile' ,
        dataset.columns[1]: 'Date',
        dataset.columns[2]: 'Time',
        dataset.columns[3]: 'Score',
        }, inplace = True)


#rename(FirstProfile)
#rename(SecondProfile)


#FirstProfile.rename(columns={ FirstProfile.columns[0]: 1 ,
#FirstProfile.columns[1]: 0,
#FirstProfile.columns[2]: 2,
#FirstProfile.columns[3]: 3,
#}, inplace = True)




#SecondProfile.rename(columns={ SecondProfile.columns[0]: 1 ,
#SecondProfile.columns[1]: 0,
#SecondProfile.columns[2]: 2,
#SecondProfile.columns[3]: 3,
#}, inplace = True)

#RawData.rename(columns={ RawData.columns[0]: "Raw Data"}, inplace = True)


#MergeData = FirstProfile.append(SecondProfile)



#df[1] = pd.to_datetime(MergeData)






#pd.DataFrame.merge(FirstProfile, SecondProfile, how="outer", on=list(FirstProfile.columns))





#MergeData = [FirstProfile, SecondProfile]

#CleanedData = pd.concat(MergeData)



#print(MegaList)
#print(SecondProfile)
#print(UseColumn[0])
#print(UseColumn.index)
#print(UseColumn)
#print(CleaednData2)
#print(x2)