### input_cls

> Input_cls(data:json[,with_player:String] ) → var:dict

使用硬编码的方式输入数据。各方的代码可以不一致，输入方会将输入以硬编码的方式输入到该函数中。其他方对应的需要显式的声明对应各个label的形状。

**args**

- *data*：数据内容
  - Json格式：{变量名:[变量形状，类型]}
- *with_player*：输入方，缺省值从config文件获取

**return**

- *var*：返回字典类型，其形式为{变量名：变量}

如下的代码为简单的输入

```python
x = input_cls({"a":[1,2,3]},with_player="Tyan") #Tyan's code
print(x["a"])
> {'a': <__placeholder__>.a}
''''''
x = input_cls({"a":[(3,),Int]},with_player="Tyan") #other's code
print(x["a"])
> {'a': <__placeholder__>.a}
```

-------



### input_with_file

> Input_with_file(path<type: Int,shape: tuple>:String[,with_player:String] ) → var:dict

读取文本文件的输入

**args**

- *path*：数据路径，在数据包中需要提供以下的两部分描述，可缺省
  - *type*：输入类型，在动态模式下允许缺省
  - *shape*：输入的形状，其中为数值时采用None表示，在动态模式下允许缺省
- *with_player*：输入方，缺省值从config文件获取

**return**

- *var*：返回字典类型，其形式为{变量名：变量}

⚠️对于静态运行模式来说路径的输入为链接方式，在程序运行到`Input_with_file("./data.json")`时只会检查文件是否存在，真正对文件进行load的操作在运行时进行。

👋框架虽然提供了动态运行时检查缺省值的方法，但建议采用显式声明的方法以提高安全性。

----

### input_map

> Input_map(path:String[,with_player:String,type:Int,shape:tuple]) → fn:callback

这是为大数据情况设计的接口，实现了延迟load的方法，返回的不是实际的变量，而是获得变量的函数，其与input函数在使用上没有明显的区别。

**return**

- *fn*：返回一个回调函数`fn("name")`，通过`fn("a")`来起到与之前`var["a"]`类似的效果。

----

### set_proto

> set_proto(name:String)

用户需要显式的声明io使用的协议。框架会对应在mplibs下搜索该协议，具体描述请参考[libs](../Libs/libs.md)



