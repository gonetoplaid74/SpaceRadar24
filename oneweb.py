from skyfield.api import load, wgs84, load_file

import json
import os, shutil
stations_url = 'http://celestrak.com/NORAD/elements/oneweb.txt'
satellites = load.tle_file(stations_url)



by_name = {sat.name: sat for sat in satellites}

f = open( 'onewebapi.txt', 'w' )
f.write( '[')
f.close()

for i in by_name:
    number = str(i)
    satellite = by_name[number]


    ts = load.timescale()



    t = ts.now()


    geocentric = satellite.at(t)
    lat, lon = wgs84.latlon_of(geocentric)
    height = wgs84.height_of(geocentric)
             
    latitude = str(lat)
    longitude = str(lon)

    alt = str(height)                
    z = alt.split('e')     
    zz = z[0]
    alti = float(zz) * 149.597871
    altitude = round(alti,2)     


    x = latitude.split('deg')
    xx = ''.join(x)
    xxx = xx.split('\'')
    xxxx = ''.join(xxx)
    xxxxx  = xxxx.split('\"')
    xxxxxx = ''.join(xxxxx)
    xxxxxxx= xxxxxx.split()
    xxxxxxxx = ''.join(xxxxxxx)
    deglat = float(xxxxxxxx)/10000


    yy = longitude.split('deg')
    yyy = ''.join(yy)
    yya = yyy.split('\'')
    yyb = ''.join(yya)
    yyc  = yyb.split('\"')
    yyd = ''.join(yyc)
    yye= yyd.split()
    yyf = ''.join(yye)
    deglon = float(yyf)/10000
                


    f = open( 'onewebapi.txt', 'a' )
    f.write( '{"latitude":' + str(deglat) + ',"longitude":' + str(deglon) + ',"altitude":' + str(altitude) + '},')
    f.close()

with open('onewebapi.txt', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()
f = open( 'onewebapi.txt', 'a' )
f.write(']')
f.close()
print("done")
shutil.copy('onewebapi.txt', './html/onewebapi.txt')