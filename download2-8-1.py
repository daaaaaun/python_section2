from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base ="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("연예인")
url = base+quote

res = req.urlopen(url)
savePath = "C:\\imagedown\\" #C:\imagedown\

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img"
for i, img_list in enumerate(img_list, 1):
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+ '.jpg')
# user-agent -> 브라우저 이용으로 요청했을때..!
    req.urlretrieve(img_list['data-source'], fullFileName)
print("다운로드완료!")
