### mplibs

```
|-- mplibs
	|-- libs
		|-- pond.mp
		|-- ...
	|-- 
	|-- ops
	|-- mplibs
	
```



Mplibs是放置协议开发人员编写的协议库的地方，在mplib下框架向协议编写者提供了一套编写协议的格式规范，在编写协议时用户需要先继承统一的协议类abc_proto。

```python
class my_protocol(abc_pro):
```

在该模块下，框架向协议编写者提供了一套协议友好的编写方式。如下为定义了一个简单的ot协议(Bellare-Micali协议)

```python
def __ot__():
  p = 2**32 - 1						#Zp
  g = random_p(0,p)				#group element
  b = assign(with_player="player_0", console, range(0,1))			#让player_0输入b ∊ Z_2
  x = assign(with_player="player_1", console, type="array", shape = (2,))#让player_1输入x ∊ {Z_p}^2
  c = random_p(0,p)
  with assign(with_player="player_1"):
    k = random_p(p)
    pk = pow(g, k, nodule = p)
    pk0,pk1 = [pk, div(c, pk)] if b == 0 else [div(c, pk), pk]
  	net.send([pk0,pk1,c], from_player = "player_1", to_player = "player_0")
  with assign(with_player="player_0"):
    check(c == mul(pk0,pk1))
    r0,r1 = random_p(p, shape = (2,))
    e0 = ["h":pow(g, r0, p), "s":xor(Hash("sha-2", pow(pk0, r0, p)),x0)]
    e1 = ["h":pow(g, r1, p), "s":xor(Hash("sha-2", pow(pk1, r1, p)),x1)]
    net.send([e0,e1], from_player = "player_0", to_player = "player_1")
  with assign(with_player="player_1"):
    e = e0 if b == 0 else e1
    x = Hash("sha-2", xor(pow(e["h"], k, p),e["s"]))
```

其实现了以下的协议流程

<img src="/Users/esion/Desktop/截屏2021-03-25 下午12.54.50.png" alt="截屏2021-03-25 下午12.54.50" style="zoom:80%;" />



#### 角色

角色是安全多方计算的一个重要内容，其定义了计算各方在协议中的作用，为了上下层统一，在该层级将采用统一的角色名来作为协议指代，以做到独立该层与上层结构。如在上述描述OT的代码中指代的`player_0`和`player_1`就是两个计算节点的声明形式。

| 角色       | 序列表示                                 | 描述     |
| ---------- | ---------------------------------------- | -------- |
| player     | player_0,player_1...player_n             | 计算节点 |
| data_owner | data_owner_0,data_owner_1...data_owner_n | 数据节点 |
| aid_server | aid_server_0,aid_server_1...aid_server_n | 辅助节点 |

协议需要声明参与计算的节点角色。所有mplibs库在载入是都会去检查是否合法声明了角色这一函数，具体声明例子如下。

```python
def roles():
  return {"player_0","player_1","data_owner_0"}
```

通过无下标的角色名来指代所有该类角色，如使用`player`指代`["player_0","player_1"]`

#### 库支持

框架向协议开发者提供了统一的调用库，上面实现OT的代码中出现所有API都是由这个库实现的。其清单列表如下

| 库名   | 作用                     |
| ------ | ------------------------ |
| net    | 进行网络通讯             |
| fifo   | 进行文件读写             |
| crypto | 进行加密解密等密码学操作 |
| arithm | 大部分的算术计算         |
| R2     | 大部分的逻辑计算         |
| random | 取随机操作               |
| Assign | 指派任务运行角色         |

- **net**

该库调用，实现了统一指派网络通讯的功能，具体如下

> net.send(data:Union, from_player:String, to_player:String) -> data:Union

该函数具有带变量传输的功能，在OT的案例代码中，`send([e0,e1], from_player = "player_0", to_player = "player_1")`将两个变量发送给了令一计算方，另一计算方可以在本地直接访问对应的`e0`，`e1`变量。此外如果使用了无下标的角色名则起到了广播的效果。如下如代码

```python
data = {"emm","Bob",{"w":100}}
net.send(data, from_player = "data_owner_0", to_player = "player")
```

实现了将`data`由`data_owner_0`广播给所有计算节点的功能。⚠️实际上上述代码中的情况不会出现，data不会以硬编码的方法被写在协议中

- **assign**

assign实现了指派计算任务的功能。

> assign(with_player:String, fn:function[, *args,**kargs])

