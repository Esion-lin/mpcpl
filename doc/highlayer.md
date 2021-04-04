## 用户语言

#### mindmpc调用库

```
|-- mindmpc
	|-- io
	|-- nn
	|-- ops
	|-- mplibs
	
	
```

#### 环境设置

- 用户可以提供一个名叫config.toml的配置文件来设置各个参数

```toml
mode="static"
[service]
	[service.A]
	name = "Alice"
	host = "127.0.0.1:9001"
	pk = "pk****"
	[service.B]
	name = "Bob"
	host = "127.0.0.1:9002"
	pk = "pk****"
	[service.C]
	name = "Emme"
	host = "127.0.0.1:9003"
	pk = "pk****"
[mlib]
path = "./lib"

[alias]
#声明角色
data_own = "Alice"
aid_server = "Bob"
players = ["Alice","Bob","Emme"]
```





| 字段         | 描述                          | 子字段                               |
| ------------ | ----------------------------- | ------------------------------------ |
| service      | 所有服务器信息                | service.name                         |
| service.name | 节点服务器信息                | name、host、pk、alias                |
| mode         | 运行模式                      | 无                                   |
| mlib         | mpc库位置                     | path                                 |
| alias        | 为节点设置别名，以供MPC库使用 | data_own、aid_server、players        |
| proto        | 设置协议                      | proto.io、proto.all、proto.arithm... |
| ...          | 预留字段                      | 无                                   |

​	其中proto字段可以定义全部计算调用的协议名，其子字段可以细致到乘法等单一算子。具体字段与mplibs描述的所有字段一致

- 动态模式/静态模式

mindmpc向用户提供了两种运行模式，其中动态模式为动态运行的方式，而静态模式会进行编译优化等工作。除了用户在toml文件中声明`mode`外，用户可以在程序运行时声明。

```python
import mind as md
md.set_mode(md.static)
md.set_mode(md.dynamic)
```

需要注意的是用户在采用不同的运行模式时，在某些API的调用时需要采用不同的调用方法⚠️

#### IO

IO模块向用户提供了输入输出的逻辑，如下给出了最简单的输入输出方法。

```python
from mind import io
x = io.input([10,6])	#输入常数，其中，x为密文类型
y = io.output(x)			#输出到y，其中，y为明文类型
```

上面的声明为隐式的声明形式，在该种声明方式下，用户需要在toml中设置别名项，如上文[事例](#环境设置)中定义了数据由Alice提供。

⚠️静态模式不支持`io.input`这一硬编码输入方式

IO模块提供了更多的选择类型，包括从文本文件输入/从模型文件输入等。



#### 安全

| 攻击模式                           | 描述                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| 来自路由的网络监听                 | 由于构建了可信P2P信道，在该情况下数据完整性和隐私性可以保证  |
| 来自本地端口的监听，数据包次序交换 | 在同步运行模式下由于程序运行数据不不并行，并不会出现安全问题，在异步运行下，会破会协议运行流程，用户成为恶意节点，可以采用恶意威胁设计的MPC协议 |
| 来自内存的攻击及系统内核攻击       | 该情况下节点成为恶意节点，半诚实协议无法在该模式下正确运行。 |

