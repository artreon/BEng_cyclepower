import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

r1_mean_y_pred_ext = [183.72700070011416]
r1_mean_y_pred_min = [177.0062964182481]
r1_mean_y_test = [163.41259582143394]
r1_mean_watts_calc = [146.9395761310687]

r2_mean_y_pred_min = [227.28513645412843]
r2_mean_y_pred_ext = [239.42396376153658]
r2_mean_y_test = [248.9652281900031]
r2_mean_watts_calc = [309.4411673393356]

r3_mean_y_pred_min = [239.6096498269175]
r3_mean_y_pred_ext = [246.87163795794277]
r3_mean_y_test = [245.8491236380862]
r3_mean_watts_calc = [209.43391757460918]


mean_y_test=(r1_mean_y_test[0]+r2_mean_y_test[0]+r3_mean_y_test[0])/3.0
print('mean', mean_y_test)
r1_mean_y_pred_ext_glm = [179.29398990479825]
r1_mean_y_pred_min_glm = [181.83819316081704]
r1_mean_y_test_glm = [163.41259582143394]
r1_mean_watts_calc_glm = [146.9395761310687]

r2_mean_y_pred_min_glm  = [231.28522922802998]
r2_mean_y_pred_ext_glm  = [243.60118239863723]
r2_mean_y_test_glm  = [248.9652281900031]
r2_mean_watts_calc_glm  = [309.4411673393356]

r3_mean_y_pred_min_glm  = [241.53188795217318]
r3_mean_y_pred_ext_glm  = [249.4258949091221]
r3_mean_y_test_glm  = [245.8491236380862]
r3_mean_watts_calc_glm  = [209.43391757460918]



r1_mean_y_pred_ext_svr = [216.99470218125322]
r1_mean_y_pred_min_svr = [216.90749555963717]
r1_mean_y_test_svr = [163.41259582143394]
r1_mean_watts_calc_svr = [146.9395761310687]

r2_mean_y_pred_min_svr = [202.78150962972185]
r2_mean_y_pred_ext_svr = [202.98539711724382]
r2_mean_y_test_svr = [248.9652281900031]
r2_mean_watts_calc_svr = [309.4411673393356]

r3_mean_y_pred_min_svr = [249.04743858000347]
r3_mean_y_pred_ext_svr = [249.00248463918058]
r3_mean_y_test_svr = [245.8491236380862]
r3_mean_watts_calc_svr = [209.43391757460918]





avg_min_test_calc=[[r1_mean_y_pred_min[0],r2_mean_y_pred_min[0],r3_mean_y_pred_min[0]],
[r1_mean_y_test[0],r2_mean_y_test[0],r3_mean_y_test[0]],
 [r1_mean_watts_calc[0],r2_mean_watts_calc[0],r3_mean_watts_calc[0]]]

avg_ext_test_calc=[[r1_mean_y_pred_ext[0],r2_mean_y_pred_ext[0],r3_mean_y_pred_ext[0]],
[r1_mean_y_test[0],r2_mean_y_test[0],r3_mean_y_test[0]],
 [r1_mean_watts_calc[0],r2_mean_watts_calc[0],r3_mean_watts_calc[0]]]
 
 
 
avg_min_test_calc_glm=[[r1_mean_y_pred_min_glm[0],r2_mean_y_pred_min_glm[0],r3_mean_y_pred_min_glm[0]],
[r1_mean_y_test_glm[0],r2_mean_y_test_glm[0],r3_mean_y_test_glm[0]],
 [r1_mean_watts_calc_glm[0],r2_mean_watts_calc_glm[0],r3_mean_watts_calc_glm[0]]]

avg_ext_test_calc_glm=[[r1_mean_y_pred_ext_glm[0],r2_mean_y_pred_ext_glm[0],r3_mean_y_pred_ext_glm[0]],
[r1_mean_y_test_glm[0],r2_mean_y_test_glm[0],r3_mean_y_test_glm[0]],
 [r1_mean_watts_calc_glm[0],r2_mean_watts_calc_glm[0],r3_mean_watts_calc_glm[0]]]
 
 
 
