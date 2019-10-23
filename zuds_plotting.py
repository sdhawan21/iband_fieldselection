import numpy as np 
import matplotlib.pyplot as plt 

from ztfquery import query
from astropy import time

zquery = query.ZTFquery()
jd_15oct2019 = time.Time("2019-10-15").jd # 2458239.5
jd_22oct2019 = time.Time("2019-10-22").jd
zquery.load_metadata(sql_query="seeing<2 and obsjd BETWEEN 2458771.5 AND 2458778.5")
zquery.show_gri_fields(title="Oct152019 < time < Oct222019 \n seeing<2", grid="main")

#mollweide figure of fields per week 


AAM_obs = np.loadtxt('AllObservability_MarchZUDS.txt')
#plt.plot(AAM_obs[265]*24, label='264')
frac_vis2hr = len(AAM_obs[265][AAM_obs[265]*24 > 2])/len(AAM_obs[265])
print(frac_vis2hr)
#plt.show()