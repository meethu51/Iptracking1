import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")

res = gip.record_by_addr('218.212.33.56')

for key, val in res.items():
    print('%s : %s'%(key,val))