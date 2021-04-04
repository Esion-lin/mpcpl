### 运行实例

#### 定义计算网络

```python
from mind import PrivateCell
from mind import io
class comp_graph(PrivateCell):
  def __init__(self):
    super(comp_graph, self).__init__(**kwargs)
  def __call__(self,input_var):
    ''''''
    return input_var 
  def __back__(self):
    '''...'''

#动态运行
x = io.input([1,2,3])
net = comp_graph()
o = net(x)

#静态运行
#postpossing
from mind.compiler import build,run
x = io.input_from_file("./data.json")
o = run(comp_graph, x)
#prepossing
from mind.compiler import build,run
net = build(comp_graph)
x = io.input_from_file("./data.json")
z = run(net, x)

```

