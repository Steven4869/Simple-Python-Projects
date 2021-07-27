import csv
fields =[ 'Nmae', 'Age', 'Marks', 'Pass/Fail']
rows =[['Steven','20','77','Pass'],['Jai','19','88','Pass'],['Amar','18','15','Fail'],['Andy','20','55','Pass']]
filename="records.csv"
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)