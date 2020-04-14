from urllib import request
from urllib import parse
import re
import webbrowser
from fake_useragent import UserAgent
import requests
import time
import submit
Page = 1
ua = UserAgent()
myheaders = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'User-Agent': ua.random}
target = 'https://blog.csdn.net/caowenbo2311694605/article/list/'+Page.__str__();
for i in range(0, 10):
    try:
        List_get = requests.get(url = target , headers = myheaders , timeout  = 3 );
    except requests.exceptions.RequestException:
        print("getsotimeout")
        continue
    break
List_html = List_get.content.decode('utf8');
#print(List_html)
# f = open("out.html","w+")
# print(List_html,file= f)
# webbrowser.open(url = "./out.html")
#patternCode = r'<code class="language-cpp">([\s\S.]*?)</code>'
pattern = re.compile(r'https://blog.csdn.net/caowenbo2311694605/article/details/[^\s\?"]*')

Resulturl = pattern.findall(List_html)
Resulturl = list(set(Resulturl))
for cururl in Resulturl:
    print(cururl)
    for i in range(0, 10):
        try:
            article_get =requests.get(url = cururl, headers  = myheaders, timeout = 3)
        except requests.exceptions.RequestException:
            print("getsotimeout")
            continue
        break
    article_html = article_get.content.decode('utf8')
    patternContent = re.compile(r'<div class="htmledit_views" id="content_views">([\s\S.]*?)</div>')
    resultContentList = patternContent.findall(article_html)
    patternTitle = re.compile(r'var articleTitle = "([\s\S.]*?)";')
    resultTitleList  = patternTitle.findall(article_html)
    print(resultTitleList) ;
    patternTime =  re.compile(r'"pubDate":"([\s\S.]*?)T')
    resultTimeList = patternTime.findall(article_html)
    print(resultTimeList)
    if len(resultContentList)==0 or len(resultTitleList)==0 or patternTime == 0:
        continue
    resultContent= resultContentList[0].replace('\n\n','')
    # print(resultContent)
    # f = open("out.html", "w+")
    # print(resultContent,file=f)
    # webbrowser.open(url="./out.html")
    # time.sleep(1)
    submit.Ssubmit(resultTitleList[0], resultContent,resultTimeList[0]);