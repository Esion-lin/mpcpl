'''
## variable
### edit:   Tyan
### remark: Calculations using attribute proxy classes 
'''
class meta_var(type):
    __ignore__ = "class mro new init setattr getattr getattribute"
    __class_attr__ = None
    def __init__(cls, class_name, base, class_attr):
        cls.__class_attr__ = class_attr
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls)
        obj.__init__(*args, **kwargs)
        value = kwargs['value']

        def make_proxy(name):
            def proxy(self, *args):
                new_arg = []
                for ele in args:
                    if isinstance(ele, cls):
                        new_arg.append(ele.value)
                    else:
                        new_arg.append(ele)
                res = getattr(value, name)(*new_arg)
                if isinstance(res, type(value)):
                    tmp = cls(value = res)
                    return tmp
                return res
            return proxy

        ignore = set("__%s__" % n for n in cls.__ignore__.split())
        for name in dir(value):
            if name not in ignore and name not in cls.__class_attr__:
                setattr(cls, name, make_proxy(name))

        return obj
class variable(metaclass=meta_var):
    def __init__(self, *args, **kwargs):
        self._value = kwargs["value"]
        self._ptype = type(self.value)
        if "type" in kwargs:
            self._stype = kwargs["type"]
        pass
    
    @property 
    def ptype(self):
        return self._ptype
    
    @property
    def value(self):
        return self._value



if __name__ == "__main__":
    test = variable(value = [1,2,3])
    test2 = variable(value = [1,2,3])
    print(test + test2)
    for ele in test:
        print(ele)
    test = variable(value = {"asdf","asdfsd"})
