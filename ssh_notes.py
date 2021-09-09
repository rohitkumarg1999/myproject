              # >>> SSH  commands<<< #
to use the ssh we need the paramiko module
1-make sure sshd service is up and running
2-make sure passwordAuthantication is yes in sshd_config file
3-get username,password,hostname,remoteserver


#basic code
import paramiko
username="root"
passwd="1234567"
hostname=ip #ip of remote server
ssh_client=paramiko.SSHClient() #it will work everywhere
ssh_client.set_missing_host_key_policy(paramio.AutoAddPolicy) #its is user because we are conneting with server with unknown host key
ssh_client.connect(hostname,username,port,passwd)
print("wait server is conneting")

command="ls;pwd" #command could be anything
#*note: command may be more then one then use smicolu to seperte the command
stdin,stdout,stderr=ssh_client.exec_command(command)
stdout=stdout.readlines()
print(stdout)

         # use to uload the file on server <<< #
after the conneting with server
sftp=ssh_client.open_sftp()
path="/upload/src.py"
localpath="src.py"
sftp.put(localpath,path)