avg_min_test_calc_svr=[[r1_mean_y_pred_min_svr[0],r2_mean_y_pred_min_svr[0],r3_mean_y_pred_min_svr[0]],
[r1_mean_y_test_svr[0],r2_mean_y_test_svr[0],r3_mean_y_test_svr[0]],
 [r1_mean_watts_calc_svr[0],r2_mean_watts_calc_svr[0],r3_mean_watts_calc_svr[0]]]

avg_ext_test_calc_svr=[[r1_mean_y_pred_ext_svr[0],r2_mean_y_pred_ext_svr[0],r3_mean_y_pred_ext_svr[0]],
[r1_mean_y_test_svr[0],r2_mean_y_test_svr[0],r3_mean_y_test_svr[0]],
 [r1_mean_watts_calc_svr[0],r2_mean_watts_calc_svr[0],r3_mean_watts_calc_svr[0]]]


fig=plt.figure(figsize=(15,9))

#Lasso
X=np.arange(1)
plt.subplot(231)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_min_test_calc[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_min_test_calc[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_min_test_calc[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])
print(max(avg_min_test_calc))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_min_test_calc[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('Lasso Minimal Features')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)
plt.ylabel('Average Power')
#plt.xlabel('Riders')


X=np.arange(1)
plt.subplot(234)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_ext_test_calc[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_ext_test_calc[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_ext_test_calc[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])

print(max(avg_ext_test_calc))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_ext_test_calc[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('Lasso Extended Features')
#plt.ylabel('Average Power')
plt.xlabel('Riders')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)


#GLM

plt.subplot(232)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_min_test_calc_glm[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_min_test_calc_glm[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_min_test_calc_glm[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])
print(max(avg_min_test_calc_glm))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_min_test_calc_glm[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc_glm[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc_glm[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('GLM Minimal Features')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)
#plt.ylabel('Average Power')
#plt.xlabel('Riders')


plt.subplot(235)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_ext_test_calc_glm[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_ext_test_calc_glm[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_ext_test_calc_glm[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])

print(max(avg_ext_test_calc_glm))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_ext_test_calc_glm[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc_glm[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc_glm[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('GLM Extended Features')
#plt.ylabel('Average Power')
plt.xlabel('Riders')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)


#SVR

plt.subplot(233)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_min_test_calc_svr[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_min_test_calc_svr[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_min_test_calc_svr[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])
print(max(avg_min_test_calc_svr))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_min_test_calc_svr[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc_svr[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_min_test_calc_svr[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('SVR Minimal Features')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)
#plt.ylabel('Average Power')
#plt.xlabel('Riders')

X=np.arange(1)
plt.subplot(236)
plt.axis([0.3,4.3,0,400])
bar1=plt.bar([1,2,3], avg_ext_test_calc_svr[0], color = '#CD2626', width = 0.3)
bar2=plt.bar([1.3,2.3,3.3], avg_ext_test_calc_svr[1], color = '#6E8B3D', width = 0.3)
bar3 = plt.bar([1.6,2.6,3.6],avg_ext_test_calc_svr[2], width = 0.3)
plt.xticks([1.3,2.3,3.3],['R1','R2','R3'])

print(max(avg_ext_test_calc_svr))
#plt.ylim((0,max(max(svr_min_rmse_sensor))))

for i,v in enumerate(avg_ext_test_calc_svr[0]):
    plt.text(bar1[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc_svr[1]):
    plt.text(bar2[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
for i,v in enumerate(avg_ext_test_calc_svr[2]):
    plt.text(bar3[i].get_xy()[0] + 0.15, v/2-20, str(round(v,3)),rotation=90,color='white',fontsize=7)
    
plt.title('SVR Extended Features')
#plt.ylabel('Average Power')
plt.xlabel('Riders')
plt.legend(('Model Avg. Power','Sensor Avg. Power', 'Strava Avg. Power'),fontsize = 6)
fig.suptitle('Model vs Sensor vs Strava Average Power - Minimal/Extended Features')
#plt.savefig('lasso_glm_svr_avg_power_min_ext.png')
#plt.show()
