'''
打印小猫爱吃鱼,小猫要喝水
小猫是一个类,爱吃鱼是一个方法,喝水是一个方法
'''
class Cat():
    def drink_water(self):
        print('小猫喝水')
    def eat_fish(self):
        print('小猫吃鱼')
cat1=Cat()#创建对象
cat1.drink_water()#cat1对象调用实例方法
cat1.eat_fish()#cat1对象调用实例方法

'''
小明和小美是一个类的两个对象,跑步和吃东西是两个方法,体重属性
每次跑步会减肥0.5公斤
每次吃东西体重会增加1公斤
'''


class people():
    def __init__(self, weight):
        self.weight = weight
        self.new_weight=weight
    def __str__(self):
        return f'体重是{self.weight}'
    def run(self,n):
        self.new_weight=self.new_weight-n
        print(f'跑步{n}后体重是{self.new_weight}')
    def eat(self,m):
        self.new_weight=self.new_weight+m
        print(f'吃饭{m}次后体重是{self.new_weight}')

xiaomei = people(75.0)
xiaoming = people(45.0)
print(xiaoming)
xiaoming.run(2)
xiaoming.eat(2)
print(xiaomei)
xiaomei.run(2)
xiaomei.eat(1)

'''
需要定义两个类,一个是房子类,一个是家具类, 房子的属性有:户型和总面积,和家具列表
家具的属性名字和占地面积,床,衣柜和餐桌是家具类的对象,
摆放家具是一个方法
'''
class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
class Home():
    def __init__(self,type,area):
        self.type=type#户型
        self.a=area#房屋面积
        self.left=area#剩余面积,剩余面积和房屋面积最开始是一样的,
        self.furniture=[]#家具列表
    def __str__(self):
        return f'房子的户型是{self.type},房子的总面积是{self.a},房子的剩余面积是{self.left},家具名称列表是{self.furniture}'

    def add_furniture(self,item):
        if self.left>item.area:
            self.furniture.append(item.name)
            self.left=self.left-item.area
home=Home('两室一厅',100)#创建对象
bed=Furniture('床',4)#创建床这个对象
home.add_furniture(bed)#家这个对象调用添加家具的实例方法
cabinet=Furniture('衣柜',2)#创建衣柜这个对象
home.add_furniture(cabinet)#家这个对象调用添加家具的实例方法
table=Furniture('餐桌',1.5)
home.add_furniture(table)
print(home)
'''
士兵是一个类,抢是一个类, 瑞恩是士兵的一个对象,AK47是手枪的一个对象,
士兵可以开火开火就是一个方法,枪可以发射子弹,发射子弹就是一个方法,枪可以填装子弹,填装子弹也是一个方法
'''
class Soldier():
    def fire(self):
        print('开火')
class Gun():
    def fire_bullet(self):
        print('发射子弹')
    def add_bullet(self):
        print('增加子弹')

ryan=Soldier()
AK47=Gun()
AK47.add_bullet()
AK47.fire_bullet()
ryan.fire()
