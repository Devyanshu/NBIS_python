import os
import cv2
import argparse
'''
This Python file will generate partial fingerprints of size 150x150
from the images of a given directory.
Partial fingerprints will be generated with a 50% overlap, to change this,
change the value of overlap variable, in fractions. Provide a path to the
original image directory and a path to location to save the images.
The partial images are saved with the same name as the original image
follwed by RxC, where R is the row from which the partial image is created
and C is the column. For more detail see: https://github.com/Devyanshu/image-split-with-overlap
'''
# _______________________________Warning _____________________________________#
'''
Please make sure that if you are using partial images, they are made from the
same process beacuse it has been observed that the images made from this file
and MATLAB, using the same logic, were not same. So to ensure correctness of
experiments, use images from a single source only,
'''
#____________________________________________________________________________#


def start_points(size, window_size, overlap):
    points = [0]
    stride = int(window_size * (1-overlap))
    counter = 1
    while True:
        pt = stride*counter
        if pt+window_size >= size:
            points.append(pt - ((pt+window_size)-size))
            break
        else:
            points.append(pt)
        counter += 1
    return points


os_path_join = os.path.join
cv2_imwrite = cv2.imwrite

if __name__ == '__main__':
    # code for cli arguments
    parser = argparse.ArgumentParser(
        description='Generate partial fingerprint images from a given original image')
    parser.add_argument(
        '-p', '--path', help='Required. Path to the directory containing original images', required=True)
    parser.add_argument(
        '-s', '--save', help='Reqired. Path to save to partial images.', required=False)
    args = vars(parser.parse_args())

    path = args['path']
    save_path = args['save']
    if save_path[-1] == '/':
        save_path = save_path[:-1]

    wh, ww = 150, 150
    # by default, overlap if 50%, change it here
    overlap = 0.5
    files = os.listdir(path)
    for file in files:
        img = cv2.imread(os_path_join(path, file), cv2.COLOR_BGR2GRAY)
        (h, w) = img.shape[:2]
        X_points = start_points(w, ww, overlap)
        Y_points = start_points(h, wh, overlap)
        row = 1
        column = 1
        for i in Y_points:
            for j in X_points:
                cropped = img[i:i+wh, j:j+ww]
                cv2_imwrite('{}/{}-{}x{}.jpeg'.format(save_path,
                                                      file.split('.')[0], row, column), cropped)
                column += 1
            column = 1
            row += 1
