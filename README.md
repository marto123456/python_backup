# python_backup
Backup multiple routers with python

We will use multithreading to ensure that all the routers can be backed up at the same time instead of one after the other.
To achieve this, we import threading.
Also, ensure that your routers are reachable and that ssh is enabled on the routers.

Create a shared network folder or a local folder on the computer where the backup file will be stored.
In my script, that position is c:/Users/user/Desktop/project.  ###Edit this value as per your need

You can clone or download this project into pycharm and enhance it as per your desire.

This script uses paramiko. The paramiko module has been used to create a module called marto.
Importing marto into our project gives it all the benefits of paramiko.
