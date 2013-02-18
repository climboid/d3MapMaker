#!/usr/bin/python

import urllib2
import zipfile
import os
import webbrowser
import subprocess

symbol_dic = {
     "AFG_Afghanistan":"Afghanistan",
     "ALA_Aland Islands":"Aland Islands",
     "ALB_Albania":"Albania",
     "DZA_Algeria":"Algeria",
     "ASM_American Samoa":"American Samoa",
     "AND_Andorra":"Andorra",
     "AGO_Angola":"Angola",
     "AIA_Anguilla Island":"Anguilla Island",
     "ATA_Antarctica":"Antarctica",
     "ATG_Antigua and Barbuda":"Antigua and Barbuda",
     "ARG_Argentina":"Argentina",
     "ARM_Armenia":"Armenia",
     "ABW_Aruba":"Aruba",
     "AUS_Australia":"Australia",
     "AUT_Austria":"Austria",
     "AZE_Azerbaijan":"Azerbaijan",
     "BHS_Bahamas":"Bahamas",
     "BHR_Bahrain":"Bahrain",
     "BGD_Bangladesh":"Bangladesh",
     "BRB_Barbados":"Barbados",
     "BLR_Belarus":"Belarus",
     "BEL_Belgium":"Belgium",
     "BLZ_Belize":"Belize",
     "BEN_Benin":"Benin",
     "BMU_Bermuda":"Bermuda",
     "BTN_Bhutan":"Bhutan",
     "BOL_Bolivia":"Bolivia",
     "BIH_Bosnia and Herzegovina":"Bosnia and Herzegovina",
     "BWA_Botswana":"Botswana",
     "BVT_Bouvet Island":"Bouvet Island",
     "BRA_Brazil":"Brazil",
     "IOT_British Indian Ocean Territory":"British Indian Ocean Territory",
     "VGB_British Virgin Islands":"British Virgin Islands",
     "BRN_Brunei Darussalam":"Brunei Darussalam",
     "BGR_Bulgaria":"Bulgaria",
     "BFA_Burkina Faso":"Burkina Faso",
     "BDI_Burundi":"Burundi",
     "KHM_Cambodia":"Cambodia",
     "CMR_Cameroon":"Cameroon",
     "CAN_Canada":"Canada",
     "CPV_Cape Verde":"Cape Verde",
     "CYM_Cayman Islands":"Cayman Islands",
     "CAF_Central African Republic":"Central African Republic",
     "TCD_Chad":"Chad",
     "CHL_Chile":"Chile",
     "CHN_China":"China",
     "CXR_Christmas Island":"Christmas Island",
     "CCK_Cocos Islands":"Cocos Islands",
     "COL_Colombia":"Colombia",
     "COM_Comoros":"Comoros",
     "COG_Congo, Republic of":"Congo, Republic of",
     "COD_Congo, The Democratic Republic of the":"Congo, The Democratic Republic of the",
     "COK_Cook Islands":"Cook Islands",
     "CRI_Costa Rica":"Costa Rica",
     "CIV_Cote d'Ivoire":"Cote d'Ivoire",
     "HRV_Croatia":"Croatia",
     "CUB_Cuba":"Cuba",
     "CYP_Cyprus":"Cyprus",
     "CZE_Czech Republic":"Czech Republic",
     "DNK_Denmark":"Denmark",
     "DJI_Djibouti":"Djibouti",
     "DMA_Dominica":"Dominica",
     "DOM_Dominican Republic":"Dominican Republic",
     "ECU_Ecuador":"Ecuador",
     "EGY_Egypt":"Egypt",
     "SLV_El Salvador":"El Salvador",
     "GNQ_Equatorial Guinea":"Equatorial Guinea",
     "ERI_Eritrea":"Eritrea",
     "EST_Estonia":"Estonia",
     "ETH_Ethiopia":"Ethiopia",
     "FLK_Falkland Islands":"Falkland Islands",
     "FRO_Faroe Islands":"Faroe Islands",
     "FJI_Fiji":"Fiji",
     "FIN_Finland":"Finland",
     "FRA_France":"France",
     "GUF_French Guiana":"French Guiana",
     "PYF_French Polynesia":"French Polynesia",
     "ATF_French Southern Territories":"French Southern Territories",
     "GAB_Gabon":"Gabon",
     "GMB_Gambia":"Gambia",
     "GEO_Georgia":"Georgia",
     "DEU_Germany":"Germany",
     "GHA_Ghana":"Ghana",
     "GIB_Gibraltar":"Gibraltar",
     "GRC_Greece":"Greece",
     "GRL_Greenland":"Greenland",
     "GRD_Grenada":"Grenada",
     "GLP_Guadeloupe":"Guadeloupe",
     "GUM_Guam":"Guam",
     "GTM_Guatemala":"Guatemala",
     "GGY_Guernsey":"Guernsey",
     "GIN_Guinea":"Guinea",
     "GNB_Guinea-Bissau":"Guinea-Bissau",
     "GUY_Guyana":"Guyana",
     "HTI_Haiti":"Haiti",
     "HMD_Heard Island and McDonald Islands":"Heard Island and McDonald Islands",
     "HND_Honduras":"Honduras",
     "HKG_Hongkong":"Hongkong",
     "HUN_Hungary":"Hungary",
     "ISL_Iceland":"Iceland",
     "IND_India":"India",
     "IDN_Indonesia":"Indonesia",
     "IRN_Iran":"Iran",
     "IRQ_Iraq":"Iraq",
     "IRL_Ireland":"Ireland",
     "IMN_Isle of Man":"Isle of Man",
     "ISR_Israel":"Israel",
     "ITA_Italy":"Italy",
     "JAM_Jamaica":"Jamaica",
     "JEY_Jersey":"Jersey",
     "JPN_Japan":"Japan",
     "JOR_Jordan":"Jordan",
     "KAZ_Kazakhstan":"Kazakhstan",
     "KEN_Kenya":"Kenya",
     "KIR_Kiribati":"Kiribati",
   "KO-_Kosova":"Kosova",
     "KWT_Kuwait":"Kuwait",
     "KGZ_Kyrgyzstan":"Kyrgyzstan",
     "LAO_Laos":"Laos",
     "LVA_Latvia":"Latvia",
     "LBN_Lebanon":"Lebanon",
     "LSO_Lesotho":"Lesotho",
     "LBR_Liberia":"Liberia",
     "LBY_Libya":"Libya",
     "LIE_Liechtenstein":"Liechtenstein",
     "LTU_Lithuania":"Lithuania",
     "LUX_Luxembourg":"Luxembourg",
     "MAC_Macao":"Macao",
     "MKD_Macedonia":"Macedonia",
     "MDG_Madagascar":"Madagascar",
     "MWI_Malawi":"Malawi",
     "MYS_Malaysia":"Malaysia",
     "MDV_Maldives":"Maldives",
     "MLI_Mali":"Mali",
     "MLT_Malta":"Malta",
     "MHL_Marshall Islands":"Marshall Islands",
     "MTQ_Martinique":"Martinique",
     "MRT_Mauritania":"Mauritania",
     "MUS_Mauritius":"Mauritius",
     "MYT_Mayotte":"Mayotte",
     "MEX_Mexico":"Mexico",
     "FSM_Micronesia, Federated States of ":"Micronesia, Federated States of ",
     "MDA_Moldova":"Moldova",
     "MCO_Monaco":"Monaco",
     "MNG_Mongolia":"Mongolia",
     "MNE_Montenegro":"Montenegro",
     "MSR_Montserrat":"Montserrat",
     "MAR_Morocco":"Morocco",
     "MOZ_Mozambique":"Mozambique",
     "MMR_Myanmar":"Myanmar",
     "NAM_Namibia":"Namibia",
     "NRU_Nauru":"Nauru",
     "NPL_Nepal":"Nepal",
     "NLD_Netherlands":"Netherlands",
     "ANT_Netherlands Antilles":"Netherlands Antilles",
     "NCL_New Caledonia":"New Caledonia",
     "NZL_New Zealand":"New Zealand",
     "NIC_Nicaragua":"Nicaragua",
     "NER_Niger":"Niger",
     "NGA_Nigeria":"Nigeria",
     "NIU_Niue":"Niue",
     "NFK_Norfolk Island":"Norfolk Island",
     "PRK_North Korea":"North Korea",
     "MNP_Northern Mariana Islands":"Northern Mariana Islands",
     "NOR_Norway":"Norway",
     "OMN_Oman":"Oman",
     "PAK_Pakistan":"Pakistan",
     "PLW_Palau":"Palau",
     "PSE_Palestina":"Palestina",
     "PAN_Panama":"Panama",
     "PNG_Papua New Guinea":"Papua New Guinea",
     "PRY_Paraguay":"Paraguay",
     "PER_Peru":"Peru",
     "PHL_Philippines":"Philippines",
     "PCN_Pitcairn Islands":"Pitcairn Islands",
     "POL_Poland":"Poland",
     "PRT_Portugal":"Portugal",
     "PRI_Puerto Rico":"Puerto Rico",
     "QAT_Qatar":"Qatar",
     "REU_Reunion":"Reunion",
     "ROU_Romania":"Romania",
     "RUS_Russian Federation":"Russian Federation",
     "RWA_Rwanda":"Rwanda",
     "SHN_Saint Helena":"Saint Helena",
     "KNA_Saint Kitts and Nevis":"Saint Kitts and Nevis",
     "SPM_Saint Pierre and Miquelon":"Saint Pierre and Miquelon",
     "VCT_Saint Vincent and the Grenadines":"Saint Vincent and the Grenadines",
     "WSM_Samoa":"Samoa",
     "SMR_San Marino":"San Marino",
     "LCA_Santa Lucia":"Santa Lucia",
     "STP_Sao Tome and Principe":"Sao Tome and Principe",
     "SAU_Saudi Arabia":"Saudi Arabia",
     "SEN_Senegal":"Senegal",
     "SRB_Serbia":"Serbia",
     "SYC_Seychelles":"Seychelles",
     "SLE_Sierra Leone":"Sierra Leone",
     "SGP_Singapore":"Singapore",
     "SVK_Slovakia":"Slovakia",
     "SVN_Slovenia":"Slovenia",
     "SLB_Solomon Islands":"Solomon Islands",
     "SOM_Somalia":"Somalia",
     "ZAF_South Africa":"South Africa",
     "SGS_South Georgia and the South Sandwich Islands":"South Georgia and the South Sandwich Islands",
     "KOR_South Korea":"South Korea",
     "ESP_Spain":"Spain",
     "LKA_Sri Lanka":"Sri Lanka",
     "SDN_Sudan":"Sudan",
     "SUR_Suriname":"Suriname",
     "SJM_Svalbard and Jan Mayen":"Svalbard and Jan Mayen",
     "SWZ_Swaziland":"Swaziland",
     "SWE_Sweden":"Sweden",
     "CHE_Switzerland":"Switzerland",
     "SYR_Syria":"Syria",
     "TWN_Taiwan":"Taiwan",
     "TJK_Tajikistan":"Tajikistan",
     "TZA_Tanzania":"Tanzania",
     "THA_Thailand":"Thailand",
     "TLS_Timor-Leste":"Timor-Leste",
     "TGO_Togo":"Togo",
     "TKL_Tokelau":"Tokelau",
     "TON_Tonga":"Tonga",
     "TTO_Trinidad and Tobago":"Trinidad and Tobago",
     "TUN_Tunisia":"Tunisia",
     "TUR_Turkey":"Turkey",
     "TKM_Turkmenistan":"Turkmenistan",
     "TCA_Turks and Caicos Islands":"Turks and Caicos Islands",
     "TUV_Tuvalu":"Tuvalu",
     "UGA_Uganda":"Uganda",
     "UKR_Ukraine":"Ukraine",
     "ARE_United Arab Emirates":"United Arab Emirates",
     "GBR_United Kingdom":"United Kingdom",
     "USA_United States":"United States",
     "UMI_United States Minor Outlying Island":"United States Minor Outlying Island",
     "URY_Uruguay":"Uruguay",
     "UZB_Uzbekistan":"Uzbekistan",
     "VUT_Vanuatu":"Vanuatu",
     "VAT_Vatican":"Vatican",
     "VEN_Venezuela":"Venezuela",
     "VNM_Vietnam":"Vietnam",
     "VIR_Virgin Islands U.S":"Virgin Islands, U.S",
     "WLF_Wallis and Futuna":"Wallis and Futuna",
     "ESH_Western Sahara":"Western Sahara",
     "YEM_Yemen":"Yemen",
     "ZMB_Zambia":"Zambia",
     "ZWE_Zimbabwe":"Zimbabwe"
}


def find_key(dic, val):
    #return the key of dictionary dic given the value
    return [k for k, v in symbol_dic.iteritems() if v == val][0]

# get the data
countryToCreate = raw_input('Country name? ')
# countryToCreate = countryToCreate.strip()

countryToCreate = countryToCreate[:1].upper() + countryToCreate[1:].lower()
fetchCountry = find_key(symbol_dic, countryToCreate)
fetchCountry = fetchCountry[:3]

url = "http://gadm.org/data/shp/"+fetchCountry+"_adm.zip"

print url

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
toConvert = fetchCountry+'_adm1.shp'
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

subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '7777'])
webbrowser.open_new_tab('localhost:7777')





