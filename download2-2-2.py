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

#url열어서 읽어온 상태
f= dw.urlopen(imgUrl).read()
f2= dw.urlopen(htmlURL).read()

saveFile1= open(savePath1, 'wb') # w:write, r:read, a:add, b:binary
saveFile1.write(f)
#사용한자원은 close()작업을 통해서 반드시 반납을 해줘야한다.
#close는 with문으로 대체할 수 있다.
saveFile1.close()

#코드의 가독성이 좋아짐, python2.7이상 버전부터 새로나온 문법
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")

#urlretrieve과 urlopen과의 차이점
#urlretrieve :
#다이렉트로 저장
#저장 -> open("r") -> 변수에 할당 -> 파싱 ->저장

#urlopen :
# 변수 할당 -> 파싱 -> 저장
# 메모리 변수에 할당
#중간작업이 필요한경우, 분석이 필요할 경우에 urlopen이 효율적
