import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://api.ipify.org"

values = {
    'format' : 'jsonp'
}
print('before', values)
params =  urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 URL", url)

reqData = req.urlopen(url).read().decode('utf-8')
#사이트에서 제공하는 ip 확인가능
print("출력", reqData)
