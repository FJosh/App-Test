import re
tempdict = {}
mydict = {}
iwscan = open("iwscan", "r").readlines()
KEYWORDS = ['Cell', 'Address:', 'Channel:', 'Frequency:', 'ESSID:', 'Encryption', 'WEP', 'WPA']
counterline = []
counter = 0
cellname = ""
for line in iwscan:
    if re.match('.*Cell.*', line):
        line.split('-')
        if cellname: 
            mydict[cellname] = tempdict
        cellname = line.split('-')[0].strip()
    if re.match('.*Address.*', line):
        line.split(':')
        data = line.split(":")
        ":".join(data[1:])
        tempdict["Address"] = ":".join(data[1:])
    if re.match('.*Channel.*', line):
        line.split(':')
        data = line.split(":")
        ":".join(data[1:])
        tempdict["Channel"] = ":".join(data[1:])   
    if re.match('.*ESSID.*', line):
        line.split(':')
        data = line.split(":")
        ":".join(data[1:])
        tempdict["ESSID"] = ":".join(data[1:])
    if re.match('.*WEP.*', line):
        line.split(':')
        data = line.split(":")
        ":".join(data[1:])
        tempdict["WEP"] = ":".join(data[1:])
    if re.match('.*WPA.*', line):
        line.split(':')
        data = line.split(":")
        ":".join(data[1:])
        tempdict["WPA"] = ":".join(data[1:])
    else:
        data = line.split(":")
    if data[0].strip() in KEYWORDS:
            tempdict[data[0].strip()] = data[1].strip()

import simplejson
print simplejson.dumps(mydict)

                
            
       
        
    
