#!/usr/bin/python

import urllib2
import zipfile
import os
import webbrowser


# get the data
countryToCreate = raw_input('Please type the abbreviation of the country you want to create a map of. Example: AFG is Afghanistan, CAN is Canada.')
countryToCreate = countryToCreate.upper().strip()

url = "http://gadm.org/data/shp/"+countryToCreate+"_adm.zip"

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

#unzip the files
zfile = zipfile.ZipFile(file_name)

for name in zfile.namelist():
  (dirname, filename) = os.path.split(name)
  print "Decompressing " + filename + " on " + os.getcwd()
  fd = open(name,"w")
  fd.write(zfile.read(name))
  fd.close()

#convert file names to lower case this is needed for GDAL to work
for filename in os.listdir("."):
    os.rename(filename, filename.lower())

#convert the shp file into geojson
toConvert = countryToCreate+'_adm1.shp'
os.system('/Library/Frameworks/GDAL.framework/Programs/ogr2ogr -f "GeoJSON" output.json '+toConvert)

#create the html file with all needed dependencies to make the map
finalFile = '<!doctype html>'
finalFile+='<html>'
finalFile+='<head>'
finalFile+='<meta charset="utf-8"/>'
finalFile+='<title></title>'
finalFile+='<script src="http://d3js.org/d3.v3.min.js"></script>'
finalFile+='</head>'
finalFile+='<body>'
finalFile+='<div id="mapContainer"></div>'
finalFile+='<script>'
finalFile+='var path, vis, xy;'
finalFile+='xy = d3.geo.mercator().scale(900);'
finalFile+='path = d3.geo.path().projection(xy);'
finalFile+='vis = d3.select("#mapContainer").append("svg:svg").attr("width", 960).attr("height", 600);'
finalFile+='d3.json("output.json", function(json) {'
finalFile+='return vis.append("svg:g").attr("class", "tracts").selectAll("path").data(json.features).enter().append("svg:path").attr("d", path).attr("fill-opacity", 0.5).attr("fill", "#85C3C0").attr("stroke", "#222");'
finalFile+='});'
finalFile+='</script>'
finalFile+='</body>'
finalFile+='</html>'

def MakeFile(file_name):

  temp_path = file_name
  file = open(temp_path, 'w')
  file.write(finalFile)
  file.close()
  print 'Execution completed. Map created successfully '

MakeFile('index.html')

os.system('python -m SimpleHTTPServer 7777')




