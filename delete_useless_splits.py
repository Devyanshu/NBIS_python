import os
import argparse

os_remove = os.remove
os_path_join = os.path.join


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This Python file deletes\
        the partial images that have minutiae <10 ")
    parser.add_argument(
        '-x', '--xyt', help="Path to the xyt files directory", required=True)
    parser.add_argument(
        '-i', '--image', help="Path to the image directory", required=True)
    args = vars(parser.parse_args())
    xyt_path = args['xyt']
    file_path = args['image']
    counter = 0
    xyts = set()
    for xyt in os.listdir(xyt_path):
        xyts.add(xyt)
    for img in os.listdir(file_path):
        if img.split('.')[0]+'.xyt' not in xyts:
            counter += 1
            os_remove(os_path_join(file_path, img))
    print("{} file(s) deleted".format(counter))
