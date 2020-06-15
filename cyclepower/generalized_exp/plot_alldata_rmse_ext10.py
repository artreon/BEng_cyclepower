import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lasso = 30.729875117758855
svr= 26.830182792758194
glm = 25.782769895406723
lstm = 4.3830293121912005#2.3830293121912005
strava = 42.30286816484331
             

error = [lasso,svr,glm,lstm]#,strava

X=np.arange(1,5)
plt.axis([0,5,0,100])
bar1=plt.bar(X, error, color=['#CD2626','#6E8B3D','Blue','#e1776f'], width = 0.3) #,'#a62b65'
plt.xticks(X,['Lasso','SVR','GLM','LSTM'], fontsize=11) #,'Strava'
plt.yticks(fontsize=11)
#print(max(svr_min_rmse_sensor))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(error):
    plt.text(bar1[i].get_xy()[0] +.1 , v+2, str(round(v,3)),rotation=90,color='black',fontsize=8)
    
plt.title('RMSE - All Riders 10-Sec Average Data With Extended Features',fontsize=11)
plt.ylabel('Error (W)',fontsize=11)
plt.xlabel('Models',fontsize=11)
plt.tight_layout()
plt.savefig('plot_alldata_rmse_ext10.png')

plt.show()
