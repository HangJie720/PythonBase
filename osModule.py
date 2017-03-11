#########################
## OS module
## directory operation should import this
import os

os.mkdir('xiaoyi')  # mkdir
os.makedirs('a/b/c', mode=666)  # 创建分级的目录
os.listdir()  # ls 返回当前层所有文件或者文件夹名到一个列表中（不包括子目录）
os.chdir()  # cd
os.getcwd()  # pwd
os.rmdir()  # rm
