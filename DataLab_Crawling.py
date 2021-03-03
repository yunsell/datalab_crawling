import requests
import sys
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('span.item_title')
i=1
for item in data:
    print(str(i)+"위: "+item.get_text())
    i+=1
i=1
sys.stdout = open("Result_crawling.txt","w")
for item in data:
    print(str(i)+"위: "+item.get_text())
    i+=1
sys.stdout.close()