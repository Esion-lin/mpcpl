### NN

nn是更为上层的API，与OPS不同的是，其图更复杂，其实现了机器学习等高级的计算接口。

> Conv(stride:Int,padding:Int, shape:Tuple) → fn:function

如上给出了卷积的API，下面给出了部分该层级的算子。

| 算子名  | 选项                                 | 说明           |
| ------- | ------------------------------------ | -------------- |
| Conv2d  | stride:Int, padding:Int, shape:Tuple | 实现了卷积     |
| Relu    |                                      | 实现了Relu     |
| AvgPool | shape:Tuple                          | 实现了平均池化 |
| MaxPool | Shape:Tuple                          | 实现了最大池话 |
| Dense   | Shape:Tuple                          | 实现了全连接   |
| ...     |                                      |                |

由于机器学习的算子众多，其实现各异，这里不再一一列举。

