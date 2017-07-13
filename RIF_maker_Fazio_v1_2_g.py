#ATTENTION!!!
''' First you have prepare your base
This is properly amount and names of column Subject	Session	Procedure[Block]	egzemocena	motivationLevelList	przymiotniki	Running[Trial]	Slide3.RESP	Slide3.RT	studyPair	PracticeCategory	PracticeCue
next you have to remove polish sight in "przymiotniki" ś ->s , ę ->e, ź ->z, ą -> a, ł ->l and blank space
next delete 'warm up' and "Ubrania" '''

import csv

data = []
with open('C:/path', encoding="cp1252") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    readCSV = [x for x in readCSV if x[2] == 'Procedure[Block]' or x[2] == 'practicePhase'
               or x[2] == 'studyPhase' or x[2] == 'evaluationPhase' or x[2] == 'motivationLevel']

# Change columns names
    for row in readCSV:
        if row[2] == 'Procedure[Block]':
            row[2] = 'ProcBlock'


# Add copy of motivation condition
    for row in readCSV:
        if row[0] != 'Subject' and row[4] != '':
            subNum = row[0]
            motNum = row[4]
            for line in readCSV:
                if line[0] == subNum and line[4] == '':
                    line[4] = motNum
                else:
                    pass
# Concatenate items
    for row in readCSV:
        data.append(row)
        if row[2] == 'studyPhase':
            print('This is studyPhase method')
            var1 = row[9]
            var2 = var1[:var1.index(' ')]
            var1 = var1[:var1.index(' ')] + var1[var1.index('-') + 2:var1.index('-') + 4]
            row.append(var1)
            row.append(var2)
        elif row[2] == 'practicePhase':
            print('This is practicePhase method')
            var1 = row[10]+row[11]
            row.append(var1)
            var2 = row[10]
            row.append(var2)
        elif row[2] == 'evaluationPhase':
            print('This is evaluationPhase method')
            var1 = row[3]
            var2 = var1[var1.index('-')+2:]
            var1 = var1[var1.index('-')+2:] + var1[:2]
            row.append(var1)
            row.append(var2)
        else:
            pass

# Counting of items occurrences
for row in data:
    count = 0
    # row.append(count)
    if len(row) < 14:
        row.append(count)
        row.append(count)
    if row[2] == 'evaluationPhase':
        cat = row[13]
        subject = row[0]
        for line in data:
            if line[0] == subject and line[13] == cat:
                count += 1
            else:
                pass

    row.append(count)

for row in data:
    count = 0
    if row[2] == 'evaluationPhase':
        cat = row[12]
        subject = row[0]
        for line in data:
            if line[0] == subject and line[12] == cat:
                count += 1
            else:
                pass

    row.append(count)

# Assignment RIF stimulus to items
for row in data:
    if row[0] == 'Subject':
        row.append('Items')
    else:
        row.append(0)
        if row[14] == 16:
            row[16] = 3  # NRP
        elif row[14] == 28:
            if row[15] == 2:
                row[16] = 2  # RP-
            else:
                row[16] = 1  # RP+

# Assignment emotional value to adjectives
for row in data:
    if row[0] == 'Subject':
        row.append('przymEmo')
    else:
        if row[5] in ['wstretny', 'zlosliwy', 'bolesny', 'wredny', 'wrogi', 'okropny','wsciekly', 'grozny', 'smutny', 'zazdrosny']:
            row.append('1')
        elif row[5] in ['dobry','piekny','mily','zdrowy','uczciwy','radosny','przyjazny','wesoly','przyjemny','szczesliwy']:
            row.append('2')
        else:
            row.append('0')
# Compare adjectives emotional value and subject's answers and cutting of file

data = [x for x in data if x[7] == x[17] or x[2] == 'ProcBlock']

for line in data:
    del line[1:4]
    del line[2:5]
    del line[3:10]

with open('C:/path', 'w', newline='', encoding="cp1252") as outfile:
    writer = csv.writer(outfile, delimiter=';')
    for row in data:
        writer.writerow(row)
