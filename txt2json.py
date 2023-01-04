import cv2
import numpy as np
import labelme
import os
import base64
import json 

############################# select dir ############
img_dir='./img+txt/'
outjson_dir='./img+txt/'
txt_dir='./img+txt/'
print("Started!!!!!!!!")
print("Please Wait!!!!!!!!!!! This may take few moments")
###################### extract image data #################
imgo=[]
image_data=[]
for filename in os.listdir(img_dir):
    o = os.path.join(img_dir, filename)
    
    if os.path.isfile(o):

        if '.jpg' in str(o):
            data = labelme.LabelFile.load_image_file(o)
            image_data.append(base64.b64encode(data).decode('utf-8'))
            imgo.append(cv2.imread(o))
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
                t=open('base.txt','r')
                l.append(t.read().split('\n'))
                g.close()
            
            ###################### make json#################
            if len(n)==3:

                with open('base3.json','r') as json_file:
                    data=json.load(json_file)
            if len(n)==4:
                with open('base4.json','r') as json_file:
                    data=json.load(json_file)
            
            if len(n)>4:
                with open('base5.json','r') as json_file:
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