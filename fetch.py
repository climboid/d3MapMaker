#!/usr/bin/python

import urllib2
import zipfile
import os
import webbrowser
import subprocess

symbol_dic = {
  "PYF" :"french polynesia",
  "AND" :"andorra",
  "SLV" :"el salvador",
  "MRT" :"mauritania",
  "GEO" :"georgia",
  "TON" :"tonga",
  "GUF" :"french guiana",
  "NLD" :"netherlands",
  "TUV" :"tuvalu",
  "DOM" :"dominican republic",
  "SYC" :"seychelles",
  "COL" :"colombia",
  "JPN" :"japan",
  "BFA" :"burkina faso",
  "ISL" :"iceland",
  "SGP" :"singapore",
  "VNM" :"vietnam",
  "SVK" :"slovakia",
  "TZA" :"tanzania",
  "TLS" :"timor-leste",
  "GAB" :"gabon",
  "JOR" :"jordan",
  "SWE" :"sweden",
  "ARM" :"armenia",
  "QAT" :"qatar",
  "SHN" :"saint helena",
  "ATA" :"antarctica",
  "LTU" :"lithuania",
  "FLK" :"falkland islands",
  "SJM" :"svalbard and jan mayen",
  "BLZ" :"belize",
  "PER" :"peru",
  "ITA" :"italy",
  "MNP" :"northern mariana islands",
  "DEU" :"germany",
  "KGZ" :"kyrgyzstan",
  "PRI" :"puerto rico",
  "BDI" :"burundi",
  "AGO" :"angola",
  "KAZ" :"kazakhstan",
  "MLT" :"malta",
  "KIR" :"kiribati",
  "ATG" :"antigua and barbuda",
  "GIN" :"guinea",
  "MWI" :"malawi",
  "NRU" :"nauru",
  "BMU" :"bermuda",
  "VUT" :"vanuatu",
  "ESP" :"spain",
  "MSR" :"montserrat",
  "KNA" :"saint kitts and nevis",
  "IOT" :"british indian ocean territory",
  "REU" :"reunion",
  "GMB" :"gambia",
  "CPV" :"cape verde",
  "AFG" :"afghanistan",
  "CMR" :"cameroon",
  "IDN" :"indonesia",
  "SUR" :"suriname",
  "TWN" :"taiwan",
  "SEN" :"senegal",
  "LCA" :"santa lucia",
  "CRI" :"costa rica",
  "KOR" :"south korea",
  "SDN" :"sudan",
  "ASM" :"american samoa",
  "MNG" :"mongolia",
  "ANT" :"netherlands antilles",
  "WLF" :"wallis and futuna",
  "SPM" :"saint pierre and miquelon",
  "MYS" :"malaysia",
  "BRA" :"brazil",
  "THA" :"thailand",
  "RUS" :"russian federation",
  "MDA" :"moldova",
  "EGY" :"egypt",
  "COD" :"congo, the democratic republic of the",
  "NIU" :"niue",
  "BIH" :"bosnia and herzegovina",
  "DMA" :"dominica",
  "RWA" :"rwanda",
  "PLW" :"palau",
  "UKR" :"ukraine",
  "MAC" :"macao",
  "WSM" :"samoa",
  "GHA" :"ghana",
  "NOR" :"norway",
  "FIN" :"finland",
  "PAN" :"panama",
  "TGO" :"togo",
  "OMN" :"oman",
  "NCL" :"new caledonia",
  "BEN" :"benin",
  "UGA" :"uganda",
  "GLP" :"guadeloupe",
  "BEL" :"belgium",
  "ZAF" :"south africa",
  "BVT" :"bouvet island",
  "ARG" :"argentina",
  "LBY" :"libya",
  "PSE" :"palestina",
  "SMR" :"san marino",
  "EST" :"estonia",
  "TUN" :"tunisia",
  "NAM" :"namibia",
  "BRN" :"brunei darussalam",
  "BLR" :"belarus",
  "IRL" :"ireland",
  "SGS" :"south georgia and the south sandwich islands",
  "LBR" :"liberia",
  "URY" :"uruguay",
  "FSM" :"micronesia, federated states of ",
  "ZWE" :"zimbabwe",
  "GUY" :"guyana",
  "NIC" :"nicaragua",
  "BOL" :"bolivia",
  "GRL" :"greenland",
  "SAU" :"saudi arabia",
  "TKL" :"tokelau",
  "UZB" :"uzbekistan",
  "FRA" :"france",
  "ARE" :"united arab emirates",
  "ESH" :"western sahara",
  "AUS" :"australia",
  "MCO" :"monaco",
  "FJI" :"fiji",
  "LKA" :"sri lanka",
  "ERI" :"eritrea",
  "ATF" :"french southern territories",
  "ALA" :"aland islands",
  "NER" :"niger",
  "ZMB" :"zambia",
  "POL" :"poland",
  "CHL" :"chile",
  "YEM" :"yemen",
  "COG" :"congo, republic of",
  "CXR" :"christmas island",
  "MUS" :"mauritius",
  "SYR" :"syria",
  "HND" :"honduras",
  "GRD" :"grenada",
  "DJI" :"djibouti",
  "GRC" :"greece",
  "ISR" :"israel",
  "CCK" :"cocos islands",
  "GUM" :"guam",
  "CAN" :"canada",
  "VEN" :"venezuela",
  "SWZ" :"swaziland",
  "TUR" :"turkey",
  "NZL" :"new zealand",
  "LUX" :"luxembourg",
  "MKD" :"macedonia",
  "CZE" :"czech republic",
  "MOZ" :"mozambique",
  "VCT" :"saint vincent and the grenadines",
  "IMN" :"isle of man",
  "MNE" :"montenegro",
  "FRO" :"faroe islands",
  "UMI" :"united states minor outlying island",
  "BHS" :"bahamas",
  "LIE" :"liechtenstein",
  "HUN" :"hungary",
  "ALB" :"albania",
  "GNQ" :"equatorial guinea",
  "ROU" :"romania",
  "BGR" :"bulgaria",
  "LAO" :"laos",
  "HKG" :"hongkong",
  "MYT" :"mayotte",
  "SLE" :"sierra leone",
  "VIR" :"virgin islands, u.s",
  "ECU" :"ecuador",
  "TCA" :"turks and caicos islands",
  "BWA" :"botswana",
  "STP" :"sao tome and principe",
  "BGD" :"bangladesh",
  "JEY" :"jersey",
  "BRB" :"barbados",
  "DNK" :"denmark",
  "MHL" :"marshall islands",
  "PCN" :"pitcairn islands",
  "TKM" :"turkmenistan",
  "LSO" :"lesotho",
  "CHE" :"switzerland",
  "BHR" :"bahrain",
  "GBR" :"united kingdom",
  "KHM" :"cambodia",
  "MEX" :"mexico",
  "TCD" :"chad",
  "AZE" :"azerbaijan",
  "COK" :"cook islands",
  "AIA" :"anguilla island",
  "JAM" :"jamaica",
  "BTN" :"bhutan",
  "PNG" :"papua new guinea",
  "MDG" :"madagascar",
  "NPL" :"nepal",
  "PRY" :"paraguay",
  "NFK" :"norfolk island",
  "SLB" :"solomon islands",
  "GNB" :"guinea-bissau",
  "SRB" :"serbia",
  "GTM" :"guatemala",
  "MAR" :"morocco",
  "ABW" :"aruba",
  "CUB" :"cuba",
  "CAF" :"central african republic",
  "PRT" :"portugal",
  "CYM" :"cayman islands",
  "HMD" :"heard island and mcdonald islands",
  "IND" :"india",
  "HRV" :"croatia",
  "SVN" :"slovenia",
  "LBN" :"lebanon",
  "NGA" :"nigeria",
  "VGB" :"british virgin islands",
  "DZA" :"algeria",
  "USA" :"united states",
  "GIB" :"gibraltar",
  "CHN" :"china",
  "CIV" :"cote d'ivoire",
  "VAT" :"vatican",
  "MLI" :"mali",
  "KEN" :"kenya",
  "MMR" :"myanmar",
  "ETH" :"ethiopia",
  "HTI" :"haiti",
  "LVA" :"latvia",
  "MDV" :"maldives",
  "PRK" :"north korea",
  "CYP" :"cyprus",
  "KO-" :"kosova",
  "IRN" :"iran",
  "COM" :"comoros",
  "GGY" :"guernsey",
  "IRQ" :"iraq",
  "AUT" :"austria",
  "TTO" :"trinidad and tobago",
  "KWT" :"kuwait",
  "MTQ" :"martinique",
  "TJK" :"tajikistan",
  "PHL" :"philippines",
  "SOM" :"somalia",
  "PAK" :"pakistan"
}



