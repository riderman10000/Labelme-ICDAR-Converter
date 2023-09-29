import os 
import argparse

'''
script to check the respective labels of the image are presented or not in the folder
'''

parser = argparse.ArgumentParser()
parser.add_argument('--image-dir', '-i', type=str, help='image directory')
parser.add_argument('--label-dir', '-l', type=str, help='label direcotry')
parser.add_argument('--image-extension', '-ie', type=str, default='jpg', help='extension of the images')
parser.add_argument('--label-extension', '-le', type=str, default='txt', help='extension of the labels')
args = parser.parse_args()

image_dir = vars(args)['image_dir']
label_dir = vars(args)['label_dir']

image_extension = '.' + vars(args)['image_extension']
label_extension = '.' + vars(args)['label_extension']

image_file_list = [ x for x in os.listdir(image_dir) if image_extension in x]
label_file_list = [ x for x in os.listdir(label_dir) if label_extension in x]

test_pass = True
for image_file_path, label_file_path in zip(image_file_list, label_file_list):
    print('[+] ', image_file_path)
    print('[+] ', label_file_path)
    # assert image_file_path.replace('.jpg', '') == label_file_path.replace('.txt', '') , '[-] file not found : ' + image_file_path
    if image_file_path.replace(image_extension, '') != label_file_path.replace(label_extension, ''):
        if image_file_path.replace(image_extension, label_extension) in label_file_list:
            print('[-] file not found : ' + label_file_path)
            test_pass = False
            break
        print('[-] file not found : ' + image_file_path)
        test_pass = False
        break
if test_pass:
    print('[+] Image Label check passed!')
else:
    print('[-] Missing image labels')