import time
import datetime
import paramiko

def ssh_con():

    print('start = ', datetime.datetime.now())
    print('Delete unkown gateway and reset to default settings')
    time.sleep(5)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.2.1', username='root', password='Pr0L1@nt')

    for i in range(2, 256):
        time.sleep(1)
        print(f'request to delete arp table for ip: 192.168.2.{i}')
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(f'arp 192.168.2.{i} -d')

    # for line in ssh_stdout:
    #     results.append(line.strip('\n'))
    print("ok")


while True:
    if __name__ == '__main__':
        ssh_con()
