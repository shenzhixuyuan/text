#变量的命名规则里面不能有空格，不能是数字开头，不能是关键字，不能包含特殊字符，不能使用中文命名
greet="您好，吃了么，"
greet_chinese=greet
greet_english="Hello, have you eaten?"
greet=greet_english
print(greet+"张三")
print(greet+"李四")
print(greet_chinese+"王五")
#type()函数可以查看变量的类型，int 表示整数，float表示浮点数，str表示字符串
print(type(greet))
print(type(3))
print(type(3.1415926))
if 3<= 3.1415926:
    print("张三和李四是同一个人")
is_name=True
print(type(is_name))
#[]表示列表，列表里面可以存放不同类型的数据，
print("3.1415926"[6])
friends=["张三","李四","王五"]
friends.append("赵六")  
friends[2] = "王五五"
print(friends[0])
#friends.tuple=("张三","李四","王五")  #元组，元组里面的数据不能修改
#print(friends.tuple[0])
#for循环可以遍历列表里面的每一个元素
for dd in friends:
    print(dd)
#range()函数可以生成一个整数序列，默认从0开始，步长为1
for i in range(0,10):
    print(i)