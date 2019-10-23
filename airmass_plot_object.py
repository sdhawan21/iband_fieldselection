import numpy as np 
import matplotlib.pyplot as plt 
import glob
import astropy.units as u

from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astroplan import Observer, time_grid_from_range, FixedTarget

#this is the best way to use the 
from astroplan.plots import plot_airmass

hsv = plt.get_cmap('hsv')
times = time_grid_from_range(Time(["2019-10-17 00:00", "2020-03-15 00:00"]), time_resolution=7*u.day)

fid, ra, dec  = np.loadtxt('March_2hr0.83_fracTime_withCoords.txt', unpack=True)
colors = hsv(np.linspace(0, 1.0, len(fid)))

#define the location and elevation of Palomar
#P48 = EarthLocation(lat=33.356*u.deg, lon=-116.863*u.deg, height=1706.0*u.m)
Palomar = Observer.at_site("Palomar")

time = times[0]#Time(["2019-10-16 00:00"])

delta_time = np.linspace(-2, 10, 100)*u.hour
time_array = time + delta_time
print(fid[20:])
#for i, fval in enumerate(fid[40:]):
#print(ra[i], dec[i])
#make plot for the first Wednesday
for i, keyval in enumerate(ra[20:]):
	coords = SkyCoord(ra=keyval*u.deg, dec=dec[i]*u.deg)
	Ftarg = FixedTarget(name=str(fid[i+20]), coord=coords)
	plot_airmass(Ftarg, Palomar, time_array, style_kwargs={'color':colors[i]})

plt.legend(loc=0,prop={'size':6})
plt.savefig('Plots_Airmass/Airmass_ZUDSfields_'+str(time.datetime.year)+'_'+str(time.datetime.month)+'_'+str(time.datetime.day)+'.pdf')
#Ftarg2 = FixedTarget(name='Ftarg2', coord=coords2)

#frame_fval = AltAz(obstime=time + delta_time, location=P48)
#get the altitude for each of the time steps?
#fval_altaz = Palomar.altaz(time + delta_time, Ftarg)#coords.transform_to(frame_fval)
#fval_altaz_zenith = 90. - fval_altaz.alt.value
#fval_airmass_w1 = 1./np.cos(fval_altaz_zenith*np.pi/180.) 
#print(fval_airmass_w1)
#print(fval_airmass_w1, time_array)

##plt.plot([0, 0], [1,3])
#plt.xlabel('Hours from Midnight')
#plt.ylabel('Airmass [Sec(z)]')

#plt.ylim(plt.ylim()[::-1])
plt.show()