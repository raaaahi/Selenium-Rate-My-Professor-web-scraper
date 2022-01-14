


#function for loop for each line of CSV
import csv
import newTry
import pandas as pd
import time

f = open('rmp list.csv') #your orignal list that has all the profs/teachers in a vertical list where prof full name is in the first columnn

csv_f = csv.reader(f)
#i = 0
rope = ""

outF = open("myOutFile.txt", "a")
outF.write("Professor,Quality Score\n")
outF.close()



for row in csv_f:

    rope=row[0]  #gets the prof name in the first column of that row
    newTry.work(rope)




print("generating CSV...")
read_file = pd.read_csv(r'myOutFile.txt')
read_file.to_csv(r'myOutFile.csv', index=None)

csvData = pd.read_csv("myOutFile.csv")

csvData.sort_values(csvData.columns[1],
                    axis=0,
                    ascending=False,
                    inplace=True)

    #rather than overwriting each csv file, lets generate a new one by creating a new csv file name per run
dName = "myOutFile"  #default name of file
ms = str(int(round(time.time() % 1000))) #takes the time, and responds with seconds/ms identifier, cleaner that using RNG
csvData.to_csv(dName+ms+".csv", index=None) #creates readable new sorted csv file


print(csvData)
# writer = csv.writer(open("outputfile.csv", 'w'))


print("CSV generated as: " +dName+ms+".csv") #name of your file



print("all done!")
f.close()