# def find_key(dic, val):
#     #return the key of dictionary dic given the value
#     return [k for k, v in symbol_dic.iteritems() if v == val][0]

# # get the data
# countryToCreate = raw_input('Country name? ')
# # countryToCreate = countryToCreate.strip()

# countryToCreate = countryToCreate[:1].upper() + countryToCreate[1:].lower()
# fetchCountry = find_key(symbol_dic, countryToCreate)
# fetchCountry = fetchCountry[:3]

# url = "http://gadm.org/data/shp/"+fetchCountry+"_adm.zip"

# print url

# file_name = url.split('/')[-1]
# u = urllib2.urlopen(url)
# f = open(file_name, 'wb')
# meta = u.info()
# file_size = int(meta.getheaders("Content-Length")[0])
# print "Downloading: %s Bytes: %s" % (file_name, file_size)

# file_size_dl = 0
# block_sz = 8192
# while True:
#     buffer = u.read(block_sz)
#     if not buffer:
#         break

#     file_size_dl += len(buffer)
#     f.write(buffer)
#     status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
#     status = status + chr(8)*(len(status)+1)
#     print status,

# f.close()

# #unzip the files
# zfile = zipfile.ZipFile(file_name)

# for name in zfile.namelist():
#   (dirname, filename) = os.path.split(name)
#   print "Decompressing " + filename + " on " + os.getcwd()
#   fd = open(name,"w")
#   fd.write(zfile.read(name))
#   fd.close()

