
from datetime import datetime
import os
import json

path = os.path.dirname(__file__)
file_name = os.path.join(path,'./transcript.txt')
timestamp_file = os.path.join(path,'./timestamp.txt')
data_file = os.path.join(path, './src/assets/data.json')

f = open(file_name, 'r', encoding = 'utf8')
t = open(timestamp_file, 'r', encoding= 'utf8')
d = open(data_file, 'w', encoding = 'utf8')

initial_time = datetime.strptime(t.readline(), '%H:%M:%S')
current_time = datetime.strptime("01:00:00", '%H:%M:%S')

while current_time < initial_time:
    line = f.readline().strip()
    if 'Time:' in line:
        current_time = line[6:]
        current_time = datetime.strptime(current_time, '%H:%M:%S')

initial_time = current_time
text = ""

while line != "":
    line = f.readline().strip()
    if line[:4] == "Text":
        text+=line[6:]+' '
    if line[:4] == "Time":
        current_time = line[6:]

total_time = datetime.strptime(current_time, '%H:%M:%S') - initial_time
total_words = text.count(' ')
with open(timestamp_file, 'w') as T:
    T.write(current_time)

data = {
    "groupNumber":1,
    "names": ["Sergio David Ferreira", "David Santiago Rojas"],
    "wordCount":total_words,
    "totalTime":round(total_time.total_seconds())
}

json_object = json.dumps(data, indent=4)
d.write(json_object)

#from transformers import pipeline

# Cargar pipeline para resumen
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#resumen = summarizer(text, max_length=total_words//2, min_length=20, do_sample=False)
#print(resumen[0]['summary_text'])
f.close()
t.close()
d.close()