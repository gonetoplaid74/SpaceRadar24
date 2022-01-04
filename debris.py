from skyfield.api import load, wgs84
import json



n = 49706
url = 'https://www.space-track.org/basicspacedata/query/class/gp/NORAD_CAT_ID/49706/format/tle/emptyresult/show'
filename = '49706.txt'.format(n)
satellite = load.tle_file(url)


ts = load.timescale()


y = 2021
mo = 11
d = 4
h = 0
m = 0
s = 0
while d < 5:
    h = 0
    while h < 12:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                t = ts.utc(y,mo,d,h,m,s)
                time =t.utc_iso()
            
                import dateutil.parser as dp
                tm = time
                tm1 = parsed_t = dp.parse(tm)
                t_in_seconds = parsed_t.timestamp()
                

                
                
                geocentric = satellite.at(t)


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
                


                f = open( 'debris1.txt', 'a' )
                f.write( '{"latitude":'+ str(deglat) + ',"longitude":' + str(deglon) + ',"timestamp":' + str(t_in_seconds) + '},')
                f.close()
                s += 1
            m +=1
        h+=1
    d += 1