#lettura file.csv
from csv import reader,writer

fp_in=open("movies.csv","r")
fp_out=open("movies_byYr.CSV","w",newline="")
csvReader1=reader(fp_in)
csvWriter1=writer(fp_out)
yr="2009"
for row in csvReader1:
   # print(row)
   # print(row[0],"|",row[-1])
   if row[-1]==yr:
       print(row[0], "|", row[-1])
       csvWriter1.writerow(row)






fp_in.close()