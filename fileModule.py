########################
## file and directory
# file_handler = open(filename, mode)
# mode is the same as other program langurage
## read
# method 1
fin = open('./test.txt')
fin.read()
fin.close()

# method 2, class file
fin = file('./test.txt')
fin.read()
fin.close()

## write
fin = open('./test.txt', 'r+')  # r, r+, w, w+, a, a+, b, U
fin.write('hello')
fin.close()

### 文件对象的方法
## help(file)

for i in open('test.txt'):
    print i

str = fin.readline()  # 每次读取一行
list = fin.readlines()  # 读取多行，返回一个列表，每行作为列表的一个元素
fin.next()  # 读取改行，指向下一行

# 用列表来写入多行
fin.writelines(list)

# 移动指针
fin.seek(0, 0)
fin.seek(0, 1)
fin.seek(-1, 2)

# 提交更新
fin.flush()  # 平时写数据需要close才真正写入文件，这个函数可以立刻写入文件
