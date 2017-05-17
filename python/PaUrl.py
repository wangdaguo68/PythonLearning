# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc)
# print(soup.prettify())
import re
import os
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import tool
class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()
    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        req = request.Request(url)
        response = urlopen(req)
        return response.read().decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        # soup = BeautifulSoup(page)
        # print(soup.prettify())
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents
    # 获取MM个人详情页面
    def getDetailPage(self, infoURL):
        url="https:"+infoURL
        print(url)
        response = urlopen(url)
        return response.read().decode('gbk')

    # 获取个人文字简介
    def getBrief(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        result = re.search(pattern, page)
        if result is None:
            pass
        else:
            return self.tool.replace(result.group(1))

    # 获取页面所有图片
    def getAllImg(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        # 个人信息页面所有代码
        content = re.search(pattern, page)
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        if content is None :
            images=None
        else:
            images = re.findall(patternImg, content.group(1))
        return images

    # 保存多张写真图片
    def saveImgs(self, images, name):
        number = 1
        #print (u"发现", name, u"共有", len(images), u"张照片")
        if images is None:
            pass
        else:
            for imageURL in images:
                splitPath = imageURL.split('.')
                fTail = splitPath.pop()
                if len(fTail) > 3:
                    fTail = "jpg"
                fileName = name + "/" + str(number) + "." + fTail
                self.saveImg(imageURL, fileName)
                number += 1

    # 保存头像
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL, fileName)

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print(u"正在偷偷保存她的个人信息为", fileName)
        if content is None:
            pass
        else:
            f.write(content)

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urlopen('http:'+imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"正在悄悄保存她的一张图片为", fileName)
        f.close()

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print(u"偷偷新建了名字叫做", path, u'的文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(u"名为", path, '的文件夹已经创建成功')
            return False

    # 将一页淘宝MM的信息保存起来
    def savePageInfo(self, pageIndex):
        # 获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        print(contents)
        for item in contents:
            # item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print(u"发现一位模特,名字叫", item[2], u"芳龄", item[3], u",她在", item[4])
            print(u"正在偷偷地保存", item[2], "的信息")
            print(u"又意外地发现她的个人地址是", item[0])
            # 个人详情页面的URL
            detailURL = item[0]
            # 得到个人详情页面代码
            detailPage = self.getDetailPage(detailURL)
            # 获取个人简介
            brief = self.getBrief(detailPage)
            # 获取所有图片列表
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            # 保存个人简介
            self.saveBrief(brief, item[2])
            # 保存头像
            self.saveIcon(item[1], item[2])
            # 保存图片
            self.saveImgs(images, item[2])

    # 传入起止页码，获取MM图片
    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print(u"正在偷偷寻找第", i, u"个地方，看看MM们在不在")
            self.savePageInfo(i)

spider = Spider()
spider.savePagesInfo(2,10)