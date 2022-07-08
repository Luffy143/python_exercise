# 作者: XWX
# 2022年06月15日21时32分18秒
class A:
    def __init__(self,name):
        self.name=name

class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

a=A('Tom')
b=B('Trump',23)
print(b.name)