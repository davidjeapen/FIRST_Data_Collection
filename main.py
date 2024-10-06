import csv
from py_pdf_parser.common import BoundingBox
fields = ['Zip Code','District']

rows = []
for data in response.css("span.info"):
    name = data.xpath("span/strong/a/text()").get()
    district = None
    if name is not None:
        # print(name)
        rows.append([name.strip()])
        district = data.xpath("span/small/text()")[1].get()
    if district is not None:
        rows[len(rows) - 1].append(district[9:])
        # print(district)

print(rows)

with open('zip_dist.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(data_list)