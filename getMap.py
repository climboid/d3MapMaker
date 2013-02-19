import json
import urllib.request, urllib.parse, urllib.error
import os
import zipfile

def getUserInput(type, selFrom, default):
    clear = '_' * 45
    cont = True
    output = ''
    while cont:
        raw = input("Enter " + type + "; leave blank for default (" + default + "); enter ls -a to list: \n").title()
        if (raw.lower() == "ls -a"):
            for key in selFrom:
                print('\t' + key)
        else:
            if (raw == ""):
                raw = default
            if (raw in selFrom):
                print("--> returned code: " + selFrom[raw] + " from: " + raw)
                print(clear + "\n")
                output = selFrom[raw]
                cont = False
            else:
                print('Couldn\'t find ' + raw+ ', Perhaps you meant one of these: ')
                count = 0
                for key in selFrom:
                    if (key[:1] == raw[:1]):
                        count += 1
                        print('\t' + key)
                if (count == 0):
                    print('No matches found :(')
                print(clear + "\n")
    return output

def downloadFile(selCountry, selMapType):
    root = 'http://www.diva-gis.org/data/'
    mapDir = selMapType + '/'
    if (selMapType == 'adm'):
        root = 'http://gadm.org/data/'
        mapDir = 'shp/'
    url = root + mapDir + selCountry + '_' + selMapType + '.zip'
    print("downloading " + url + " with urllib")
    path = selCountry + "_" + selMapType
    if not(os.path.isdir(path)):
        os.makedirs(path)
    urllib.request.urlretrieve(url, path + "/code.zip")
    return unzipFile(path, "/code.zip")

def unzipFile(path, inputfile):
    shpFiles = []
    zf = zipfile.ZipFile(path + inputfile)
    for interiorFile in zf.namelist():
        if (interiorFile.endswith('.shp')):
            try:
                data = zf.read(interiorFile)
            except KeyError:
                print('ERROR: Did not find in zip file' % interiorFile)
            else:
                newfile = path + '/' + interiorFile
                print('Unzipping shapefile: ' + newfile)
                output = open(newfile, 'wb')
                output.write(data)
                output.close()
                shpFiles.append(newfile)
            print
    return shpFiles

def convertToGeojson(filesToUpload):
    url = 'http://ogre.adc4gis.com/convert'
    values = {'upload' : open(filesToUpload[0], 'rb')}
   # r = requests.post(url,files = values)
   # print(r.text)

