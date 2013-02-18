import urllib2
import zipfile
import os

url = "http://gadm.org/data/shp/AFG_adm.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

zfile = zipfile.ZipFile(file_name)
print "in here and i dont have a zip file yet", file_name

for name in zfile.namelist():
  (dirname, filename) = os.path.split(name)
  print "Decompressing " + filename + " on " + os.getcwd()
  fd = open(name,"w")
  fd.write(zfile.read(name))
  fd.close()