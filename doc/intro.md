### tranner

Python_func -> graph



### placeholder

- name
- ...

placeholder如名字所示用于占位。需要完整的type，shape等，在编译模式中会被下发到C上用于生成图。

### variable

ori-variable：

- enc
- dec
- value
- type
- name

variable（ori-variable）：

- enc
- Dec
- value->placeholder

Constant（ori-variable）:

- enc
- Dec

变量类型有两种（variable，Constant），都由ori-variable继承，其中最大的区别为variable的value可以为placeholder类型。其下发到底层图上是以变量名下发，而Constant以值下发。enc和dec分别对应将具体值转换到域\环上。值得注意的是下发时需要将类型也下发涉及到是否进行过放大操作需要进行的底层协议运行有所区别。

### operator







### network

网络层由底层自动控制。其中需要向上层提供以下接口

- 简单的数据传输

```swift
func trans(from player_name:String, to player_name:String, with data:Json) → Json
```

- 简单的同步操作，所有节点就是否持有label保持同步。

```swift
func syn(on label:String, with players:[String]) → Json
```



#### PrivateCell

```python
class mul(PrivateCell):
    def __init__(self, *args, **kwargs):
        pass
    def __call__(self,...):
        #动态运行模式
    def __infer__(self,...):
        #定义编译模式
```



### cc

node



### 用户调用语言

由于该层级面向用户，所以直接删除本地计算（明文计算）的接口 ，默认为密文计算

```python

class graph(PrivateCell):
  def __init__(self):
    self.mul = mind.ops.mul()
    self.w=mind.variable(name,type,shape)
    self.x=mind.variable(name,type,shape)
  def __call__(self, w, x):
    map([w,x], [self.w, self.x])
    z = wx
    '''z=self.mul(w,z,protocol = "") 	#显式调用'''
  	#对share-base来说，得到[z] ← mul([x],[y])
x = mind.input_cls(player_name:name,label:"x",data:"")	# activate x 
w = mind.input_cls(player_name:name,label:"w",data:"")
z = run(graph, w, x)#编译模式
'''
⥯
g = build(graph)
z = g(w,x)
'''
z = graph(w, x) #动态图模式
z = z.reveal()	#对share-base来说，得到z ← reveal([z])
```



### 运行模式

项目支持两种运行模式

```python
mind.set_mode(GRAPH)
```

- 编译运行模式

  ​	在该模式下用户在执行`build(with net：PrivateCell)`后获得由底层编译后的函数入口。

  - 该模块将PrivateCell内部的所有内容使用运行时(C)展开(具体展开形式为递归的调用PrivateCell的infer函数)，得到一段编译的二进制C程序，

- 动态运行模式

  ​	该模式不涉及到混编的内容，定义函数后，直接递归调用PrivateCell的所有内容得到输出。

### 运行时语言

最终的代码会被转化为运行时语言。

```swift
func input() → Placeholder{
  w = Input("Bob")
  w0 = run(random(0,2**32),"Bob")
  w1 = run(w - w0 mod 2**32,"Bob")
  w = trans(from:"Bob",to:"Emme",with:w0)
  syn(on:w["label"])
  return w
}

```

```python
from .API import *
__all__ = [
    "input_data",
    "input_from_file",
    "input_with_interact",
    "open_var",
    "input_from_func",
    "start_task",
    "set_player_with",
    "load_param_from_tfckpt",
]
'''config.json'''
{
  "player_0":["10.12.187.22:10001","pk0******"],
  "player_1":["10.32.44.17:10001","pk0******"],
  "player_aid":["118.0.12.43:10001","pk0******"],
}
'''player_0'''
w = mindmpc.user.input_data("player_0",[2,3,4])	#激活的 Placeholder 类型
x = mindmpc.user.input_data("player_1",(3,1))		#Placeholder 类型
z = mindmpc.ops.mul(w,x)
mindmpc.user.open_var("player_1", z)
'''player_1'''
w = mindmpc.user.input_data("player_0",(3,1))
x = mindmpc.user.input_data("player_1",[6,8,9])
z = mindmpc.ops.mul(w,x)
ans = mindmpc.user.open_var("player_1", z)			#明文类型
'''player_aid'''
w = mindmpc.user.input_data("player_0",(3,1))
x = mindmpc.user.input_data("player_1",(3,1))
z = mindmpc.ops.mul(w,x)
mindmpc.user.open_var("player_1", z)

class Player:
	'''
	'''
	def start_node(self, node_callback):
		self.node = Node(self.host, self.port, node_callback, self.public_key)
		self.node.start()
		self.on = True
  ...
  
```



```
func 1_out_of_2_OT() → Placeholder{
	#Bob local store a_0,a_1
	#Emme local store a_b
  [x0,x1] = Input("Bob")
  b = Input("Emme")
  d = run(b⊕c,"Emme")
  d = trans(from:"Emme",to:"Bob",with:d)
  x_d⊕x_0
  return w
}
```

