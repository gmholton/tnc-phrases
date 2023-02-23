#!/usr/bin/env python3
# split the phrases csv database
# so that items separated by "//" made
# into separate entries (matching the audio files)
#
# renumber the 'order' column accordingly
#
import os, re, csv

data = '../_data/phrases.csv'
outfile = '../_data/phrases2.csv'

# if not os.path.exists(outfile):
#     os.makedirs(outfile)

with open(data, "r") as f:
    csv_reader = csv.DictReader(f)
    phrases = list(csv_reader)
    # q = [ph for ph in phrases if ph['secnum'] == sec]
    
    cat = []
    sec = 1
    while sec < 30:
        secphrases = [ph for ph in phrases if ph['secnum'] == str(sec)]
        order = 1
        for ph in secphrases:
            tnc = ph['tnc'].split('//')
            eng = ph['eng'].split('//')
            if len(tnc) == len(eng):
                i = 0
                while i < len(tnc):
                    line = {'secnum':int(ph['secnum']), 
                            'order':int(order),
                             'section': ph["section"],
                            'tnc': tnc[i].strip(),
                            'eng': eng[i].strip(),
                            'audio':''}
                    cat.append(line)
                    order += 1
                    i += 1
            else:
                line = {'secnum':int(ph['secnum']),
                        'order':int(order),
                        'section':ph['section'],
                        'tnc':tnc,
                        'eng':eng,
                        'audio':''}
                cat.append(line)
                order += 1
                print("Mismatched separator",ph['secnum'],", ", ph['order'])
        sec += 1
    
with open(outfile, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(cat[0].keys()), quoting = csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    writer.writerows(cat)                    
            