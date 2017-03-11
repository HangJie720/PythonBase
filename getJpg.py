# !/usr/bin/python
import re
import urllib2


# Get the source code of a website
def getHtml(url):
    print 'Getting html source code...'
    page = urllib2.urlopen(url)
    html = page.read()
    return html


# Open the website and check up the address of images,
# and find the common features to decide the re_rule
def getImageAddrList(html):
    print 'Getting all address of images...'
    rule = r"src=\"(.+\.jpg)\" pic_ext"
    imReg = re.compile(rule)
    imList = re.findall(imReg, html)
    return imList


def getImage(imList):
    print 'Downloading...'
    name = 1;
    for imgurl in imList:
        urllib.urlretrieve(imgurl, '%s.jpg' %name)
        name += 1
    print 'Got ', len(imList), ' images!'


## main
htmlAddr = "http://imgsrc.baidu.com/forum/pic/item/bede9735e5dde711c981db20a0efce1b9f1661d5"
html = getHtml(htmlAddr)
imList = getImageAddrList(html)
getImage(imList)