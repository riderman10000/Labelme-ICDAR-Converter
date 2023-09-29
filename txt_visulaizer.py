import os 
import cv2  
import numpy as np
import argparse
import textwrap


parser = argparse.ArgumentParser(epilog=textwrap.dedent(
    '''
    About:
        script to visulaize the labels and check if they are valid
    '''))
parser.add_argument('--image-dir', '-i', type=str, help='path to image directory')
parser.add_argument('--text-dir', '-t', type=str, help='path to text directory of labels')
parser.add_help = True
args = parser.parse_args()

image_dir = vars(args)['image_dir']
txt_dir = vars(args)['text_dir']

for file in os.listdir(txt_dir):
    if '.txt' in file:
        with open(os.path.join(txt_dir, file), 'r') as txt_file:
            # read the points from the file 
            lines = txt_file.readlines()
            polygons = {}
            for line in lines:
                # extract the label and points 
                line_info = line.replace(' ', '').strip('/n').split(',')
                points, label = [ int(x) for x in line_info[:-1]], line_info[-1]
                xy_coordinate = []
                for i in range(0, len(points), 2):
                    xy_coordinate.append([points[i], points[i+1]])
                xy_coordinate = np.array(xy_coordinate)
                xy_coordinate = xy_coordinate.reshape((-1, 1, 2))
                polygons[label] = xy_coordinate
            
            # open image 
            image_path = os.path.join(image_dir, file.replace('.txt', '.jpg'))
            if os.path.exists(image_path):
                image = cv2.imread(image_path)
                for i, label in enumerate(polygons.keys()):
                    image = cv2.polylines(image, [polygons[label]], isClosed=True, color=(255 * (i == 0)  , 255 * (i == 1), 255 * (i == 2)), thickness= 2)
                cv2.imshow(file, image)
                if cv2.waitKey(2000) & 0xFF == 27:
                    exit()
                cv2.destroyAllWindows()