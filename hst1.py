from skyfield.api import load, wgs84
import json
stations_url = 'http://celestrak.com/NORAD/elements/science.txt'
satellites = load.tle_file(stations_url)


by_name = {sat.name: sat for sat in satellites}
satellite = by_name['HST']


n = 20580
url = 'https://celestrak.com/satcat/tle.php?CATNR={}'.format(n)
filename = 'tle-CATNR-{}.txt'.format(n)
satellites = load.tle_file(url, filename=filename)

print(satellite.epoch.utc_jpl())
ts = load.timescale()



t = ts.now()
                
                
geocentric = satellite.at(t)
print(geocentric)

lat, lon = wgs84.latlon_of(geocentric)
                
latitude = str(lat)
longitude = str(lon)
                
            
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
                
print(deglat)
print(deglon)
print(n)


f = open('./public/hst.txt', 'w')
f.write('[{"name":' + str(n) + ',"latitude":'+ str(deglat) + ',"longitude":' + str(deglon) + '}]')
f.close()
   