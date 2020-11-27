import xml.etree.ElementTree as ET
f=ET.parse('etc/hadoop/core-site.xml')
r=f.getroot()
print(r)
x=ET.SubElement(r,'property')
n=ET.SubElement(x,'name')
n.text='fs.default.name'
ip=input('Enter Your Master IP Address')
port=input('Enter Your Master Port No.')
v=ET.SubElement(x,'value')
v.text='hdfs://{0}:{1}'.format(ip,port)
f.write('etc/hadoop/core-site.xml')

 
   
