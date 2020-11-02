import marton
import threading

def backup(router):
    servers = marton.login(**router)
    open_shell = marton.platform_shell(servers)
    marton.enter_command(open_shell, 'terminal length 0')
    marton.enter_command(open_shell, 'enable')
    marton.enter_command(open_shell, 'cisco1')
    marton.enter_command(open_shell, 'show run')
    output = marton.show(open_shell)
    output1 = output.splitlines()
    output1 = output1[8:-1]
    output = '\n'.join(output1)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour

    file_name = "C:/Users/User/Desktop/project/"f'{router["ip_address"]}_{year}-{month}-{day}.txt'
    with open(file_name, 'w') as f:
        f.write(output)
    marton.close(servers)
router1 = {'ip_address':'192.168.100.1', 'port':'22', 'username':'martins', 'password':'cisco'}
routers = [router1]

threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router, ))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
