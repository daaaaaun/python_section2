import pytube
import os
import subprocess

#다운받을 동영상 주소를 입력받어 저장
ytFileName = input("변환할 YouTube 영상 URL을 입력해주세요")
yt = pytube.YouTube(ytFileName)
videos = yt.streams.all()

#video 순번 입력
for i in range(len(videos)) :
    print(i ,',', videos[i] )

cNum = int(input("다운받을 영상의 화질을 선택하세요"))
down_dir = "c:/youtube"
videos[cNum].download(down_dir)

newFileName = input("변환시 MP3 파일명을 입력하세요")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
    ])

print("동영상 다운로드 및 MP3 변환이 완료됐습니다")

#https://www.youtube.com/watch?v=IHNzOHi8sJs&list=PL4QNnZJr8sRNKjKzArmzTBAlNYBDN2h-J
