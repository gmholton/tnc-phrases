#!/usr/bin/env python3
# recognize text in audio clips
# then guess language based on result
# store results in json so we can process files later

# speech recognition
import speech_recognition as sr
import os, json

r = sr.Recognizer()

inpath = "clips/"

out = {}
count = 0
for fn in os.listdir(inpath):
    if fn.endswith('wav'):
        count += 1
        print('\r',count, fn, '       ',end ='')
        src = sr.AudioFile(os.path.join(inpath,fn))
        with src as source:
            audio = r.record(src)
        try:
            result=r.recognize_google(audio,show_all=True)
            if len(result) > 0:
                if 'confidence' in result['alternative'][0]:
                    confidence = result['alternative'][0]['confidence']
                else:
                    confidence = 0
                txt = result['alternative'][0]['transcript']
                # print(f"{fn}: {txt} ({confidence})")

            else:
                # empty result
                txt = ""
                confidence = 0
        except sr.UnknownValueError:
            # recognizer fails
            txt = ""
            confidence = 0
        except sr.RequestError as e:
            # recognizer unreachable??
            txt = "ERROR"
            confidence = 0

        # guess language as tanacross if low confidence
        # unless it has the word "number", which for some reason
        # also has low confidence
        if confidence < .9 and 'number' not in txt:
            lang = 'tnc'
        else:
            lang = 'eng'

        out.update( {fn : {'text':txt, 'confidence':confidence, 'language': lang } })
                 
with open('test.json', 'w') as convert_file:
     convert_file.write(json.dumps(out, indent=4))
print("DONE")