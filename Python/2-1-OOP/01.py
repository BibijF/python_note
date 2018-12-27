"""
定义一个学生类，用来形容学生
"""


class Student:
    # 一个空类，pass代表直接跳过
    # 空类必须有pass
    pass


# 定义一个对象
mingyue = Student()


# 定义一个类，用来描述听Python的学生
class PythonStudent:
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    # 注意：
    # 1. def doHomework的缩进层级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print('I am doing homework')

        # 推荐在函l数末尾使用return语句
        return None


# 实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递参数
yueyue.doHomework()
