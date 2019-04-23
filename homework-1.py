import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

banner1 ="https://ssl.pstatic.net/tveta/libs/1223/1223602/1979fc69ba8deb1d0985_20190311161002960.jpg"
banner2 = "https://ssl.pstatic.net/tveta/libs/1230/1230617/a76228e6e7a8e7d71268_20190311112256309.jpg"

savePath1 = "c:/banner1.jpg"
savePath2 = "c:/banner2.jpg"

req.urlretrieve(banner1,savePath1)
req.urlretrieve(banner2, savePath2)

print("배너 저장 완료^0^")
