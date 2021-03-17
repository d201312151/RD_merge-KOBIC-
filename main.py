#-*-coding: utf-8 -*-

import os, re
import pandas as pd

path = "/home/runner/RDmergeKOBIC/MK"

listd = os.listdir(path)
list1 = listd[0] #KOBIC에서는 0
list2 = listd[1] #KOBIC에서는 1

RD1 = pd.read_excel("{}/{}".format(path,list1))

RD2 = pd.read_csv("{}/{}".format(path,list2))
RD2 = RD2.iloc[12:]
RD2 = RD2.rename(columns = RD2.iloc[0])
RD2 = RD2.iloc[1:]

indexs = list(RD1["Name"])
columns = list(range(len(RD1)))
dict_mk = dict(zip(indexs, columns))
df_columns = list(RD2["Assay"])
df_columns = df_columns[:96]

df = pd.DataFrame(dict_mk, index = indexs, columns = df_columns)

for k, i in enumerate(list(RD1["ID"])) :
    SID = "ID.str.contains(@i)"
    RD22 = RD2.query(SID)
    RD22 = RD22.loc[:, ["Assay", "Converted"]]
    RD22.index = list(RD22["Assay"])
    RD22 = RD22.transpose()
    RD22 = RD22.iloc[1] ## type: series
    for l in range(len(df_columns)) :
        df.loc[df.index == indexs[k],df_columns[l]] = RD22[l]


df.replace(r'\W','',regex=True, inplace = True)
df.replace('NoCall', 'FL', inplace = True)
print(df)

#df.to_excel("/home/runner/RDmergeKOBIC/test.xlsx")

##Reference
#https://blog.naver.com/wideeyed/221867273249 Query 함수 사용법
#https://ponyozzang.tistory.com/614 Datafram replace regex 사용법
