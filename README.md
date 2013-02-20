d3MapMaker
==========

An automated SVG map maker built with Python and d3.js

# Instructions
You need to install  the <a href="http://www.gdal.org/" target="_blank">(GDLA) Geo spatial Data Abstraction Library</a>. Mac users download from <a href="http://www.kyngchaos.com/software/frameworks" target="_blank">this link</a>

Once you have downloaded GDAL install the complete package.

Create a repo for this map 

<pre>
  <code>
    mkdir myMap
  </code>
</pre>

Cd to that repo

<pre>
  <code>
    cd myMap
  </code>
</pre>

Run the python script

<pre>
  <code>
    ./fetch.py
  </code>
</pre>

You will then be prompted to enter the name of the country that you want a map of. Type it in, hit enter and that should be it.

This will create the geoJSON object that the index.html file is expecting in order to render a map.

Once the geoJSON file is there the script will launch a localhost on port 7777 opening up the index file with your country.

Currently supports python verstion 2.7.2

## Supported countries
<ul name="cnt"> 
    <li value="AFG_Afghanistan">Afghanistan</li> 
    <li value="ALA_Åland Islands">Aland Islands</li> 
    <li value="ALB_Albania">Albania</li> 
    <li value="DZA_Algeria">Algeria</li> 
    <li value="ASM_American Samoa">American Samoa</li> 
    <li value="AND_Andorra">Andorra</li> 
    <li value="AGO_Angola">Angola</li> 
    <li value="AIA_Anguilla Island">Anguilla Island</li> 
    <li value="ATA_Antarctica">Antarctica</li> 
    <li value="ATG_Antigua and Barbuda">Antigua and Barbuda</li> 
    <li value="ARG_Argentina">Argentina</li> 
    <li value="ARM_Armenia">Armenia</li> 
    <li value="ABW_Aruba">Aruba</li> 
    <li value="AUS_Australia">Australia</li> 
    <li value="AUT_Austria">Austria</li> 
    <li value="AZE_Azerbaijan">Azerbaijan</li> 
    <li value="BHS_Bahamas">Bahamas</li> 
    <li value="BHR_Bahrain">Bahrain</li> 
    <li value="BGD_Bangladesh">Bangladesh</li> 
    <li value="BRB_Barbados">Barbados</li> 
    <li value="BLR_Belarus">Belarus</li> 
    <li value="BEL_Belgium">Belgium</li> 
    <li value="BLZ_Belize">Belize</li> 
    <li value="BEN_Benin">Benin</li> 
    <li value="BMU_Bermuda">Bermuda</li> 
    <li value="BTN_Bhutan">Bhutan</li> 
    <li value="BOL_Bolivia">Bolivia</li> 
    <li value="BIH_Bosnia and Herzegovina">Bosnia and Herzegovina</li> 
    <li value="BWA_Botswana">Botswana</li> 
    <li value="BVT_Bouvet Island">Bouvet Island</li> 
    <li value="BRA_Brazil">Brazil</li> 
    <li value="IOT_British Indian Ocean Territory">British Indian Ocean Territory</li> 
    <li value="VGB_British Virgin Islands">British Virgin Islands</li> 
    <li value="BRN_Brunei Darussalam">Brunei Darussalam</li> 
    <li value="BGR_Bulgaria">Bulgaria</li> 
    <li value="BFA_Burkina Faso">Burkina Faso</li> 
    <li value="BDI_Burundi">Burundi</li> 
    <li value="KHM_Cambodia">Cambodia</li> 
    <li value="CMR_Cameroon">Cameroon</li> 
    <li value="CAN_Canada">Canada</li> 
    <li value="CPV_Cape Verde">Cape Verde</li> 
    <li value="CYM_Cayman Islands">Cayman Islands</li> 
    <li value="CAF_Central African Republic">Central African Republic</li> 
    <li value="TCD_Chad">Chad</li> 
    <li value="CHL_Chile">Chile</li> 
    <li value="CHN_China">China</li> 
    <li value="CXR_Christmas Island">Christmas Island</li> 
    <li value="CCK_Cocos Islands">Cocos Islands</li> 
    <li value="COL_Colombia">Colombia</li> 
    <li value="COM_Comoros">Comoros</li> 
    <li value="COG_Congo, Republic of">Congo Republic of</li> 
    <li value="COD_Congo, The Democratic Republic of the">Congo The Democratic Republic of the</li> 
    <li value="COK_Cook Islands">Cook Islands</li> 
    <li value="CRI_Costa Rica">Costa Rica</li> 
    <li value="CIV_Côte d'Ivoire">Cote d'Ivoire</li> 
    <li value="HRV_Croatia">Croatia</li> 
    <li value="CUB_Cuba">Cuba</li> 
    <li value="CYP_Cyprus">Cyprus</li> 
    <li value="CZE_Czech Republic">Czech Republic</li> 
    <li value="DNK_Denmark">Denmark</li> 
    <li value="DJI_Djibouti">Djibouti</li> 
    <li value="DMA_Dominica">Dominica</li> 
    <li value="DOM_Dominican Republic">Dominican Republic</li> 
    <li value="ECU_Ecuador">Ecuador</li> 
    <li value="EGY_Egypt">Egypt</li> 
    <li value="SLV_El Salvador">El Salvador</li> 
    <li value="GNQ_Equatorial Guinea">Equatorial Guinea</li> 
    <li value="ERI_Eritrea">Eritrea</li> 
    <li value="EST_Estonia">Estonia</li> 
    <li value="ETH_Ethiopia">Ethiopia</li> 
    <li value="FLK_Falkland Islands">Falkland Islands</li> 
    <li value="FRO_Faroe Islands">Faroe Islands</li> 
    <li value="FJI_Fiji">Fiji</li> 
    <li value="FIN_Finland">Finland</li> 
    <li value="FRA_France">France</li> 
    <li value="GUF_French Guiana">French Guiana</li> 
    <li value="PYF_French Polynesia">French Polynesia</li> 
    <li value="ATF_French Southern Territories">French Southern Territories</li> 
    <li value="GAB_Gabon">Gabon</li> 
    <li value="GMB_Gambia">Gambia</li> 
    <li value="GEO_Georgia">Georgia</li> 
    <li value="DEU_Germany">Germany</li> 
    <li value="GHA_Ghana">Ghana</li> 
    <li value="GIB_Gibraltar">Gibraltar</li> 
    <li value="GRC_Greece">Greece</li> 
    <li value="GRL_Greenland">Greenland</li> 
    <li value="GRD_Grenada">Grenada</li> 
    <li value="GLP_Guadeloupe">Guadeloupe</li> 
    <li value="GUM_Guam">Guam</li> 
    <li value="GTM_Guatemala">Guatemala</li> 
    <li value="GGY_Guernsey">Guernsey</li> 
    <li value="GIN_Guinea">Guinea</li> 
    <li value="GNB_Guinea-Bissau">Guinea-Bissau</li> 
    <li value="GUY_Guyana">Guyana</li> 
    <li value="HTI_Haiti">Haiti</li> 
    <li value="HMD_Heard Island and McDonald Islands">Heard Island and McDonald Islands</li> 
    <li value="HND_Honduras">Honduras</li> 
    <li value="HKG_Hongkong">Hongkong</li> 
    <li value="HUN_Hungary">Hungary</li> 
    <li value="ISL_Iceland">Iceland</li> 
    <li value="IND_India">India</li> 
    <li value="IDN_Indonesia">Indonesia</li> 
    <li value="IRN_Iran">Iran</li> 
    <li value="IRQ_Iraq">Iraq</li> 
    <li value="IRL_Ireland">Ireland</li> 
    <li value="IMN_Isle of Man">Isle of Man</li> 
    <li value="ISR_Israel">Israel</li> 
    <li value="ITA_Italy">Italy</li> 
    <li value="JAM_Jamaica">Jamaica</li> 
    <li value="JEY_Jersey">Jersey</li> 
    <li value="JPN_Japan">Japan</li> 
    <li value="JOR_Jordan">Jordan</li> 
    <li value="KAZ_Kazakhstan">Kazakhstan</li> 
    <li value="KEN_Kenya">Kenya</li> 
    <li value="KIR_Kiribati">Kiribati</li> 
  <li value="KO-_Kosova">Kosova</li> 
    <li value="KWT_Kuwait">Kuwait</li> 
    <li value="KGZ_Kyrgyzstan">Kyrgyzstan</li> 
    <li value="LAO_Laos">Laos</li> 
    <li value="LVA_Latvia">Latvia</li> 
    <li value="LBN_Lebanon">Lebanon</li> 
    <li value="LSO_Lesotho">Lesotho</li> 
    <li value="LBR_Liberia">Liberia</li> 
    <li value="LBY_Libya">Libya</li> 
    <li value="LIE_Liechtenstein">Liechtenstein</li> 
    <li value="LTU_Lithuania">Lithuania</li> 
    <li value="LUX_Luxembourg">Luxembourg</li> 
    <li value="MAC_Macao">Macao</li> 
    <li value="MKD_Macedonia">Macedonia</li> 
    <li value="MDG_Madagascar">Madagascar</li> 
    <li value="MWI_Malawi">Malawi</li> 
    <li value="MYS_Malaysia">Malaysia</li> 
    <li value="MDV_Maldives">Maldives</li> 
    <li value="MLI_Mali">Mali</li> 
    <li value="MLT_Malta">Malta</li> 
    <li value="MHL_Marshall Islands">Marshall Islands</li> 
    <li value="MTQ_Martinique">Martinique</li> 
    <li value="MRT_Mauritania">Mauritania</li> 
    <li value="MUS_Mauritius">Mauritius</li> 
    <li value="MYT_Mayotte">Mayotte</li> 
    <li value="MEX_Mexico">Mexico</li> 
    <li value="FSM_Micronesia, Federated States of ">Micronesia Federated States of </li> 
    <li value="MDA_Moldova">Moldova</li> 
    <li value="MCO_Monaco">Monaco</li> 
    <li value="MNG_Mongolia">Mongolia</li> 
    <li value="MNE_Montenegro">Montenegro</li> 
    <li value="MSR_Montserrat">Montserrat</li> 
    <li value="MAR_Morocco">Morocco</li> 
    <li value="MOZ_Mozambique">Mozambique</li> 
    <li value="MMR_Myanmar">Myanmar</li> 
    <li value="NAM_Namibia">Namibia</li> 
    <li value="NRU_Nauru">Nauru</li> 
    <li value="NPL_Nepal">Nepal</li> 
    <li value="NLD_Netherlands">Netherlands</li> 
    <li value="ANT_Netherlands Antilles">Netherlands Antilles</li> 
    <li value="NCL_New Caledonia">New Caledonia</li> 
    <li value="NZL_New Zealand">New Zealand</li> 
    <li value="NIC_Nicaragua">Nicaragua</li> 
    <li value="NER_Niger">Niger</li> 
    <li value="NGA_Nigeria">Nigeria</li> 
    <li value="NIU_Niue">Niue</li> 
    <li value="NFK_Norfolk Island">Norfolk Island</li> 
    <li value="PRK_North Korea">North Korea</li> 
    <li value="MNP_Northern Mariana Islands">Northern Mariana Islands</li> 
    <li value="NOR_Norway">Norway</li> 
    <li value="OMN_Oman">Oman</li> 
    <li value="PAK_Pakistan">Pakistan</li> 
    <li value="PLW_Palau">Palau</li> 
    <li value="PSE_Palestina">Palestina</li> 
    <li value="PAN_Panama">Panama</li> 
    <li value="PNG_Papua New Guinea">Papua New Guinea</li> 
    <li value="PRY_Paraguay">Paraguay</li> 
    <li value="PER_Peru">Peru</li> 
    <li value="PHL_Philippines">Philippines</li> 
    <li value="PCN_Pitcairn Islands">Pitcairn Islands</li> 
    <li value="POL_Poland">Poland</li> 
    <li value="PRT_Portugal">Portugal</li> 
    <li value="PRI_Puerto Rico">Puerto Rico</li> 
    <li value="QAT_Qatar">Qatar</li> 
    <li value="REU_Reunion">Reunion</li> 
    <li value="ROU_Romania">Romania</li> 
    <li value="RUS_Russian Federation">Russian Federation</li> 
    <li value="RWA_Rwanda">Rwanda</li> 
    <li value="SHN_Saint Helena">Saint Helena</li> 
    <li value="KNA_Saint Kitts and Nevis">Saint Kitts and Nevis</li> 
    <li value="SPM_Saint Pierre and Miquelon">Saint Pierre and Miquelon</li> 
    <li value="VCT_Saint Vincent and the Grenadines">Saint Vincent and the Grenadines</li> 
    <li value="WSM_Samoa">Samoa</li> 
    <li value="SMR_San Marino">San Marino</li> 
    <li value="LCA_Santa Lucia">Santa Lucia</li> 
    <li value="STP_Sao Tome and Principe">Sao Tome and Principe</li> 
    <li value="SAU_Saudi Arabia">Saudi Arabia</li> 
    <li value="SEN_Senegal">Senegal</li> 
    <li value="SRB_Serbia">Serbia</li> 
    <li value="SYC_Seychelles">Seychelles</li> 
    <li value="SLE_Sierra Leone">Sierra Leone</li> 
    <li value="SGP_Singapore">Singapore</li> 
    <li value="SVK_Slovakia">Slovakia</li> 
    <li value="SVN_Slovenia">Slovenia</li> 
    <li value="SLB_Solomon Islands">Solomon Islands</li> 
    <li value="SOM_Somalia">Somalia</li> 
    <li value="ZAF_South Africa">South Africa</li> 
    <li value="SGS_South Georgia and the South Sandwich Islands">South Georgia and the South Sandwich Islands</li> 
    <li value="KOR_South Korea">South Korea</li> 
    <li value="ESP_Spain">Spain</li> 
    <li value="LKA_Sri Lanka">Sri Lanka</li> 
    <li value="SDN_Sudan">Sudan</li> 
    <li value="SUR_Suriname">Suriname</li> 
    <li value="SJM_Svalbard and Jan Mayen">Svalbard and Jan Mayen</li> 
    <li value="SWZ_Swaziland">Swaziland</li> 
    <li value="SWE_Sweden">Sweden</li> 
    <li value="CHE_Switzerland">Switzerland</li> 
    <li value="SYR_Syria">Syria</li> 
    <li value="TWN_Taiwan">Taiwan</li> 
    <li value="TJK_Tajikistan">Tajikistan</li> 
    <li value="TZA_Tanzania">Tanzania</li> 
    <li value="THA_Thailand">Thailand</li> 
    <li value="TLS_Timor-Leste">Timor-Leste</li> 
    <li value="TGO_Togo">Togo</li> 
    <li value="TKL_Tokelau">Tokelau</li> 
    <li value="TON_Tonga">Tonga</li> 
    <li value="TTO_Trinidad and Tobago">Trinidad and Tobago</li> 
    <li value="TUN_Tunisia">Tunisia</li> 
    <li value="TUR_Turkey">Turkey</li> 
    <li value="TKM_Turkmenistan">Turkmenistan</li> 
    <li value="TCA_Turks and Caicos Islands">Turks and Caicos Islands</li> 
    <li value="TUV_Tuvalu">Tuvalu</li> 
    <li value="UGA_Uganda">Uganda</li> 
    <li value="UKR_Ukraine">Ukraine</li> 
    <li value="ARE_United Arab Emirates">United Arab Emirates</li> 
    <li value="GBR_United Kingdom">United Kingdom</li> 
    <li value="USA_United States">United States</li> 
    <li value="UMI_United States Minor Outlying Island">United States Minor Outlying Island</li> 
    <li value="URY_Uruguay">Uruguay</li> 
    <li value="UZB_Uzbekistan">Uzbekistan</li> 
    <li value="VUT_Vanuatu">Vanuatu</li> 
    <li value="VAT_Vatican">Vatican</li> 
    <li value="VEN_Venezuela">Venezuela</li> 
    <li value="VNM_Vietnam">Vietnam</li> 
    <li value="VIR_Virgin Islands, U.S">Virgin Islands U.S</li> 
    <li value="WLF_Wallis and Futuna">Wallis and Futuna</li> 
    <li value="ESH_Western Sahara">Western Sahara</li> 
    <li value="YEM_Yemen">Yemen</li> 
    <li value="ZMB_Zambia">Zambia</li> 
    <li value="ZWE_Zimbabwe">Zimbabwe</li> 
  </ul>

## Todos
<ol>
  <li>Make the dictionary of countries more robust to handle special characters, partial type ins etc.</li>
  <li>If the user types in an error make sure to catch it</li>
  <li>Some countries do not have regions only the country outlyer, add the option to fetch all availble shp files for a given country</li>
</ol>

## Credit
I want to thank <a href="http://stackoverflow.com/users/2032478/jan-van-der-laan" taget="_blank">Jan van der Laan</a> and <a href="http://bost.ocks.org/mike/" taget="_blank">Mike Bostock</a> for their full and comprehensive responses to my stack overflow <a href="http://stackoverflow.com/questions/14492284/center-a-map-in-d3-given-a-geojson-object" taget="_blank">questions</a>. With out their answers I would have never figured the centering of the map and the scaling of it on my own... believe me I tried.



  
