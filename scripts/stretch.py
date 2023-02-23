#!/usr/bin/env python3
import os, re, csv

data = '../_data/phrases.csv'

with open(data, "r") as f:
	csv_reader = csv.DictReader(f)
	phrases = list(csv_reader)
    
	q = [ph for ph in phrases if phrases[0]['secnum'] == '5']

	print(q)