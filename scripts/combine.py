#!/usr/bin/env python3
# append f2 to f1
import sys, os
from pydub import AudioSegment

s1 = 'tnc/tnc-' + str(sys.argv[1]).zfill(2) + "-" + str(sys.argv[2]).zfill(2) + ".wav"
s2 = 'tnc/tnc-' + str(sys.argv[1]).zfill(2) + "-" + str(sys.argv[3]).zfill(2) + ".wav"

sound1 = AudioSegment.from_file(s1, format="wav")
sound2 = AudioSegment.from_file(s2, format="wav")

combined = sound1 + sound2

combined.export(s1, format="wav")
os.remove(s2)