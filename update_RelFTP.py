import os
from local_settings import APP_RELFTP_PATH
from local_settings import SERVER, SERVER_DISK
import shutil
from datetime import datetime

server_number = 0
qry_name = ''

def get_path_server_by_number(n) -> str:
    return '\\\\' + SERVER + '-' + str(n) + '\\' + SERVER_DISK + '$\\'

def copy_file(name_file, path) -> None:
    try:
        shutil.copy(get_path_server_by_number(server_number) + APP_RELFTP_PATH + name_file, path)
        print('Copied', name_file, 'to', path)

    except Exception as e:
        if rename_file(name_file, path):
            return

        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

def rename_file(name_file, path) -> bool:
    try:
        new_name = name_file + '.old.' + str(datetime.now().date())
        os.rename(path + name_file, path + new_name)
        print('Renamed', name_file, 'to', new_name)

        copy_file(name_file, path)

        return True

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
        return False

def update_qry(name_file):
    for i in range(0, 22):
        if i == server_number:
            continue

        path = get_path_server_by_number(i) + APP_RELFTP_PATH

        copy_file(name_file, path)

if '__main__' in __name__:
    try:
        server_number = int(input('Copiar do Servidor (apenas o número do servidor): '))
        qry_name = input('Nome do arquivo completo (xxx00000.qr2): ').upper()

        qry_path = '\\' + qry_name

        update_qry(qry_path)

    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    os.system(r'PAUSE')