import csv

with open('C:/Users/NammaYamini/OneDrive - M2P Solutions Private Limited/projects/others/compressor/size-compared-updation/batch10-update_non_audited_records_12thApril2023.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if int(row[6]) > 100000:
            with open('C:/Users/NammaYamini/OneDrive - M2P Solutions Private Limited/projects/others/compressor/filtered-lists/batch10-update_non_audited_records_12thApril2023.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row)
