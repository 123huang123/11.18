from functools import  reduce

x=input("请输入数字：")#输入你想输入的数字，用空格间隔输入完毕按enter,会自动形成列表

def prod(x):
    list=x.split(" ")
    intlist=[int(i) for i in list]
    sum = reduce(lambda x, y: x * y, intlist)
    return sum

#接收数字并转化为列表
sum=prod(x)

print ("列表{0}的乘积是{1}".format([int(i) for i in x.split(" ")],sum))
