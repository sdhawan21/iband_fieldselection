# coding: utf-8
from matplotlib import gridspec
gs = gridspec.GridSpec(8, 6)
aam = loadtxt('AllObservability.txt')
aam
field_index = loadtxt('FieldLists/Feb_fieldList_2hr0.87fracTime.txt')
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            
cla()
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            obs_val = aam[i] * 24.
            
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            obs_val = aam[i] * 24
            
            
aam
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            obs_val = aam[int(i)] * 24
            
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            obs_val = aam[int(i)] * 24
            
for i in field_index:
    for kval in range(8):
        for rval in range(6):
            ax = subplot(gs[kval, rval])
            obs_val = aam[int(i)] * 24
            ax.plot(obs_val, label=str(i))
            
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[fid]
        ax.plot(obs_val*24., label=str(fid))
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        
cla()
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        
counter=0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        
counter=0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        ax.legend(loc=0)
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(fid))
        counter+= 1
        ax.legend(loc=0)
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        counter+= 1
        ax.legend(loc=0)
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        counter+= 1
        ax.legend(loc=0)
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        ax.plot([0, 150],[2,2]) 
        ax.xlim(0, 145)
        counter+= 1
        ax.legend(loc=0)
        
        
cla()
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        ax.plot([0, 150],[2,2]) 
        ax.xlim(0, 145)
        counter+= 1
        ax.legend(loc=0)
        
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        ax.plot([0, 150],[2,2]) 
        ax.xlim(0, 145)
        counter+= 1
        ax.legend(loc=0)
        
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        ax.plot(obs_val*24., label=str(int(fid)))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=0)
        
        
get_ipython().run_line_magic('ls', '')
field_index = loadtxt('FieldLists/Feb_fieldList_2hr0.87fracTime.txt')
n_iband_exp = np.loadtxt('out.dat', delimiter='|', skiprows=2)
n_iband_exp[:,0] = n_iband_exp[:,0].astype('int')
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
    if kval > 6:
        ax.set_xlabel('Days since 15-10-2019')
    if rval == 0:
        ax.set_ylabel('Hours Vis')
        
        
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
    if kval > 6:
        ax.set_xlabel('Days since 15-10-2019')
    if rval == 0:
        ax.set_ylabel('Hours Vis')
        
        
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
    if kval > 6:
        ax.set_xlabel('Days since 15-10-2019')
    if rval == 0:
        ax.set_ylabel('Hours Vis')
        
        
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
    if kval > 6:
        ax.set_xlabel('Days since 15-10-2019')
    if rval == 0:
        ax.set_ylabel('Hours Vis')
        
        
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
            
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
        
        
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        fields = 
        ax.plot(obs_val*24., label=str(int(fid))+' '+str(n_image))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
        
        
        
fields = loadtxt('radec_Feb_2hrVis0.87frac.txt')
fields
fields[:,0] == field_index
get_ipython().run_line_magic('pwd', '')
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(n_image)+','+str(fields[counter][1]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
        
        
        
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        #fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(n_image)+','+str(fields[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
            
        
        
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        #fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(n_image)+','+str(fields[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':6})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
            
        
        
        
savefig('ZUDS_2hr087_VisPlot.pdf')
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        #fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(n_image)+','+str(fields[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':9})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
            
            
        
        
        
savefig('ZUDS_2hr087_VisPlot.pdf')
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        #fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(int(n_image))+','+str(fields[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':9})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
            
            
        
        
        
counter = 0
for kval in range(8):
    for rval in range(6):
        ax = subplot(gs[kval, rval])
        fid = field_index[counter]
        obs_val = aam[int(fid)]
        if int(fid) in n_iband_exp[:,0]:
            n_image = n_iband_exp[n_iband_exp[:,0] == fid][0][1] 
        else:
            n_image = 0
        #fields = 
        ax.plot(obs_val*24., label=str(int(fid))+','+str(int(n_image))+','+str(fields[counter][2]))
        ax.plot([0, 150],[2,2]) 
        ax.set_xlim(0, 145)
        counter+= 1
        ax.legend(loc=2, prop={'size':9})
        if kval > 6:
            ax.set_xlabel('Days since 15-10-2019')
        if rval == 0:
            ax.set_ylabel('Hours Vis')
            
            
        
        
        
savefig('ZUDS_2hr087_VisPlot.pdf')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('saveit', 'plotter.py')
get_ipython().run_line_magic('save', 'plotter.py')
get_ipython().run_line_magic('save', 'plotter.py 1-69')
