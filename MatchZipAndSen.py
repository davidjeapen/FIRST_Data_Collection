import csv

senDistrict = []
with open('SenatorData.csv') as senData:
    csvreader = csv.reader(senData, delimiter=',')
    for row in csvreader:
        senDistrict.append(row)

senDistDict = {}

repDistDict = {}
with open('RepData.csv') as repData:
    csvreader = csv.reader(repData, delimiter=',')
    for row in csvreader:
        if len(row[1]) < 3:
            repDistDict[row[1].strip()] = row[0]



zip_sen = {}
zip_rep = {}
with open('all_zip_dist.csv') as senData:
    csvreader = csv.reader(senData, delimiter=',')
    for row in csvreader:
        key = row[0].strip()
        if len(key) == 5:

            zip_rep[key] = [row[1].replace(' ', '')]
            zip_sen[key] = [row[2].replace(' ', '')]

            rep_districts = zip_rep[key][0].split(",")
            sen_districts = zip_sen[key][0].split(",")

            reps = []
            for rep_dist in rep_districts:
                reps.append(repDistDict.get(rep_dist))

            senators = []
            for sen_dist in sen_districts:
                senators.append(senDistDict.get(sen_dist))

            zip_rep[key].append(reps)
            zip_sen[key].append(senators)



zipsForDistrict = []
for row in enumerate(senDistrict):
    district = row[1]
    zipsForDistrict[i] = []
    for row2 in zip_sen:
        dist = row2[1].split(',')
        if dist.__contains__(district):
            zipsForDistrict[i].append(row2[0])

all_schools = []
with open('sd-export-public-schools-20240105.0951.csv') as schoolZips:
    csvreader = csv.reader(schoolZips, delimiter=',')
    for row in csvreader:
        data = []
        try:
            if int(row[7]) > 2 and not ('Exclusively' or 'Primarily') in row[17]:
                data.append(row[1])
                data.append(row[3])
                data.append(row[4])
                data.append(row[5])
                data.append(row[11])
                data.append(row[22])
                all_schools.append(data)
        except ValueError:
            pass


zip_sen = zip_sen[2:]

names = []
nums = []
for row in senDistrict:
    names.append(row[0])
    nums.append(row[1])


for key in zip_sen:
    districts = zip_sen[key][0].strip(' ').split(",")
    senators = []
    for dist in districts:
        senators.append(senDistDict.get(dist))
    zip_sen[key].append(senators)

for key in zip_rep:
    districts = zip_rep[key][0].strip(' ').split(",")
    reps = []
    for dist in districts:
        reps.append(repDistDict.get(dist))
    zip_sen[key].append(reps)

zips = []
distSen = []

for row in zip_sen:
    zips.append(row[0])
    distSen.append([row[1], row[2]])

senNameDict = {zips[i]: distSen[i] for i in range(len(zips))}

mshs[i] = mshs[i][:5]

for i, school in enumerate(mshs):
    if len(school) == 5:
        try:
            mshs[i].append(zip_rep.get(school[4])[0])
            mshs[i].append(zip_rep.get(school[4])[1])
            mshs[i].append(zip_sen.get(school[4])[0])
            mshs[i].append(zip_sen.get(school[4])[1])
        except TypeError:
            print("Line ", i, " has an invalid zipcode")


for i, school in enumerate(all_schools):
    if len(school) == 6:
        key = school[4].strip()
        try:
            all_schools[i].append(zip_rep.get(key)[0])
            all_schools[i].append(zip_rep.get(key)[1])
            all_schools[i].append(zip_sen.get(key)[0])
            all_schools[i].append(zip_sen.get(key)[1])
        except TypeError:
            print(school[4], " has not been found")

senNameDict['53059'] = ['13', [senDistDict.get('13')]]


def reset_mshs():
    for i, row in enumerate(mshs):



