import re

ip="10-10-10-1 #Ip address"

#to delete comment
ip=re.sub('#.*$','',ip,1)
print(ip)

#To replace - with .

print(re.sub('-','.',ip))

print(re.sub('\D','','1234hello #ser567'))


print(re.sub('\D','','1234hello #ser567',1)) #only first counter


print(re.sub('\D.*$','','1234hello #ser567'))
