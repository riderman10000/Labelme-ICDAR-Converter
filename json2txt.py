##################### imports ########################

import json
import os
import argparse
import sys

########## cli document ############
parser=argparse.ArgumentParser()
parser.add_argument('--text_dir=',type=str)
parser.add_argument('--json_dir=',type=str)
args=parser.parse_args()

json_dir=vars(args)['json_dir=']
txt_dir=vars(args)['text_dir=']


################### directories #####################
# json_dir='C:/innate2/ocrUnilever/det_db/outtxt/'
# txt_dir='C:/innate2/ocrUnilever/det_db/img+txtuni/'

################################ Conversion ###############
print("Started!!!!!!!!")
u=0
for filename in os.listdir(json_dir):

    g = os.path.join(json_dir, filename)
    if os.path.isfile(g):
        if '.json' in g:
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
                json_name=g.replace(json_dir,'')
                txt_name=json_name.replace('.json','.txt')
                f=open(txt_dir+txt_name,'a')
                f.write(str(points_str))
                f.write('\n')
                f.close()
            u=u+1
            print("Number of conversion completed: ",u)
print("COMPLETED")