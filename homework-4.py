#다음 실시간 검색어 10개 출력해서 가지고 오기
#링크정보도 가지고 오기..!!! -> 인기검색어에 연동되는

from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url ="https://www.daum.net"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

realtime = soup.select_one("ol.list_hotissue.issue_row").find_all("a", tabindex="-1")

for i, e in enumerate(realtime,1):
    print(i,"인기검색어",":", e.string,  "link", ":", e.attrs['href'])
    i += 1
