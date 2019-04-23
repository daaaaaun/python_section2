import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

banner1 ="https://ssl.pstatic.net/tveta/libs/1223/1223602/1979fc69ba8deb1d0985_20190311161002960.jpg"
banner2 = "https://ssl.pstatic.net/tveta/libs/1230/1230617/a76228e6e7a8e7d71268_20190311112256309.jpg"

savePath1 = "c:/banner1.jpg"
savePath2 = "c:/banner2.jpg"

f = req.urlopen(banner1).read()
f2 = req.urlopen(banner2).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("배너 저장 완료^0^")
