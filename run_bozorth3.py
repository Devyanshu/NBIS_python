import os
import argparse
'''
This Python file takes a directory and matches xyt files,
one by one, to all the xyt files in the directory. Thus, it is assumed that
the path given has only xyt files.
The result of the bozorth3 comparison is displayed as the output on the
terminal, to save the result to a text file for processing, use the '>>'
operator to append the output.
Example run_bozorth3.py -p /home/Desktop/XYT >> result.txt
'''
if __name__ == "__main__":
    # code for cli arguments
    parser = argparse.ArgumentParser(description='desc')
    parser.add_argument(
        '-p', '--path', help='Required. Path to the directory', required=True)
    parser.add_argument(
        '-t', '--threshold', help='Optional. Threshold value to run Bozorth3.\
        Default value is 0', required=False, default=0)
    args = vars(parser.parse_args())

    path = args['path']
    if path[-1] == '/':
        path = path[:-1]
    threshold = args['threshold']

    # Running bozorth3 using os.system(),
    # See manual for bozorth3 for details on argument and parameters
    for file in os.listdir(path):
        os.system('bozorth3 -m1 -A outfmt=spg -T {} -p {} {}/*.xyt'
                  .format(threshold, os.path.join(path, file), path))
