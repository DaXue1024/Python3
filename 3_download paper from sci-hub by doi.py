import urllib.request
import re
import os
#https://pubs.acs.org/doi/pdf/10.1021/jacs.9b09236

log = open('download.log', 'a')
list1 = []
f = open('3_list.txt','r')
fw = open('unfind_sci-hub.txt','w')
for line in f:
    list1.append(line.strip())
for i in list1:
    url = 'https://sci-hub.se/'+ i.strip()
#	print url
    source = urllib.request.urlopen(url).read().decode('utf-8')
    try:
        id = re.findall('src="\/.*FitH',source)
        name = id[0].replace('//','/').replace('src="/','')
        if name.split('/')[0] == 'downloads':
            link = 'https://sci-hub.se/'+ name
            print (link)
        else:
            link = 'https://' + name
         #   print (link)
         #   print (link)
        cmd = 'wget ' + link 
        #os.system(cmd)
    except IndexError:
        fw.write(i + '\n')
