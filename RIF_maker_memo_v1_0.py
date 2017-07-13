import csv

data = []
with open('RIF_merge_prb_v2.csv', encoding="cp1252") as csvfile:
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
    if len(row) < 17:
        row.append(count)
        row.append(count)
    if row[2] == 'evaluationPhase':
        cat = row[16]
        subject = row[0]
        for line in data:
            if line[0] == subject and line[16] == cat:
                count += 1
            else:
                pass

    row.append(count)

for row in data:
    count = 0
    if row[2] == 'evaluationPhase':
        cat = row[15]
        subject = row[0]
        for line in data:
            if line[0] == subject and line[15] == cat:
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
        if row[17] == 16:
            row[19] = 3  # NRP
        elif row[17] == 28:
            if row[18] == 2:
                row[19] = 2  # RP-
            else:
                row[19] = 1  # RP+

            ''' oznaczyć przymiotniki pozytywne i nehgatywne i poónweqać je z reakacją a potem dodac filtr
            nie musze tego robić dla odpamiętywania '''

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
'''
for row in data:
    if row[7] == row[20]:
        row.append('good')
    else:
        row.append('not')'''
data = [x for x in data if x[7] == x[20] or x[2] == 'ProcBlock']

'''for line in data:
    del line[1:4]
    del line[2:5]
    del line[3:13]'''

for line in data:
    del line[1:3]
    del line[3:4]
    del line[3:16]
    del line[4]

#data = [x for x in data if x[2] == 'evaluationPhase' or x[2] == 'motivationLevel' or x[2] == 'Procedure[Block]']


with open('RIF_merge_output_v2_memo.csv', 'w', newline='', encoding="cp1252") as outfile:
    writer = csv.writer(outfile, delimiter=';')
    for row in data:
        writer.writerow(row)

'''
    readCSV = [x for x in readCSV if x[2] == 'Procedure[Block]'or x[2] == 'practicePhase'
               or x[2] == 'studyPhase' or x[2] == 'evaluationPhase'or x[2] == 'motivationLevel']
# Add copy of motivation condition

    for row in readCSV:
        if row == 0:
            motCol = row.index('motivationLevelList')
        for line in readCSV:
            if line[0] != '' and line[motCol] != '':
                subNum = line[0]
                motCond = line[motCol]
            elif line[0] != '' and line[motCol] == '':
                line[motCol] = subNum


'''
'''
    for row in readCSV:
        if row[0] == 'Subject':
            pass
        elif row[0] != 'Subject' and row[4] != '':
            subNum = row[0]
            motNum = row[4]
        elif row[0] != 'Subject' and row[4] == '':
            row[4] = motNum
'''