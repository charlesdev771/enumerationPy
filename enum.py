import socket 
domain = 'bancocn.com'
names = ['ns1', 'ns2', 'www', 'ftp', 'intranet']

for name in names:
	dns = name + '.' + domain
	try:
		print dns + ": " + socket.gethostbyname(dns)
	except socket.gaierror:
		pass
