import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lasso = 34.56865606833308
svr= 26.79907035944703
glm = 23.865097442565276
lstm = 5.050731652226662# 3.050731652226662
strava = 42.30286816484331
             

error = [lasso,svr,glm,lstm]#,strava

X=np.arange(1,5)
plt.axis([0,5,0,100])
bar1=plt.bar(X, error, color=['#CD2626','#6E8B3D','Blue','#e1776f'], width = 0.3) #,'#a62b65'
plt.xticks(X,['Lasso','SVR','GLM','LSTM'], fontsize=11) #'Strava'
plt.yticks(fontsize=11)
#print(max(svr_min_rmse_sensor))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(error):
    plt.text(bar1[i].get_xy()[0] +.1 , v+2, str(round(v,3)),rotation=90,color='black',fontsize=8)
    
plt.title('RMSE - All Riders 10-Sec Average Data With Minimal Features',fontsize=11)
plt.ylabel('Error (W)',fontsize=11)
plt.xlabel('Models',fontsize=11)
plt.tight_layout()
plt.savefig('plot_alldata_rmse_min10.png')

plt.show()
