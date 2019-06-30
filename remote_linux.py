import paramiko
import getpass

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.199.130', username='root', password=getpass.getpass())
cmd='free'
stdin,stdout,stderr=client.exec_command(cmd)

for line in stdout:
    print(line)
client.close()
