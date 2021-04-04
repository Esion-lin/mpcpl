### graph

用户在graph中定义计算图。该模块的功能体现在用户继承框架实现的图基类。在基类中定义计算和计算结构。然后调用系统实现的图运行和图编译方法得到输出结果。

#### PrivateCell

> class PrivateCell():

PrivateCell是计算图的基类，用户在定义自定义的计算图时需要实现该继承类。

```python
class mycell(PrivateCell):
  def __init__(self,*args,**kargs):
    super(mycell, self).__init__(*args,**kargs)
  ...
```

#### \_\_init\_\_

用户需要实现__init__方法来注册计算操作

```python
def __init__(self,*args,**kargs):
	super(mycell, self).__init__(*args,**kargs)
  self.conv = mind.nn.conv(stride=1,padding=0,shape=(3,3,3))
  self.mul = mind.ops.mul()
  ...
```

在该函数中用户声明了许多计算单元，基类会初始化对应的算子，并完成一部预计算的工作。

#### \_\_call\_\_

用户需要实现\_\_call__方法来定义计算结构，在静态运行模式下，该过程会生成计算图。

```python
def __call__(self,*args,**kargs):
  y = self.conv(kargs["w"],kargs["x"])
  z = self.mul(kargs["w_2"],y)
  ...
```

#### 计算图的递归性

计算图是可递归的，即，一个计算图可以是由几个计算图组成，如果打开框架的开源代码可以发现，所有的nn和ops的算子都是由计算图实现，所以用户可以构建自己的计算图。

```python
class mygraph(PrivateCell):
  def __init__(self,*args,**kargs):
    super(mycell, self).__init__(*args,**kargs)
    self.mycell_1 = mycell(*args,**kargs)
    self.mycell_2 = myops(*args,**kargs)
  def __call__(self,*args,**kargs):
    y = self.mycell_1(kargs["w"],kargs["x"])
  	z = self.mycell_2(kargs["w_2"],y)
```



