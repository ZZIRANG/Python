import csv
seodaemun=[]
header=[]
rownum=0

with open("miso.csv","r", encoding="cp949") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        if "둔산로" in row[2]:
            print(row[0], row[2])