### ops

ops是由PrivateCell构建的基本计算算子。其包括了算术电路的基本操作，以及一些逻辑判断，流程控制等的算子。

#### 算术操作

​	算术操作实现了例如以下的API。

> Mul(shape:tuple) → fn:function

​	Mul初始化一个乘法算子，在需要预计算的场合需要提供乘法的形状。所有的算子初始化后都会返回一个callable的入口。

| 算子名 | 选项                      | 说明                                     |
| ------ | ------------------------- | ---------------------------------------- |
| Mul    | Shape:Tuple               | 实现了乘法                               |
| Div    | Shape:Tuple               | 实现了除法                               |
| MatMul | ShapeA:Tuple,ShapeB:Tuple | 实现了矩阵乘法                           |
| Add    | Shape:Tuple               | 实现了加法                               |
| Sub    | Shape:Tuple               | 实现了减法                               |
| Pow    | Developing                | 计算复杂度大于多项式的算子需要进一步开发 |
| ...    |                           |                                          |

#### 逻辑运算

​	逻辑操作实现了例如以下的API。

> Shift(shape:tuple) → fn:function



| 算子名 | 选项        | 说明                   |
| ------ | ----------- | ---------------------- |
| lShift | Shape:Tuple | 实现了算术左移         |
| rShift | Shape:Tuple | 实现了算术右移         |
| And    | Shape:Tuple | 实现了与门             |
| Xor    | Shape:Tuple | 实现了异或             |
| Or     | Shape:Tuple | 实现了或门             |
| Eq     | Shape:Tuple | 实现了判断值相等的操作 |
| Ge     | Shape:Tuple | 实现了判断值大于的操作 |
| ...    |             |                        |

#### 访问控制

​	在该层级下，框架设计实现了一些常规访问控制使用的函数，如

> Reshape(new_shape:tuple) → fn:function

对数组进行了reshape的操作，访问控制的API大多只进行明文的index访问进行密态访问时需要进行的工作要复杂的多，如下表中的Index算子就进行了密态访问。在该模块下有更复杂的API留待下一步的开发，如集合求交（*Private* Set Intersection——PSI）等。

| 算子名  | 选项                              | 说明                  |
| ------- | --------------------------------- | --------------------- |
| Reshape | new_shape:Tuple                   | 实现了对数组的reshape |
| Index   | Idx:Placeholder                   | 实现了密态访问操作    |
| index   | Idx:tuple                         | 实现了访问操作        |
| Append  | Var:Placeholder,Var2:Placeholder  | 实现了添加操作        |
| stack   | Var1:Placeholder,Var2:Placeholder | 实现了合并的操作      |
| ...     |                                   |                       |

#### 