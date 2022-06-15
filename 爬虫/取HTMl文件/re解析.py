#!/usr/bin/python
import requests
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
for i in range(1,32):
    url='https://cnstatic01.e.vhall.com/document/84a088d056b41a94be469bd96065e961/'+str(i)+'.jpg'
    re=requests.get(url,headers=headers)
    print(re.status_code)
    path= str(i)+'.jpg'
    with open(path, 'wb') as f:
        for chunk in re.iter_content(chunk_size=128):
            f.write(chunk)