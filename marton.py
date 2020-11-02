import paramiko
import time

def login(ip_address, port, username, password):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to host: {ip_address}...')
    cl.connect(ip_address, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    return cl

def platform_shell(cl):
    shell = cl.invoke_shell()
    return shell

def enter_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)


def show(shell, n=10000):
    result = shell.recv(n)
    return result.decode()

def close(cl):
    if cl.get_transport().is_active():
        print('Connection Closed')
        cl.close()


