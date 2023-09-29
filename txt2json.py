import os 
import cv2 
import labelme 
import base64
import json 
import argparse 

json_dict = {
    'version': '5.1.1',
    'flags': {},
    'shapes': [],
    'imagePath': 0,
    'imageData': 0,
    'imageHeight': 0,
    'imageWidth': 0
}

label_dict = {
    'label': "",
    'points': [],
    'group_id': None,
    'description': None,
    'shape_type': 'polygon',
    'flags': {}
}

parser = argparse.ArgumentParser()
parser.add_argument('--image-dir', '-i', type=str, help='path to directory where the image files are presented')
parser.add_argument('--text-dir', '-t', type=str, help='path to directory where the text files are presented')
parser.add_argument('--json-dir', '-j', type=str, help='path to directory to save the generated json files')
args = parser.parse_args()

image_dir = vars(args)['image_dir']
txt_dir = vars(args)['text_dir']
json_dir = vars(args)['json_dir']

for file in os.listdir(txt_dir):
    if '.txt' in file:
        image_json_info = json_dict
        with open(os.path.join(txt_dir, file), 'r') as txt_file:
            lines = txt_file.readlines()
            for line in lines:
                line_info = line.replace(' ', '').strip('\n').split(',')
                points, label = [ int(x) for x in line_info[:-1]], line_info[-1]
                xy_coordinate = []
                for i in range(0, len(points), 2):
                    xy_coordinate.append([points[i], points[i+1]])
                print(xy_coordinate, label)
                line_label_dict = label_dict.copy()
                line_label_dict['label'] = label
                line_label_dict['points'] = xy_coordinate
                image_json_info['shapes'].append(line_label_dict)
                print(len(line_label_dict['points']))
                line_label_dict = {}
            
            image_path = os.path.join(image_dir, file.replace('.txt', '.jpg'))
            if os.path.exists(image_path):
                image_json_info['imagePath'] = image_path
                image_json_info['imageData'] = base64.b64encode(
                    labelme.LabelFile.load_image_file(image_path)).decode('utf-8')
                image = cv2.imread(image_path)
                height, width, channel = image.shape 
                image_json_info['imageHeight'] = height
                image_json_info['imageWidth'] = width

                with open(os.path.join(json_dir, file.replace('.txt', '.json')), 'w+') as json_file:
                    json.dump(image_json_info, json_file)
                print('file save in ')
            else:
                print('[-] could not generate file for : ', txt_file)
            image_json_info['shapes'] = []
            del image_json_info 
