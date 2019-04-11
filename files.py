"""Reads and writes files."""
import os
import random
import string



def create_file(base_path):
    """Function to create file."""
    if not os.path.exists(base_path):
        os.makedirs(folder_path)
        print("new folder created")


def write_functions(folder_path):
    """Function is used to write."""
    items = [x for x in range(1, 11)]
    size = 0
    for x in items:
        file_path = folder_path + "/{}.file.txt".format(x)
        with open(file_path, "w")as f:
            size = size + 24
            r_char = ''.join([random.choice(string.ascii_letters) for n in range(size)])
            f.write("{}".format(r_char))
    return r_char


# def read_functions(folder_path):
#     """Function is used to read."""
#     for file in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file)
#         with open(file_path, 'r') as f:
#             f_content = f.read()
#             f_size = os.path.getsize(file_path)
#             f_name, f_ext = os.path.splitext(f)
#             f_srno, f_name = f_name.split('.')
#             logger.info('{} | {} | {} | {}'.format(f_srno, f_name, f_content, f_size))


def read_functions(folder_path):
    """Function to read the files."""
    count = 0
    print('{} | {} | {} | {}'.format('Sr No.', 'File name', 'Content', 'Size'))
    for file in os.listdir(folder_path):
        count += 1
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            f_size = os.path.getsize(file_path)
            print('{} | {} | {} | {}'.format(count, file, f.read(), f_size))


base_path = os.getcwd()
folder_path = base_path + '/newfolder3'
create_file(folder_path)
write_functions(folder_path)
read_functions(folder_path)
