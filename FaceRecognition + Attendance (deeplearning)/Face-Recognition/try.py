import pandas as pd
import time
from datetime import datetime

name="Md.Mazher 303302817022"
k=name.split(' ')
print(k[0])



'''def markk(k):
    timing=input("enter time")
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if k[0] not in nameList:
            #now = datetime.now()
            #dtString = now.strftime('%H:%M')
            #if dtString == ('08:00'):
            if timing == "08:00" or timing == "09:00" or timing == "10:00" or timing == "11:00" :
                f.writelines(f'\n{timing},{k[0]},{k[1]},{str(1)}')
            
                

while True:
    markk(k)'''
'''
k=input("enter k")
j=input("enter k")

income1 = pd.DataFrame({'Names':[k],
                   'Salary':[j]})
income1.to_excel("education_salary.xls")
print(income1)


'''
'''

def mark(k):
    df = pd.read_excel("raw_data.xls")
    now = datetime.now()
    dtString = now.strftime('%H:%M')
    if dtstring == "08:00":
        income= 
    
mark(k)'''





df = pd.DataFrame(columns=["Name", "Roll-Number", "Sub1"])


#parts = int(input("Enter the number of day parts:"))
#timing = input("Enter time")

while True:
    #adf = pd.read_excel("education_salary3.xls")
    timing = input("Enter time")
    if timing == "08:00" or timing == "09:00":
        dp = input("Name ")
        st = input("Rollnumber {}".format(dp))
        et = input("sub1 {}".format(dp))
        df1 = pd.DataFrame(data=[[dp,st,et]],columns=["Name", "Roll-Number", "Sub1"])
        df = pd.concat([df,df1], axis=0)
    else:
        break

df.index = range(len(df.index))
df.to_excel('education_salary3.xls')
print(df)







