import urllib.request, urllib.parse, urllib.error
import json
link = input('Enter location:')
html = urllib.request.urlopen(link).read().decode()
print('Retrieved',len(html),'characters')
try:
    js = json.loads(html)
except:
    js = None
cn = 0
sm = 0
for item in js['comments']:
    cn +=1
    sm += int(item['count'])
print('count:', cn)
print('sum:', sm)           