#네이버 금융 top 상위종목 10개 가져오기

from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read()
#네이버 주식은 한글깨짐의 문제 발생
content = res.decode('euc-kr','replace').encode('utf-8','replace')
soup = BeautifulSoup(content, "html.parser")

top10 = soup.select("#siselist_tab_0 > tr" )

i =1
for e in top10:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string)
        i += 1
