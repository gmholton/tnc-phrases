#!/usr/bin/env python3
# renumber clips by track
# this sorts the clips in each track (tnc-01, tnc-02, ...)
# then renumbers them sequentially with padded numbers, i.e.,
# tnc-01-01, tnc-01-02, ...
#
# Be sure to remove any non-Tanacross clips first
#

import os, re, shutil
import numpy as np

prefix = "tnc-"
ext = "wav"

indir = 'tnc/'
outdir =  'tnc-renum/'

if not os.path.exists(outdir):
	os.makedirs(outdir)
	 
files = [f for f in os.listdir(indir) if f.endswith('wav')]

alltracks = [f.split("-")[1] for f in files]
tracks = np.unique( np.array(alltracks))


for track in tracks:
	tracklist = [f for f in files if prefix+track in f ]
	tracklist.sort()
	clip = 0
	for f in tracklist:
		clip += 1
		newtrack = prefix + track + "-" + str(clip).zfill(2) + "." + ext
		shutil.copyfile(os.path.join(indir,f), os.path.join(outdir, newtrack))
	print(f"Track {track}: renumbered {clip} clips")

print("DONE")
