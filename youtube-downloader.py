import pytube
import os
import subprocess #파이썬을 실행하면서 별도의 프로세스를 실행해서 커맨드 환경을 실행

#다운받을 동영상
yt = pytube.YouTube("https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG")
videos = yt.streams.all()

#print('videos', videos)
for i in range(len(videos)) : #range(5) 1,2,3,4
    print(i, ',', videos[i])

cNum = int(input("다운 받을 화질은? (0~21 입력)"))
down_dir = "c:/youtube"
videos[cNum].download(down_dir)

newFileName = input("변환할 때 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])
print("동영상 다운로드 및 MP3 변환완료")
