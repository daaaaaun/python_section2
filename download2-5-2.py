from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""


soup = BeautifulSoup(html, 'html.parser')
#print('prettify', soup.prettify())

h1 = soup.html.body.h1
print('h1', h1)
#print(h1.string)
p1 = soup.html.body.p
print('p1', p1)
#태그가 줄바꿈이 되어 있으면 공백으로 인식해서 빈칸이 출력된다.
#따라서 enter를 했으면 next_sibling을 두번 쳐야 한다.
p2 = p1.next_sibling.next_sibling
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >>" , h1.string)
print("h1 >>" , p1.string)
print("h1 >>" , p2.string)
