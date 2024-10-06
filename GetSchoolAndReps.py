import csv

mshs = []

with open('sd-export-public-schools-20240105.0951.csv') as schoolZips:
    csvreader = csv.reader(schoolZips, delimiter=',')
    for row in csvreader:
        data = []
        if row[5].lower().__contains__("secondary" or "middle" or "high") and not row[8].lower().__contains__("Exclusively"):
            data.append(row[1])
            data.append(row[3])
            data.append(row[4])
            data.append(row[5])
            data.append(row[11])
            mshs.append(data)

zip_sen = []
with open('all_zip_dist.csv') as senData:
    csvreader = csv.reader(senData, delimiter=',')
    for row in csvreader:
        zip_sen.append([row[0]])
        zip_sen[len(zip_sen)-1].append(row[2])

with open('all_zip_dist.csv') as zip_dist:
    csvreader = csv.reader(zip_dist, delimiter=',')
    for row in csvreader:


for zipcode in zip_sen:


