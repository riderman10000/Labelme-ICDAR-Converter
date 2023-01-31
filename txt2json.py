import cv2
import numpy as np
import labelme
import os
import base64
import json

import argparse
import sys

########## cli document ############
parser=argparse.ArgumentParser()
parser.add_argument('--img_dir=',type=str)
parser.add_argument('--text_dir=',type=str)
parser.add_argument('--json_dir=',type=str)
args=parser.parse_args()

img_dir=vars(args)['img_dir=']
outjson_dir=vars(args)['json_dir=']
txt_dir=vars(args)['text_dir=']

############################# select dir ############
#img_dir='C:/innate2/ocrUnilever/det_db/outtxt/'
#outjson_dir='C:/innate2/ocrUnilever/det_db/outtxt/'
#txt_dir='C:/innate2/ocrUnilever/det_db/outtxt/'
print("Started!!!!!!!!")
print("Please Wait!!!!!!!!!!! This may take few moments")
###################### extract image data #################
imgo=[]
image_data=[]
v=0
for filename in os.listdir(img_dir):
    o = os.path.join(img_dir, filename)
    
    if os.path.isfile(o):

        if '.jpg' in str(o):
            data = labelme.LabelFile.load_image_file(o)
            image_data.append(base64.b64encode(data).decode('utf-8'))
            imgo.append(cv2.imread(o))
            v=v+1
            print("Number of data stored: ",v)
u=0

for txtname in os.listdir(txt_dir):
    q = os.path.join(txt_dir, txtname)

    if os.path.isfile(q):
        if '.txt' in q:
    ############################ extract coordinates from txt #################
            h=open(q)
            #print(h.read()) 
            n=[]
            l=[]
            for j in range(0,len(h.readlines())):
                m=[]
                for i in range(0,8):
                    g=open(q)
                    m.append(str(list(g.read().split('\n'))[j]).split(',')[i])
                    g.close()
                n.append(m)
                g=open(q)
                #l.append(str(list(g.read().split('\n'))[j]).split(',')[8])
                l=[]
                t=open('system/base.txt','r')
                l.append(t.read().split('\n'))
                g.close()
            
            ###################### make json #################
            if len(n)==1:
                with open('system/base1.json','r') as json_file:
                    data=json.load(json_file)
            
            if len(n)==2:
                with open('system/base2.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==3:

                with open('system/base3.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==4:
                with open('system/base4.json','r') as json_file:
                    data=json.load(json_file)
            
            if len(n)==5:
                with open('system/base5.json','r') as json_file:
                    data=json.load(json_file)

            if len(n)==6:

                with open('system/base6.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==7:
                with open('system/base7.json','r') as json_file:
                    data=json.load(json_file)
            
            if len(n)==8:
                with open('system/base8.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==9:

                with open('system/base9.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==10:
                with open('system/base10.json','r') as json_file:
                    data=json.load(json_file)
            
            if len(n)==11:
                with open('system/base11.json','r') as json_file:
                    data=json.load(json_file) 

            if len(n)==12:

                with open('system/base12.json','r') as json_file:
                    data=json.load(json_file)
               

            for j in range(0,len(n)): 
                data['shapes'][j]['label']=l[0][j]
                data['shapes'][j]['points']=[[float(n[j][0]), float(n[j][1])], [float(n[j][2]), float(n[j][3])], [float(n[j][4]), float(n[j][5])], [float(n[j][6]),float(n[j][7])]]
            data['imageData']=image_data[u]
            data['imageHeight']=imgo[u].shape[0]
            data['imageWidth']=imgo[u].shape[1]
            data['imagePath']=txtname.replace('.txt','.jpg')
            p=txtname.replace('.txt','.json')
            with open(outjson_dir+str(p), "w") as outfile:
                json.dump(data, outfile)
            u=u+1
            print("Number of conversion completed: ",u)
print("COMPLETED")