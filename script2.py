import sys
import os
import os.path
import hashlib
import paramiko
from exceptions import Exception


#f = open(sys.argv[1])
#hosts = f.readlines()
hosts = ["192.168.1.20", "192.168.1.30"]
user = 'vagrant'
passw = 'vagrant'
port = 22

def connection():
	checkFiles = {}
	for i in range(len(hosts)):
		host = str(hosts[i])
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname=host, username=user, password=passw, port=port)
		stdin, stdout, stderr = client.exec_command('md5sum /home/vagrant/myDoc')
		data = stdout.read() + stderr.read()
		checkFiles[i] = data
		client.close()
	return checkFiles

def checkCopies():
	checkFiles = connection()
	checked = []
	c=0
	for i in range(len(hosts)):
	        fileToCheck1= hosts[i]
	        for j in range(len(hosts)):
	                if (i!=j):
	                        fileToCheck2= hosts[j]
	                        if fileToCheck2 not in checked:
	                                if (checkFiles[i]==checkFiles[j]):
	                                        print "Fine: "+"\n" +(str(hosts[i]))+" "+(str(hosts[j]))
	        				c+=1
		checked.append(fileToCheck1)
	if c==0:
		raise Exception("They are not the same.")

checkCopies()
