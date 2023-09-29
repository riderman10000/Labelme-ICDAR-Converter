import os 
import json 
import sys
import argparse

json_dict = {
    'version': '5.1.1',
    'flags': {},
    'shapes': [],
    'imagePath': 0,
    'imageData': 0,
    'imageHeight': 0,
    'imageWidth': 0,
}

label_dict = { # shapes
    'label': "",
    'points': [],
    'group_id': None,
    'description': None,
    'shape_type': 'polygon',
    'flags': {}
}

parser = argparse.ArgumentParser()
parser.add_argument('--json-dir', '-j',  type=str, help='path to directory where the json files are presented')
parser.add_argument('--text-dir', '-t', type=str, help='path to directory to save the generated text files')
args = parser.parse_args()

txt_dir = vars(args)['text_dir']
json_dir = vars(args)['json_dir']


for file in os.listdir(json_dir):
    if '.json' in file:
        with open(os.path.join(json_dir, file)) as json_file:
            print('[+] Txt file of ', file)
            image_json_info = json.load(json_file)
            labels = []
            for label_shape_dict in image_json_info['shapes']:
                # print(label_shape_dict)
                label, xycoordinates = label_shape_dict['label'], label_shape_dict['points']
                points = []
                points_str = ''
                for x,y in xycoordinates:
                    points_str += str(int(x)) +', '+str(int(y)) + ', ' # add as such because the format looks like: x1, y1, x2, y2, x3, y3, x4, y4 ..., label_name
                txt_lable_point_str = points_str + label +'\n'
                labels.append(txt_lable_point_str)
                # print(label, points, '\n', points_str)
            with open(os.path.join(txt_dir, file.replace('.json', '.txt')), 'w+') as txt_file:
                for label in labels:
                    txt_file.write(label)

print('[+] Done Converting')