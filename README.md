d3MapMaker
==========

An automated d3 map maker. 
Input the 3 character country code of the country you want. Example: AFG for Afghanistan, (this will improve in next updates) and you will get an index.html file with your map in SVG using D3 and scaled to 900.


# Instructions
You need to install  the <a href="http://www.gdal.org/" target="_blank">(GDLA) Geo spatial Data Abstraction Library</a>. Mac users download from <a href="http://www.kyngchaos.com/software/frameworks" target="_blank">this link</a>

Once you have downloaded GDAL install it.

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

This will create what you need an launch a localhost:7777. Go that that URL and you should see your map.

## Todos
<ol>
  <li>Create the dictionary with country names and their corresponding abbreviations for diva to fetch the data</li>
  <li>Include js code to center the map projection and scale it to something bigger than 900</li>
</ol>


  