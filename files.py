"""Reads and writes files."""
import os
import random
import string
from logzero import logger

base_path = os.getcwd()
folder_path = base_path + '/newfolder3'

if base_path.os.exist():  # if not os.exists()
    os.makedirs(base_path)  #
    logger.info("new folder created")

# function to write the files
def wr():
    items = [x for x in range(1, 11)]
    size = 0
    for x in items:
        with open("{}.file.txt".format(x), "w")as f:
            size = size + 24
            r_char = ''.join([random.choice(string.ascii_letters) for n in range(size)])
            f.write("{}".format(r_char))
    return r_char

# function to read the files
def r():

    for f in os.listdir():
        with open("{} .file.txt".format(f), 'r') as f:
            if f.mode == 'r':
                f_content = f.read()
                f_size = os.path.getsize(f)
                f_name, f_ext = os.path.splitext(f)
                f_srno, f_name = f_name.split('.')
                logger.info('{} | {} | {} | {}'.format(f_srno, f_name, f_content, f_size))
wr()
r()
