import os
from local_settings import APP_SERVER_PATH, APP_CLIENT_PATH, APP_FTP_PATH, SERVER, SERVER_DISK
import shutil


def get_path_server_by_number(n):
    return '\\\\' + SERVER + '-' + str(n) + '\\' + SERVER_DISK + '$\\'


def copy_file(name_file, path):
    try:
        shutil.copy(name_file, path)
        print('Copied', name_file, 'to', path)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def update_dll(name_file):
    for i in range(0, 6):
        path = get_path_server_by_number(i) + APP_SERVER_PATH

        copy_file(name_file, path)

def update_bpl(name_file):
    for i in range(0, 22):
        path = get_path_server_by_number(i) + APP_CLIENT_PATH

        copy_file(name_file, path)

def update_zip(name_file):
    for i in range(0, 22):
        path = get_path_server_by_number(i) + APP_FTP_PATH

        copy_file(name_file, path)

if '__main__' in __name__:
    try:
        dir_list = os.listdir()

        for i in dir_list:
            if '.dll' in i:
                update_dll(i)
                continue
            if '.bpl' in i:
                update_bpl(i)
                continue
            if '.zip' in i:
                update_zip(i)
                continue

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    os.system(r'PAUSE')