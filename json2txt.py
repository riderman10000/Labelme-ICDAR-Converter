##################### imports ########################

import json
import os

################### directories #####################
dir='./json/'
txt_dir='./txt/'

################################ Conversion ###############
print("Started!!!!!!!!")
u=0
for filename in os.listdir(dir):

    g = os.path.join(dir, filename)
    if os.path.isfile(g):
        f=open(g)
        data = json.load(f)
        for i in range(0,len(data['shapes'])):
            points_list=[]
            for j in range(0,4):
                for k in range(0,2):
                    points_list.append(int(data['shapes'][i]['points'][j][k]))
            points_list.append(data['shapes'][i]['label'])
            
            a=str(points_list).replace('[','')
            b=str(a).replace(']','')
            points_str=str(b).replace("'","")
            json_name=g.replace(dir,'')
            txt_name=json_name.replace('.json','.txt')
            f=open(txt_dir+txt_name,'a')
            f.write(str(points_str))
            f.write('\n')
            f.close()
            u=u+1
            print("Number of conversion completed: ",u)
print("COMPLETED")