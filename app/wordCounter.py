import os
import socket

directory = os.path.dirname(os.path.realpath(__file__))
dataDirectory = directory+r"/home/data"
totalWords = 0
maxwords = 0
fileWithMaxWords = ""
listOfFiles = ""

for filename in os.listdir(dataDirectory):
    filepath = os.path.join(dataDirectory, filename)
    if filename.endswith(".txt"):
        listOfFiles += filename+" "
        file = open(filepath)
        data = file.read()
        words = data.split()
        wordCount = len(words)
        if wordCount >= maxwords:
            maxwords = wordCount
            fileWithMaxWords = filename
        totalWords += wordCount
        file.close()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


line1 = f"Hostname: {hostname}"
line2 = f"IP Address: {ip_address}"
line3 = "Total Words: "+str(totalWords)
line4 = "Highest Words: "+str(maxwords)
line5 = "File with highest words: "+fileWithMaxWords
line6 = "List of files: "+listOfFiles



outputDirectoryPath = os.path.join(directory+r"\home", 'output')
if not os.path.isdir(outputDirectoryPath):
    os.mkdir(outputDirectoryPath)
outputfilePath = os.path.join(outputDirectoryPath, 'output.txt')
f = open(outputfilePath, 'w')
f.writelines([line1, line2+"\n", line3+"\n", line4+"\n", line5+"\n", line6])
