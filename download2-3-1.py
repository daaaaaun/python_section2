import sys
import io
import urllib.request as req
from urllib.parse import urlparse
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url ="http://www.encar.com"

mem = req.urlopen(url)

#print(type(mem))
#세가지 자료형은 필히 알아두기
#print(type({})) #딕셔너리
#print(type([])) #리스트
#print(type(())) #튜플

#print("geturl",mem.geturl())
#print("status", mem.status) #응답코드 200: 정상, 404: 응답없음, 403, 500: 서버에러
#print("headers", mem.getheaders())
#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) #euc-kr : 오래된 사이트
print(urlparse("http://www.encar.com?test=test")) #따로 import를 해서 사용한다.
