from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import request
postData={
    "app": "adv",
    "return": "http://user.qzone.qq.com/",
    "username": "474208445",
    "password": ""
}
req = request.Request("https://user.qzone.qq.com/474208445/infocenter?ptsig=qemkdj3Dvfleqm5rpcHCRk5gJkhcT0STO3vDH-szugA_",postData)
response = urlopen(req)
page=response.read()
soup = BeautifulSoup(page)
print(soup.prettify())