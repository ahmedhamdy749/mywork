#total = 0 
#count = 0 
#while True:
#    inp = input('Enter a number:')
#    if inp == 'done' : break
#    value = float(inp)
#    total = total + value
#    count = count + 1

#average = total / count
#print('average:',average) 





#numlist = list()
#while True : 
    #inp = input('Enter a number:')
   # if inp == 'done' : break
  #  value = float(inp)
 #   numlist.append(value)
#average = sum(numlist) / len(numlist)
#print('average:' , average)      



#mydic = dict()
#mydic['money'] = 12
#mydic['candy'] = 3
#mydic['tissus']= 75
#print(mydic)



#counts = dict()
#names = ['csev','cwen','csev','zqian','cwen']
#for name in names : 
 #   if name not in counts:
  #      counts[name] = 1
   # else:
    #    counts[name] = counts[name]+ 1
#print(counts)  



#stuff = dict()
#print(stuff.get('candy',-1))



#days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
#print(days[2])
#print('hello world')

#import urllib.request , urllib.parse, urllib.error
#fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
   # print(line.decode().strip())
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')

            
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))