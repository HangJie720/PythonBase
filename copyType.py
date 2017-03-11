##############################
### memory operation
## 浅拷贝：对引用对象的拷贝（只拷贝父对象）
## 深拷贝：对对象资源的拷贝

a = [1, 2, 3]
b = a  # id(a) == id (b), 同一个标签，相当于引用
a.append(4)  # a = [1, 2, 3, 4], and b also change to = [1, 2, 3, 4]

import copy

a = [1, 2, ['a', 'b']]  # 二元列表
c = copy.copy(a)  # id(c) != id(a)
a.append('d')  # a = [1, 2, ['a', 'b'], 'd'] but c keeps not changed
# 但只属于浅拷贝，只拷贝父对象
# 所以 id(a[0]) == id(c[0])，也就是说对a追加的元素不影响c，
# 但修改a被拷贝的数据后，c的对应数据也会改变，因为拷贝不会改变元素的地址
a[2].append('d')  # will change c, too
a[1] = 3  # will change c, too

# 深拷贝
d = copy.deepcopy(a)  # 全部拷贝，至此恩断义绝，两者各走
# 各的阳关道和独木桥，以后毫无瓜葛

