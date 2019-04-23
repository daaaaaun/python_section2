from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
#http://test.com/html/a.html/b.html 주소가 이상한걸 알기때문에 a.html을
#삭제라고 뒤에 b.html을 붙인다.
#urljoin을
print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/img.css"))
