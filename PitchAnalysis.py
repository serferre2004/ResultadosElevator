
from datetime import datetime
import csv
import os
import json

path = os.path.dirname(__file__)
file_name = os.path.join(path,'./transcript.txt')
timestamp_file = os.path.join(path,'./timestamp.txt')
data_file = os.path.join(path, './src/assets/data.json')

f = open(file_name, 'r', encoding = 'utf8')
t = open(timestamp_file, 'r', encoding= 'utf8')
d = open(data_file, 'w', encoding = 'utf8')

    
stamp = t.readline().split('|')
initial_time = datetime.strptime(stamp[0], '%H:%M:%S')
current_time = datetime.strptime("01:00:00", '%H:%M:%S')
with open('turnos.csv', encoding='utf8') as fd:
    reader=csv.reader(fd)
    interestingrows=[row for idx, row in enumerate(reader) if idx == int(stamp[1])+1]
info_group = interestingrows[0][0]
info_group = info_group.strip().split(';')

while current_time <= initial_time:
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
palabras = text.split()  # Divide el texto por espacios
palabras_normalizadas = [palabra.lower() for palabra in palabras]
palabras_unicas = set(palabras_normalizadas)
total_words = len(palabras)
unique_words = len(palabras_unicas)
prcnt = round(unique_words/total_words*100)
with open(timestamp_file, 'w', encoding='utf8') as T:
    T.write(current_time+"|"+str(int(stamp[1])+1))

data = {
    "groupNumber":info_group[0],
    "names": [info_group[2]],
    "groupName":info_group[1],
    "wordCount":total_words,
    "uniquePrcnt": prcnt,
    "totalTime":round(total_time.total_seconds())
}

json_object = json.dumps(data, indent=4)
d.write(json_object)

f.close()
t.close()
d.close()