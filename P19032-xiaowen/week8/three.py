#!/usr/local/python3/bin/python3
"""
3、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li) 
"""

1.第一个print输出：[[10],[10],[10],[10],[10]]
	原因：[[]] * 5 这个嵌套列表中的列表将基于一个内存地址指针复制出5份指向同一内存地址的列表，所有当其中某一个列表发生变化，其他列表也会花生变化
2.第二个print输出：[[10,20],[10,20],[10,20],[10,20],[10,20]]
	原因：同上
3.第三个print输出：[[10,20],[10,20],[10,20],[10,20],[10,20],30]
	原因：此项添加值并未该更嵌套列表
