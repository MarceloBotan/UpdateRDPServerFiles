import os
from local_settings import *
import shutil
from datetime import datetime

SERVERS = [0, 1, 2, 5, 6]
CLIENTS = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def get_path_server_by_number(n):
    return '\\\\' + SERVER + '-' + str(n) + '\\' + SERVER_DISK + '$\\'

def copy_file(path_file, path):
    try:
        shutil.copy(path_file, path)
        print('Copied', path_file.split('\\')[-1], 'to', path.split('\\')[2])

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def rename_file(file_name, path):
    try:
        new_name = file_name + '.old.' + str(datetime.now().strftime('%Y%m%d%H%M%S'))
        new_path = path + new_name
        file_path = path + file_name

        os.rename(file_path, new_path)
        print('\nRenamed', file_name)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def delete_old():
    pass

def is_local():
    if server_number not in SERVERS and server_number not in CLIENTS:
        return True
    return False

def update_servers(file_name, update_path, rename = True):
    for i in SERVERS:
        update_files(i, file_name, update_path, rename)

def update_clients(file_name, update_path, rename = True):
    for i in CLIENTS:
        update_files(i, file_name, update_path, rename)

def update_files(i, file_name, update_path, rename = True):
    if i == server_number:
        return

    path = get_path_server_by_number(i) + update_path

    if rename:
        rename_file(file_name, path)

    if not is_local():
        copy_path = get_path_server_by_number(server_number) + update_path
        copy_file(copy_path + file_name, path)
        return

    copy_file(file_name, path)

    # if update_path == APP_ZABBIX_PATH:
    #     os.system('net stop "Zabbix Agent" && net start "Zabbix Agent"')


def local_update():
    try:
        dir_list = os.listdir()

        for i in dir_list:
            print(i)
            if '.dll' in i:
                update_servers(i, APP_SERVER_PATH)

            elif '.zip' in i:
                update_servers(i, APP_FTP_PATH)
                update_clients(i, APP_FTP_PATH)

            elif '.bpl' in i and '.zip' not in i:
                update_servers(i, APP_CLIENT_PATH)
                update_clients(i, APP_CLIENT_PATH)

            elif '.bat' in i or '.vbs' in i or ('.exe' in i and not 'update_files.exe' in i):
                update_servers(i, APP_SAPORE_INFO_PATH, False)
                update_clients(i, APP_SAPORE_INFO_PATH, False)

            elif '.QR2' in i:
                update_servers(i, APP_RELFTP_PATH)
                update_clients(i, APP_RELFTP_PATH)

            elif '.conf' in i:
                update_servers(i, APP_ZABBIX_PATH)
                update_clients(i, APP_ZABBIX_PATH)
    
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    os.system(r'PAUSE')
    
def server_update():
    try:
        qry_name = input('File name (xxx00000.qr2): ').upper()

        update_servers(qry_name, APP_RELFTP_PATH)
        update_clients(qry_name, APP_RELFTP_PATH)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    os.system(r'PAUSE')

if '__main__' in __name__:
    server_number = int(input('Copy from server ... ([0-9] or -1 to local files): '))

    if is_local():
        local_update()
    else:
        server_update()
    