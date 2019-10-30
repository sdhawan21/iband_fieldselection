import numpy as np 
import matplotlib.pyplot as plt 

g_suspect = np.loadtxt('suspectrefs_fid1.txt', dtype='str')
r_suspect = np.loadtxt('suspectrefs_fid2.txt', dtype='str')
i_suspect = np.loadtxt('suspectrefs_fid3.txt', dtype='str')

zuds_fid = np.loadtxt('../final_ZUDS_files/DR8_overlap_MostObs_ZUDSFields_withObsVals_RA170.txt')

id_arr_gband = []
def get_badref_fid(g_suspect):
	id_arr_gband=[]
	for i in g_suspect:
		str_ref = i[0].split('/')
		#print(str_ref)
		fid = int(str_ref[5][-3:])
		ccdid = int(str_ref[7][-2:])
		qid = int(str_ref[8][-1])
		print(fid, ccdid, qid)
		id_arr_gband.append([fid, ccdid, qid])
	id_arr_gband = np.array(id_arr_gband)
	fields = np.unique(id_arr_gband[:,0])
	print(fields)
	n_ccd_q = np.array([[fid, len(id_arr_gband[id_arr_gband[:,0] == fid])] for fid in fields])
	
	return id_arr_gband, n_ccd_q

id_arr_gband, n_ccd_g = get_badref_fid(g_suspect)
id_arr_rband, n_ccd_r = get_badref_fid(r_suspect)
id_arr_iband, n_ccd_i = get_badref_fid(i_suspect)
print(n_ccd_g)
zuds_badchan = []
for fid in zuds_fid[:,0]:
    if fid in id_arr_gband[:,0]:
        n_g = n_ccd_g[n_ccd_g[:,0] == fid][0][1]
    else:
        n_g = 0
    if fid in id_arr_rband[:,0]:
        n_r = n_ccd_r[n_ccd_r[:,0] == fid][0][1]
    else:
        n_r = 0
    if fid in id_arr_iband[:,0]:
        n_i = n_ccd_i[n_ccd_i[:,0] == fid][0][1]
    else:
        n_i = 0
    zuds_badchan.append([int(fid), n_g, n_r, n_i])

print(zuds_badchan, np.shape(zuds_badchan))
np.savetxt("badref_channels_ZUDSfields.txt", zuds_badchan)