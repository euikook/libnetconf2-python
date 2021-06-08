#!/usr/bin/python3

import sys
import os
import getpass
import json
import yang
import netconf2 as nc

def interactive_auth(name, instruct, prompt, data):
	print(name)
	return getpass.getpass(prompt)

def password_auth(user, host, data):
	return getpass.getpass((user if user else os.getlogin()) + '@' + host + ' password : ')

def hostkey_check(hostname, state, keytype, hexa, priv):
	return True

#
# get know where to connect
#
host = input("hostname: ")
try:
	port = int(input("port    : "))
except:
	port = 0;
user = input("username: ")

#
# set SSH settings
#
if user:
	ssh = nc.SSH(username=user)
else:
	ssh = nc.SSH()
ssh.setAuthInteractiveClb(interactive_auth)
ssh.setAuthPasswordClb(password_auth)
ssh.setAuthHostkeyCheckClb(hostkey_check)

#
# create NETCONF session to the server
#
try:
	session = nc.Session(host, port, ssh)
except Exception as e:
	print(e)
	sys.exit(1)


# perform user-rpc and print rpc-reply

rpc = """<get-schema xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
	<identifier>ietf-netconf-monitoring</identifier>
</get-schema>
"""

try:
	data = session.rpcUser(rpc)
except nc.ReplyError as e:
	reply = {'success':False, 'error': []}
	for err in e.args[0]:
		reply['error'].append(json.loads(str(err)))
		print(json.dumps(reply))
		sys.exit(1)

print(data.print_mem(yang.LYD_JSON, yang.LYP_FORMAT | yang.LYP_WITHSIBLINGS))
