#for循环,缩进的效果
num=[1, 2, 3, 4, 5]
total=0
for i in num:
    total +=i   
    print("当前循环累加结果：" + str(total))
print("循环累加结果：" + str(total))
#按顺序判断,当第一个条件满足时，后面的条件就不会再判断了
age=38
if age >= 40:
    print("你已经到了该知天命的年纪了！")
elif age >= 18:
    print("你已经成年了，要承担起责任了！")
else:
    print("你还年轻，继续努力吧！")
#字典,前面的name、age、gender是键，value是值，字典里面的键不能重复，值可以重复
person={"name":"张三","age":18,"gender":"男"}
print(person["name"])
print(person["age"])
print(person.keys())
print(person.values())  
#items()方法可以获取字典里面的键值对，返回的是一个列表，列表里面的每一个元素都是一个元组，
# 元组里面有两个元素，第一个元素是键，第二个元素是值
print(person.items())
#items()适合应用到for循环里面
for key,value in person.items():
    print(key + ":" + str(value))