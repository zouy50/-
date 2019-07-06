class Bunch(dict):
    ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

t = Bunch(a=1, b=2)
print(t.__dict__)
# print(t.a)

# 1


# a = dict(one=1, two=2)
# print(dir(a))
# print(dir.__doc__)
# # print(a.__dict__.one)
