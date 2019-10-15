import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('Masukkan argument nama file output')
    sys.exit()
else:
    fileName = sys.argv[1]

try:
    file = open(fileName+".txt", "r")
except IOError:
    print ("Oops, can't open the file!")

data = file.read()
data = data.splitlines()
no = 0;
for url in data:
    print("Downloading", url)
    page = requests.get(url)
    data = BeautifulSoup(page.text, "html.parser")
    try:
        f = open(str(no)+".html", "w+")
        f.write(str(data))
        f.close()
        no += 1;
    except IOError:
        print("Can't download", url)