def main():
    countryCodes = {"Afghanistan":"AFG","Åland Islands":"ALA","Albania":"ALB","Algeria":"DZA","American Samoa":"ASM","Andorra":"AND","Angola":"AGO","Anguilla Island":"AIA","Antarctica":"ATA","Antigua and Barbuda":"ATG","Argentina":"ARG","Armenia":"ARM","Aruba":"ABW","Australia":"AUS","Austria":"AUT","Azerbaijan":"AZE","Bahamas":"BHS","Bahrain":"BHR","Bangladesh":"BGD","Barbados":"BRB","Belarus":"BLR","Belgium":"BEL","Belize":"BLZ","Benin":"BEN","Bermuda":"BMU","Bhutan":"BTN","Bolivia":"BOL","Bosnia and Herzegovina":"BIH","Botswana":"BWA","Bouvet Island":"BVT","Brazil":"BRA","British Indian Ocean Territory":"IOT","British Virgin Islands":"VGB","Brunei Darussalam":"BRN","Bulgaria":"BGR","Burkina Faso":"BFA","Burundi":"BDI","Cambodia":"KHM","Cameroon":"CMR","Canada":"CAN","Cape Verde":"CPV","Cayman Islands":"CYM","Central African Republic":"CAF","Chad":"TCD","Chile":"CHL","China":"CHN","Christmas Island":"CXR","Cocos Islands":"CCK","Colombia":"COL","Comoros":"COM","Republic of Congo":"COG","The Democratic Republic of the Congo":"COD","Cook Islands":"COK","Costa Rica":"CRI","Côte d'Ivoire":"CIV","Croatia":"HRV","Cuba":"CUB","Cyprus":"CYP","Czech Republic":"CZE","Denmark":"DNK","Djibouti":"DJI","Dominica":"DMA","Dominican Republic":"DOM","Ecuador":"ECU","Egypt":"EGY","El Salvador":"SLV","Equatorial Guinea":"GNQ","Eritrea":"ERI","Estonia":"EST","Ethiopia":"ETH","Falkland Islands":"FLK","Faroe Islands":"FRO","Fiji":"FJI","Finland":"FIN","France":"FRA","French Guiana":"GUF","French Polynesia":"PYF","French Southern Territories":"ATF","Gabon":"GAB","Gambia":"GMB","Georgia":"GEO","Germany":"DEU","Ghana":"GHA","Gibraltar":"GIB","Greece":"GRC","Greenland":"GRL","Grenada":"GRD","Guadeloupe":"GLP","Guam":"GUM","Guatemala":"GTM","Guernsey":"GGY","Guinea":"GIN","Guinea-Bissau":"GNB","Guyana":"GUY","Haiti":"HTI","Heard Island and McDonald Islands":"HMD","Honduras":"HND","Hongkong":"HKG","Hungary":"HUN","Iceland":"ISL","India":"IND","Indonesia":"IDN","Iran":"IRN","Iraq":"IRQ","Ireland":"IRL","Isle of Man":"IMN","Israel":"ISR","Italy":"ITA","Jamaica":"JAM","Jersey":"JEY","Japan":"JPN","Jordan":"JOR","Kazakhstan":"KAZ","Kenya":"KEN","Kiribati":"KIR","Kosova":"KO-","Kuwait":"KWT","Kyrgyzstan":"KGZ","Laos":"LAO","Latvia":"LVA","Lebanon":"LBN","Lesotho":"LSO","Liberia":"LBR","Libya":"LBY","Liechtenstein":"LIE","Lithuania":"LTU","Luxembourg":"LUX","Macao":"MAC","Macedonia":"MKD","Madagascar":"MDG","Malawi":"MWI","Malaysia":"MYS","Maldives":"MDV","Mali":"MLI","Malta":"MLT","Marshall Islands":"MHL","Martinique":"MTQ","Mauritania":"MRT","Mauritius":"MUS","Mayotte":"MYT","Mexico":"MEX","Federated States of Micronesia":"FSM","Moldova":"MDA","Monaco":"MCO","Mongolia":"MNG","Montenegro":"MNE","Montserrat":"MSR","Morocco":"MAR","Mozambique":"MOZ","Myanmar":"MMR","Namibia":"NAM","Nauru":"NRU","Nepal":"NPL","Netherlands":"NLD","Netherlands Antilles":"ANT","New Caledonia":"NCL","New Zealand":"NZL","Nicaragua":"NIC","Niger":"NER","Nigeria":"NGA","Niue":"NIU","Norfolk Island":"NFK","North Korea":"PRK","Northern Mariana Islands":"MNP","Norway":"NOR","Oman":"OMN","Pakistan":"PAK","Palau":"PLW","Palestina":"PSE","Panama":"PAN","Papua New Guinea":"PNG","Paraguay":"PRY","Peru":"PER","Philippines":"PHL","Pitcairn Islands":"PCN","Poland":"POL","Portugal":"PRT","Puerto Rico":"PRI","Qatar":"QAT","Reunion":"REU","Romania":"ROU","Russian Federation":"RUS","Rwanda":"RWA","Saint Helena":"SHN","Saint Kitts and Nevis":"KNA","Saint Pierre and Miquelon":"SPM","Saint Vincent and the Grenadines":"VCT","Samoa":"WSM","San Marino":"SMR","Santa Lucia":"LCA","Sao Tome and Principe":"STP","Saudi Arabia":"SAU","Senegal":"SEN","Serbia":"SRB","Seychelles":"SYC","Sierra Leone":"SLE","Singapore":"SGP","Slovakia":"SVK","Slovenia":"SVN","Solomon Islands":"SLB","Somalia":"SOM","South Africa":"ZAF","South Georgia and the South Sandwich Islands":"SGS","South Korea":"KOR","Spain":"ESP","Sri Lanka":"LKA","Sudan":"SDN","Suriname":"SUR","Svalbard and Jan Mayen":"SJM","Swaziland":"SWZ","Sweden":"SWE","Switzerland":"CHE","Syria":"SYR","Taiwan":"TWN","Tajikistan":"TJK","Tanzania":"TZA","Thailand":"THA","Timor-Leste":"TLS","Togo":"TGO","Tokelau":"TKL","Tonga":"TON","Trinidad and Tobago":"TTO","Tunisia":"TUN","Turkey":"TUR","Turkmenistan":"TKM","Turks and Caicos Islands":"TCA","Tuvalu":"TUV","Uganda":"UGA","Ukraine":"UKR","United Arab Emirates":"ARE","United Kingdom":"GBR","United States":"USA","United States Minor Outlying Island":"UMI","Uruguay":"URY","Uzbekistan":"UZB","Vanuatu":"VUT","Vatican":"VAT","Venezuela":"VEN","Vietnam":"VNM","U.S. Virgin Islands":"VIR","Wallis and Futuna":"WLF","Western Sahara":"ESH","Yemen":"YEM","Zambia":"ZMB","Zimbabwe":"ZWE"}
    selCountry = str(getUserInput('Country Name', countryCodes, "United States"))

    mapTypeCodes = {"Administrative areas":"adm","Inland water":"wat","Roads":"rds","Railroads":"rrd","Elevation":"alt","Elevation":"msk_alt","Land cover":"cov","Land cover":"msk_cov","Population":"pop","Population":"msk_pop","Gazetteer":"gaz"}
    selMapType = str(getUserInput('Map Type', mapTypeCodes, "Administrative areas"))

    shpfiles = downloadFile(selCountry, selMapType)
    #convertToGeojson(shpfiles)


if __name__ == "__main__":
    main()