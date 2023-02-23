#!/usr/bin/env python3
# convert to mp3

from pydub import AudioSegment
import os

# set up file paths
indir = "tnc-renum/"
outdir = "../assets/audio/"

# create the output directory if it doesn't exist
if not os.path.exists(indir):
	os.makedirs(outdir)
    
count = 0
for f in os.listdir(indir):
	if f.endswith(".wav"):
        # load the audio file
		inpath = os.path.join(indir, f)
		outfile = os.path.splitext(f)[0] + ".mp3"
		outpath = os.path.join(outdir, outfile)
		if not os.path.exists(outpath):
			AudioSegment.from_wav(inpath).export(outpath, format="mp3")
			count += 1

print(f"{count} mp3 files created")