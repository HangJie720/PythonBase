###################################
### 异常处理
# 异常抛出机制，为程序开发人员提供一种在运行时发现错误，
# 进行恢复处理，然后继续执行的能力

# 用try去尝试执行一些代码，如果错误，就抛出异常，
# 异常由except来捕获，并由我们写代码来处理这种异常
try:
    fin = open("abc.txt")
    print hello
    ### your usually process code here
except IOError, msg:
    print "On such file!"
    ### your code to handle this error
except NameError, msg:
    print msg
    ### your code to handle this error
finally:  # 不管上面有没有异常，这个代码块都会被执行
    print 'ok'

# 抛出异常，异常类型要满足python内定义的
if filename == "hello":
    raise TypeError("Nothing!!")
