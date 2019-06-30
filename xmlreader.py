import xml.etree.ElementTree as ET

fo=open("sysinfor.xml")
sys_info=ET.fromstring(fo.read())
print(sys_info)
system=sys_info.findall('sys')
print(system)

for record in system:
    print(record.find('name').text)
    print(record.find('ip').text)
    print(record.find('port').text)
    print("{}----{}".format(record.get('id'), record.find('ip').text))
fo.close()