其作用是令`with_player`运行`fn`函数。上述OT代码中`b = assign(with_player="player_0", console, range(0,1))	`通过assign实现了令`player_0`运行`console(range(0,1))`，该函数实现从命令行读入范围为`[0,1]`的数，我们可以通过以下的案例代码进一步了解其功能。

```python
data0 = assign(with_player="data_owner_0", random, 0, 100， shape = (3,3))#令data_owner_0执行data0 = random(0,100,shape = (3,3))
data = assign(with_player="data_owner_0", fifo.csv, "./data.csv", "r")
def share(a,b,N):
  return arithm.mod(a-b,N)
data3 = assign(with_player="data_owner_0", share, data, data0, 2**32)
net.send(data0, from_player = "data_owner_0", to_player = "player_0")
net.send(data1, from_player = "data_owner_0", to_player = "player_1")
```

上述的代码表示了data_owner_0进行一次秘密分享的过程。显然可以通过打包函数的方法来简化该流程

```python
def share(N):
  data0 = random(0,2**32,shape = (3,3))
  data1 = arithm.mod(fifo.csv("./data.csv", "r") - data0, N)
	return [data0, data1]
data0, data1 = assign(with_player="data_owner_0", share, 2**32)
net.send(data0, from_player = "data_owner_0", to_player = "player_0")
net.send(data1, from_player = "data_owner_0", to_player = "player_1")
```

*使用with语句*

用户也可以采用with来简化操作，上述OT代码中`with assign(with_player="player_0")`就采用了这种方法来让`player_0`运行一段代码块。下面的代码采用这种方法实现了上面的秘密分享的过程。

```python
with assign(with_player="data_owner_0"):
	data0 = random(0,2**32,shape = (3,3))
	data1 = arithm.mod(fifo.csv("./data.csv", "r") - data0, N)
net.send(data0, from_player = "data_owner_0", to_player = "player_0")
net.send(data1, from_player = "data_owner_0", to_player = "player_1")
```

- **crypto**

crypto 提供常规的加密函数等密码学操作。上述OT案例中`Hash("sha-2", pow(pk0, r0, p))`采用sha-2作为Hash算法计算了`pow(pk0, r0, p)`的结果

| 函数   | 说明                                   | 选项                                    |
| ------ | -------------------------------------- | --------------------------------------- |
| hash   | 哈希函数                               | hash(type:String,data:String)           |
| Enc    | 加密函数                               | Enc(type:String,key:String,data:String) |
| KeyGen | 密钥生成函数                           | KeyGen(type:String,data:String)         |
| Dec    | 解密函数                               | Dec(type:String,key:String,data:String) |
| ...    | 其他预留函数，供未来实现签名等函数使用 |                                         |

- **fifo**

使用fifo库进行文件读写等功能。在上述OT的例子中`console(range(0,1))`和`console(type="array",shape = (2,))`就是该库中的函数，前者实现了从命令行读入0或1后者读入一个形状是`(2,1)`的数组。

| 函数    | 描述         | 选项                          |
| ------- | ------------ | ----------------------------- |
| csv     | 读写数组     | csv(path:String, mod:String)  |
| Json    | 读写字典     | json(path:String, mod:String) |
| seed    | 读写随机种子 | seed(path:String, mod:String) |
| console | 从命令行读入 | console(type:String, **kargs) |
| Output  | 输出到命令行 | output(data:Union)            |

- **arithm**/**R2**

arithm和R2是一些计算接口，如加减乘除，移位异或按位与等

- **random**

random的实现较为复杂，由于其分为两种情况一种是运行在assign下，另一种是运行在public的情况下，即所有计算方共同运行，在该情况下需要进行seed的访问，在该情况下，在该函数的底层采用了fifo的seed和net的通信功能进行seed的管理。其按生成的限制分为random和random_p两个函数，前者没有限制，后者生成的为质数以支持域上的操作。如OT代码中`random_p(p, shape = (2,))`生成了范围为`(0,p)`的形状为`(2，1)`的随机矩阵。



#### 节点与图

节点与图并不向用户暴露，而是实现库文件的具体方案，所有的库文件的实现都是基于数据节点和计算节点实现，如下图定义了简单的乘法调用时库的实现图。W和X、Y是数据节点，而Mul是计算节点。节点是整个框架真正基础的结构，其支持生成描述的编译模式和动态运行，由其向上构建协议再由协议向上构建计算任务。

<img src="/Users/esion/Desktop/截屏2021-03-26 上午9.52.33.png" alt="截屏2021-03-26 上午9.52.33" style="zoom:50%;" />

由于在mplibs中所有的代码均是掉用库函数实现，整个协议文件可以直接编译为更大的类似上图的计算图。