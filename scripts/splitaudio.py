#!/usr/bin/env python3
# split ripped audio tracks into chunks

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# set up file paths
indir = "wav/"
outdir = "clips/"

# create the output directory if it doesn't exist
if not os.path.exists(outdir):
    os.makedirs(outdir)

# define the silence threshold (in dB)
silence_thresh = -50 # -50
min_silence = 300

# Iterate over all the files in the directory
for file_name in os.listdir(indir):
    if file_name.endswith(".wav"):
        # load the audio file
        audio_file = AudioSegment.from_wav(indir + file_name)

        # split the audio file into chunks on the basis of silence
        audio_chunks = split_on_silence(audio_file, min_silence_len=min_silence, silence_thresh=silence_thresh)

        # export each audio chunk as a separate file
        track = os.path.splitext(file_name)[0]
        count = 1
        for i, chunk in enumerate(audio_chunks):
            chunk.export(os.path.join(output_dir_path, f"tnc-{track}-{i.zfill(2)}.wav"), format="wav")
            count += 1
        print(f"File {file_name} split into {count} chunks.")
