import csv

sleep_data = []

with open('sleepdata.csv') as f:
    all_data = csv.reader(f, delimiter=';')

    for entry in all_data:
        if 'Start' in entry: # dont do anything with the first row
            pass
        else:
            new_entry = {}
            new_entry['Start'] = entry[0]
            new_entry['End'] = entry[1]
            new_entry['Sleep Quality'] = entry[2]
            new_entry['Time in bed'] = entry[3]
            new_entry['Wake up'] = entry[4]
            new_entry['Sleep Notes'] = entry[5]
            sleep_data.append(new_entry)

print sleep_data
