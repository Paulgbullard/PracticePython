import urllib3
import certifi
http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",ca_certs=certifi.where())

strt = "http://www.youtube.com/watch?v="
lst = ["zMUH99b5iZI","hga8HQFXaDw","VitcSlnBHH8","HmCyc0VN568","5kTn9Jz3na8","qZeQNx_AaK8","3rRT7AsmDvY","eJE2uq43_a8","VQpqj6QS1qQ","qtAZQJ1r6wE","QYs8pzAfxsw","Pu3GAwikwxo","MupHRh0QLfY"]
new_lst = []
for a in lst:
    b = strt + a
    new_lst.append(b)

for a in new_lst:
    r = http.request("GET",a)
    html = r.data.decode('utf-8')

    wordBreak = ['<','>']  
    html = list(html)
    i = 0
    while i < len(html):
        if html[i] in wordBreak:
            html[i] = ' '
        i += 1

    #The block above is just to make the html.split() easier.

    html = ''.join(html)
    html = html.split()
    print(html)
    dataSwitch = False
    dataSwitch2 = False
    numOfViews = ' '
    videoTitle = ' '
    for element in html:
        if element == '/div':
            dataSwitch = False
            dataSwitch2 = False
        if dataSwitch:
            numOfViews += str(element)
        if dataSwitch2:
            videoTitle += str(element)
        if element == 'class="watch-view-count"':
            dataSwitch = True
        if element == 'class="watch-title" dir="ltr" title="':
            dataSwitch2 = True
        

    print (numOfViews + " " + videoTitle)

input("Press enter to exit")
