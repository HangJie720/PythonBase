# recursion
#!/usr/bin/python
# coding:utf8
import os


def dirList(path):
    fileList = os.listdir(path)
    allFile = []
    for fileName in fileList:
        # allFile.append(dirPath + '/' + fileName) # the same as below
        filePath = os.path.join(path, fileName)
        if os.path.isdir(filePath):
            dirList(filePath)
        allFile.append(filePath)
    return allFile

# os.walk函数
# os.walk 返回一个生成器，每次是一个三元组 [目录, 子目录, 文件]
gen = os.walk('/')
for path, dir, filelist in os.walk('/'):
    for filename in filelist:
        os.path.join(path, filename)
