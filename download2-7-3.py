#rmse#네이버 금융 top 상위종목 10개 가져오기

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base = "https://www.inflearn.com/"
#url에 한글정보를 전달하면 인코딩해주는 함수 qoute_plus
#url 형식을 한글 -> Unicode에 맞는 형식으로 변환
quote = rep.quote_plus("추천-강좌")
#print(quote)

url = base + quote
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print(soup)

recommand = soup.select("ul.slides")[0]
for i,e in enumerate(recommand,1):
    print(i,e.select_one("h4.block_title > a").string)

#스크래핑 시 중간중간 본인이 엘리먼트를 정확하게 가지고 왔는지 확인하기 위해
#print 함수 찍어볼것
