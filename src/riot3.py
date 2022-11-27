
import urllib
from urllib import parse
from urllib.request import urlopen

from bs4 import BeautifulSoup



def riot():
    headers = {'User-Agent': "Mozilla/5.0"}
    domain = 'https://fow.kr/find/'
    query_string = '마틴마틴마틴마틴'
    parser = "lxml"
    class_names = "recent_td"
    tag_name = "td"
    req = urllib.request.Request(domain+ parse.quote(query_string), headers=headers)  # parse.quote() 한글 가능
    soup = BeautifulSoup(urlopen(req), parser)
    title = {"class": class_names}
    titles = soup.find_all(name=tag_name, attrs=title)
    titles = [i.find('a')['href'] for i in titles if i.find('a') is not None ]
    for i in titles:
        print(f"https://fow.kr/{i}")

    import subprocess
    subprocess.call(r'C:\Users\min\Code\riot-project\static\data\test.bat')
riot()

"""
def query_string():
    headers = {'User-Agent': "Mozilla/5.0"}
    domain = 'https://fow.kr/'
    query_string = 'ranking'
    parser = "lxml"
    id_names = "r_out"
    tag_name = "tbody"
    req = urllib.request.Request(domain+query_string,headers=headers) # parse.quote() 한글 가능
    soup = BeautifulSoup(urlopen(req), parser)
    title = {"id": id_names}
    titles = soup.find_all(name=tag_name, attrs=title)
    print(titles)
    titles = [i.find('a')['href'] for i in titles if i.find('a') is not None]
    print(soup)
query_string()



from inspect import getfile
import os
import re
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
overlap = []
url = "https://fow.kr/find/hide+on+bush"
site = "https://fow.kr"
rec = "/home/orah010/usedOpenRead.do;"
dl = "/spec_down.php?ip=replay.fow.kr:8088&key="
def get_download(url, fname, directory):
    try:
        os.chdir(directory)
        request.urlretrieve(url, fname)
        print('다운로드 완료\n')
    except HTTPError as e:
        print('error')
        return
def downSearch(getDLATag, filename):
   for getDLLink in getDLATag:
       try:
           if dl in getDLLink.get('href'):
               accessDLUrl = site + getDLLink.get('href')
               print("다운로드 링크: ", accessDLUrl)
               path = "C:\\ORS\\국내인증실적"
               if os.path.isfile(path + filename):
                   print("다운로드 실패 : 동일 파일 존재\n")
               else:
                   get_download(accessDLUrl, filename, path)
       except:
           pass
def Search(getA, num):
    for getLink in getA:
        data = getLink.get('href')
        try:
            if rec in getLink.get("href"):
                if data not in overlap:
                    overlap.append(data)
                    accessUrl = site + getLink.get("href")
                    r = requests.get(accessUrl)
                    soup = BeautifulSoup(r.text, "html.parser")
                    getDLATag = soup.find_all("a")
                    getfilenameTag = soup.find_all("td")
                    td = getfilenameTag[len(getfilenameTag)-1]
                    filename = str(num) + ". " + str(td)[4:int(str(td).find(".pdf"))+4].strip()
                    #print(filename)
                    num = num - 1
                    downSearch(getDLATag, filename)
        except:
            pass
def main():
    pageoffset = 0
    num = 627
    while pageoffset <= 620:
        # request 모듈을 사용하여 웹 페이지의 내용을 가져온다
        r = requests.get(url+str(pageoffset))
        # beautiful soup 초기화
        soup = BeautifulSoup(r.text, "html.parser")
        # 태그로 찾기 (모든 항목)
        getA = soup.find_all("a")
        Search(getA, num)
        pageoffset += 10
        num -= 10
main()



"""