# #convert file names to lower case this is needed for GDAL to work
# for filename in os.listdir("."):
#     os.rename(filename, filename.lower())

# #convert the shp file into geojson
# toConvert = fetchCountry+'_adm1.shp'
# os.system('/Library/Frameworks/GDAL.framework/Programs/ogr2ogr -f "GeoJSON" output.json '+toConvert)

# #create the html file with all needed dependencies to make the map
# finalFile = '<!doctype html>'
# finalFile+='<html>'
# finalFile+='<head>'
# finalFile+='<meta charset="utf-8"/>'
# finalFile+='<title></title>'
# finalFile+='<script src="http://d3js.org/d3.v3.min.js"></script>'
# finalFile+='</head>'
# finalFile+='<body>'
# finalFile+='<div id="mapContainer"></div>'
# finalFile+='<script>'
# finalFile+='var path, vis, xy;'
# finalFile+='xy = d3.geo.mercator().scale(900);'
# finalFile+='path = d3.geo.path().projection(xy);'
# finalFile+='vis = d3.select("#mapContainer").append("svg:svg").attr("width", 960).attr("height", 600);'
# finalFile+='d3.json("output.json", function(json) {'
# finalFile+='return vis.append("svg:g").attr("class", "tracts").selectAll("path").data(json.features).enter().append("svg:path").attr("d", path).attr("fill-opacity", 0.5).attr("fill", "#85C3C0").attr("stroke", "#222");'
# finalFile+='});'
# finalFile+='</script>'
# finalFile+='</body>'
# finalFile+='</html>'

# def MakeFile(file_name):

#   temp_path = file_name
#   file = open(temp_path, 'w')
#   file.write(finalFile)
#   file.close()
#   print 'Execution completed. Map created successfully '

# MakeFile('index.html')

# subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '7777'])
# webbrowser.open_new_tab('localhost:7777')





