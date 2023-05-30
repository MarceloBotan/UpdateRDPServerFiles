# Update files between RDP servers

Files update automation in RDP servers

Add local_settings.py in the same update_files.exe directory's

```bash 
APP_SERVER_PATH = 'path_to_app_server_dir'
APP_CLIENT_PATH = 'path_to_app_client_dir'
APP_FTP_PATH = 'path_to_app_ftp_dir'

SERVER = 'server_name_without_number'
SERVER_DISK = 'C'
```

## Compile exe

To compile a exe python file, first install the requirements.txt in a virtual enviorment

```bash
python -m venv venv
```

```bash
pip install -r requirements.txt
```

And compile

```bash
pyinstaller update_files.py --onefile
```