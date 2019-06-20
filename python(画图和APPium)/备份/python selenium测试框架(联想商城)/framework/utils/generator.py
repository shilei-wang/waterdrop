# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

import random
#很神奇的类 可以生成各种随机资源，包括地址 电话 email ip
from faker import Factory

class Generator(object):
    def __init__(self):
        self.fake = Factory().create('zh_CN')

    def random_phone_number(self):
        """随机手机号"""
        return self.fake.phone_number()

    def random_name(self):
        """随机姓名"""
        return self.fake.name()

    def random_address(self):
        """随机地址"""
        return self.fake.address()

    def random_email(self):
        """随机email"""
        return self.fake.email()

    def random_ipv4(self):
        """随机IPV4地址"""
        return self.fake.ipv4()

    def random_str(self,min_chars=0, max_chars=8):
        """长度在最大值与最小值之间的随机字符串"""
        return self.fake.pystr(min_chars=min_chars, max_chars=max_chars)

#yield 阻塞 例子
# def create_counter(n):
#     while True:
#         # next调用一次 这里返回一次
#         yield n
#         # 每次这里都会阻塞 知道下一次next的调用
#         n += 1
#
# cnt = create_counter(2)
# print next(cnt) #输出2
# print next(cnt) #输出2

# id_gen = generator.factory_generate_ids(starting_id=0, increment=2)()
# for i in range(5):
#     print(next(id_gen))

    def factory_generate_ids(self,starting_id=1, increment=1):
        """ 返回一个生成器函数，调用这个函数产生生成器，生成递增ID """
        def generate_started_ids():
            val = starting_id
            local_increment = increment
            while True:
                yield val
                val += local_increment
        return generate_started_ids

# choices = ['John', 'Sam', 'Lily', 'Rose']
# choice_gen = generator.factory_choice_generator(choices)()
# for i in range(5):
#     print(next(choice_gen))

    def factory_choice_generator(self,values):
        """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
        def choice_generator():
            my_list = list(values)
            while True:
                #从列表里 random.choice
                yield random.choice(my_list)
        return choice_generator

generator = Generator()