#!/usr/bin/env python3
# This just joins to audio files together, in case
# the segmenter incorrectly separated them
# Run from command line with: secnum , track1, track2
#
# Warning! No error handling
#
import sys, os
from pydub import AudioSegment

indir = "tnc/"
prefix = "tnc"
sep = "-"
soundformat = "wav"


s1 = indir + prefix + sep + str(sys.argv[1]).zfill(2) + sep + str(sys.argv[2]).zfill(2) + "." + soundformat
s2 = indir + prefix + sep + str(sys.argv[1]).zfill(2) + sep + str(sys.argv[3]).zfill(2) + "." + soundformat

sound1 = AudioSegment.from_file(s1, format= soundformat )
sound2 = AudioSegment.from_file(s2, format= soundformat)

combined = sound1 + sound2

combined.export(s1, format=soundformat)
os.remove(s2) # watch out! deleting sound2 