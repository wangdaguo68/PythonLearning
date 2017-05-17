#爬取豆瓣用户 2017.05.17
import requests
import http.cookiejar as cookielib
import re
import urllib
from bs4 import BeautifulSoup

agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
headers={
    'User-Agent':agent
}
session=requests.session()
session.cookies=cookielib.LWPCookieJar(filename='cookies')

def login():
    #模拟登陆豆瓣首页
    loginUrl = 'https://www.douban.com/accounts/login'
    #post过去的数据
    formData = {
        "redir": "http://movie.douban.com/mine?status=collect",
        "form_email": '18862243277',
        "form_password": 'king665206',
        "login": u'登录'
    }
    #请求地址
    r = requests.post(loginUrl, data=formData, headers=headers)
    login_page=r.text
    '''''获取验证码图片'''
    # 利用bs4获取captcha地址
    soup = BeautifulSoup(login_page,"html.parser")
    captchaAddr = soup.find('img', id='captcha_image')['src']
    # 利用正则表达式获取captcha的ID
    reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captchaID = re.findall(reCaptchaID, login_page)
    # 保存到本地
    urllib.request.urlretrieve(captchaAddr, "captcha.jpg")
    captcha = input('please input the captcha:')
    formData['captcha-solution'] = captcha
    formData['captcha-id'] = captchaID

    r = requests.post(loginUrl, data=formData, headers=headers)
    page = r.text
    print(r.url)
    if r.url=='https://movie.douban.com/mine?status=collect':
        print('登陆成功！')
        print('我看过的电影','-'*60)
        #获取看过的电影
        soup = BeautifulSoup(page,"html.parser")
        result = soup.findAll('li',attrs={"class":"title"})
        #print result
        for item in result:
            print(item.find('a').get_text())
    else:
        print("登陆失败！")

if __name__=='__main__':
    login()