import sys
import requests
from bs4 import BeautifulSoup
import os
import download

if len(sys.argv) < 2:
    print('Masukkan argument nama file output')
    sys.exit()
else:
    fileName = sys.argv[1]

try:
    file = open(fileName+".txt", "a+")
except IOError:
    print ("Oops, can't open the file!")

tglAwal     = 1
tglAkhir    = 2
blnAwal     = 1
blnAkhir    = 1
thnAwal     = 2019
thnAkhir    = 2019
jmlHalaman  = 5

allUrls = {}

for tahun in range(thnAwal, thnAkhir+1):
    for bulan in range(blnAwal, blnAkhir+1):
        for tanggal in range(tglAwal, tglAkhir+1):
            for halaman in range(1,jmlHalaman+1):
                indexUrl = "https://news.detik.com/indeks/all/"+str(halaman)+"?date="+("{:02}".format(bulan))+"/"+("{:02}".format(tanggal))+"/"+str(tahun)
                page = requests.get(indexUrl)
                data = BeautifulSoup(page.text, "html.parser")
                for div in data.find_all("div", class_="desc_idx ml10"):
                    url = div.find('a').get('href');
                    if url not in allUrls.keys():
                        allUrls[url] = 0


for key in allUrls:
    file.write(key+'\n')

print("Berhasil mendapatkan", len(allUrls), "url")

willDownload = input("Ingin mendownload semua halaman?[Y/n]")
if willDownload in ['y', 'Y', '\n'] :
    os.system('python download.py '+fileName)
