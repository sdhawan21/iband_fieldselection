import numpy as np 
import matplotlib.pyplot as plt 
import corner

from astropy.io import ascii 

from astropy.table import Table
from matplotlib import gridspec

#field IDs from astroplan for the airmass/lunation constraints
field_IDs = np.loadtxt('FieldLists/NovMarch_fieldList_2hr0.83fracTime.txt') 
target_table = Table.read('fields.txt', format='ascii')
tar_tab = target_table[['%ID', 'RA', 'Dec']]
field_withCoords = []
iband_ref = ascii.read('ztf_i_band_coverage.csv', format='csv')
All_obs = np.loadtxt('AllObservability_MarchZUDS.txt')

for val in tar_tab:
	if val[0] in field_IDs:
		rcid = iband_ref[iband_ref['field'] == val[0]]['rcid'][0]
		field_withCoords.append([val[0], val[1], val[2], rcid])
field_withCoords = np.array(field_withCoords)
print(field_withCoords)
good_ref_fields = field_withCoords[field_withCoords[:,-1] >= 50]
print(len(good_ref_fields))

#make the first figure on the RA/Dec of the field centers as a gradient with the 
#hours observable 
fig1 = plt.figure(1)

obs_arr = [np.sum(All_obs[int(i)+1])*24./152. for i in field_IDs]
print(field_withCoords[:,1], field_withCoords[:,2])
plt.plot(field_withCoords[:,1], field_withCoords[:,2], 'gs')
#plt.scatter(field_withCoords[:,1], field_withCoords[:,2], c=obs_arr)
plt.gray()
plt.ylabel('Dec (deg)', fontsize=15)
plt.xlabel('RA (deg)', fontsize=15)
plt.savefig('Nov_fieldCoords_ZUDS1.pdf')

gs = gridspec.GridSpec(11, 4)
nday_month = [31, 30, 31, 31, 29]
print(np.sum(nday_month))
plt.show()
counter = 0

fig2 = plt.figure(2, figsize=(15,12))

for kval in range(11):
    for rval in range(4):
        ax = plt.subplot(gs[kval, rval])
        fid = field_IDs[counter]
        obs_val = All_obs[int(fid)+1]
        #if int(fid) in n_iband_exp[:,0]:
        #    n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        #else:
        #    n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+', '+str(field_withCoords[counter][1])+', '+str(field_withCoords[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
    	if rval == 0:
        	ax.set_ylabel('Hours Vis')
    if kval > 9:
    	ax.set_xlabel('Days since 15-10-2019')
    

#plt.savefig('fieldVis_AllSurvey_ZUDS1.pdf')

