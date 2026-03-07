import os
import sys
import threading
import time
import webview
from django.core.management import execute_from_command_line

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def start_django_server():
    """This function secretly runs your Django server in the background."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nutritrack_project.settings')
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])

if __name__ == '__main__':
    # Fix for Windows Taskbar to show your custom icon instead of the Python snake
    try:
        import ctypes
        myappid = 'nutritrack.health.dashboard.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception:
        pass

    # 1. Start the Django server in a separate background thread
    server_thread = threading.Thread(target=start_django_server)
    server_thread.daemon = True
    server_thread.start()

    # 2. Give Django 2 seconds to fully boot up
    time.sleep(2)

    # 3. Create a PERMANENT storage path in your Windows AppData folder
    app_data_path = os.environ.get('APPDATA', os.path.expanduser('~'))
    permanent_storage = os.path.join(app_data_path, 'NutriTrack_App_Data')

    # 4. Define the path to your new icon
    icon_path = resource_path('logo.ico')

    # 5. Define the window
    webview.create_window(
        title='NutriTrack - Personal Health Dashboard',
        url='http://127.0.0.1:8000',
        width=1200,
        height=800,
        resizable=True
    )

    # 6. Start the app with the storage path AND the custom icon attached!
    webview.start(private_mode=False, storage_path=permanent_storage, icon=icon_path)