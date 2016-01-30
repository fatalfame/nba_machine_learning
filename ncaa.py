import csv as csv

files = ('../Code/ncaa_machine_learning/inputs/arizona.csv', '../Code/ncaa_machine_learning/inputs/duke.csv')

fieldnames = ['W-L%', 'PTS', 'SOS', 'Season']
writer = csv.DictWriter(open('..//Code/ncaa_machine_learning/outputs/team_features.csv', 'wb'),
                        fieldnames=fieldnames)
writer.writeheader()
for file_names in files:
    input_file = open(file_names, 'rt')
    reader = csv.DictReader(input_file)
    for row in reader:
        print row
        for value in row.iteritems():
            writer.writerow({'Season': row['Season'], 'W-L%': row['W-L%'], 'PTS': row['PTS'], 'SOS': row['SOS']})

