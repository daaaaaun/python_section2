import sys
import io
import urllib.request as dw

#atom editor에서 한글을 제대로 출력하기 위한것
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20110303_192/eereer3_1299091887664sXsKi_JPEG/Animals_Drawings_Wallpaper_%2818%29.jpg"
htmlURL = "http://google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"
#urlretrieve함수는 매개변수로 경로화 path, 파일명을 받는다.
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
