import csv
seodaemun=[]
header=[]
rownum=0

with open("miso.csv","r", encoding="cp949") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row)