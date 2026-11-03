#def是定义函数的关键字，函数名称加上括号。
def me():
    return "加油啊，\n你一定会成功的!"
print(me())
def me2(name):
    return "加油啊，" + name + "\n你一定会成功的!"
print(me2("李四"))
#f-string格式化字符串，f-string是Python3.6之后新增的功能，
# f-string可以在字符串里面直接使用变量，变量前面加上f即可。
def me3(name):
    return f"加油啊，{name}\n你一定会成功的!"
print(me3("王五"))
#函数的参数可以有默认值，默认值可以在函数定义的时候指定，如果调用函数的时候没有传入参数，就会使用默认值。
#还可以进行更高级的运算
def num(x):
    return x*2
print(num(5))
#函数可以有多个参数，参数之间用逗号隔开，函数的返回值可以是任意类型的数据，包括列表、字典、元组等。
#函数可以把其他的数据类型都包含进来,组合起来，他们的功能就比较强大.
num2=[1, 2, 3, 4, 5]
def num3(num2):
    total=0
    for i in num2:
        total +=i   
    return total
#写成函数的好处就是后面可以直接调用函数，不用再写一遍代码，减少了代码的重复性，提高了代码的可读性和可维护性。
print(num3(num2))
#函数里面定义的变量是局部变量，函数外面定义的变量是全局变量，局部变量只能在函数里面使用，全局变量可以在函数里面使用，
# 但是不能修改全局变量的值，如果要修改全局变量的值，需要使用global关键字。

#面向对象编程，类是面向对象编程的核心概念，类是对一类事物的抽象，类里面可以包含属性和方法，
# 属性是类的特征，方法是类的行为。
#class Person:：这就是一个“模具”。它规定了“人类”应该有什么特征（比如都有年龄）和什么行为（比如都能算年龄总和）。
class Person:
#init定义了一个初始值
    def __init__(self,age):
#self是类的实例化对象，age是类的参数，age是一个列表，里面存放了多个年龄
#self：代表“这个具体的人本身”（也就是 clac）。你可以把它理解为“我”。
#clac 只是一个“变量名”而已，是你（或者写这段代码的人）自己随便起的一个名字。
#clac可以换成小明、张三、李四、王五等任何名字，只要你在实例化的时候保持一致就行。
        self.age=age    
#self是类的实例化对象，self.age是类的属性，age是类的参数，age是一个列表，里面存放了多个年龄
#第二个方法sum()是计算年龄的总和，第三个方法average()是计算平均年龄，返回的是一个浮点数。
    def sum(self):
        total=0
        for i in self.age:
            total +=i
        return total
    def average(self):
        return self.sum()/ len(self.age)
age=[1, 2, 3, 4, 5]
#实例化类,创建一个Person类的实例，传入年龄参数
clac=Person(age)
#算总和，调用类的方法,调用类的sum()方法，计算年龄的总和，调用类的average()方法，计算平均年龄
print(clac.sum())
#算平均值，调用类的方法
print(clac.average())