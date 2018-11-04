#Different filenames (like ../../flag1.jpg,../../flag23.jpg,../../turn13.jpg)  with their file paths are stored in a csv.
"The aim is to sort of all filenames with 'flag and 'turn' together"

import numpy as np
import pandas as pd

df =pd.read_csv(r'D:\path\to\the\folder\file.csv')
filenames= df['filename']
flags=[]
turns=[]
path=''

for file in filenames:
    filepath= file.split('/')
    lastchar= filepath[-1]
    number= lastchar[lastchar.find("(") + 1:lastchar.find(")")]
    # print(lastchar.split(' ')[0])
    if (lastchar.split(' ')[0]=='flag'):
        path=file.split('flag')[0]
        flags.append(int(number))
    elif (lastchar.split(' ')[0]=='turn'):
        turns.append(int(number))
# print(len(flags))
# print(len(turns))


flags= np.sort(flags)
turns=np.sort(turns)

# print(len(flags))
# print(len(turns))

turnpaths=[]
flagpaths=[]

for each in flags:
    flagpaths.append(path+'flag ('+str(each)+').JPG')
for each in turns:
    turnpaths.append(path+'turn ('+str(each)+').JPG')

indexs=[]
for each in flagpaths:
   indexs.append(df.index[df.filename==each][0])
for each in turnpaths:
   indexs.append(df.index[df.filename==each][0])

outputdf= df.reindex(indexs)
outputdf.to_csv(r'D:\save\to\the\folder\sorted.csv')
print(outputdf)
# print(filenames)


