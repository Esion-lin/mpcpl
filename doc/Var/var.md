### Var

var向用户提供变量和变量管理的功能

#### 安全类型

在明文下，计算机语言一般会定义类型，String，Boolean，Int，Float，对于该框架，提供以下的安全类型。

| 类型    | 支持的操作        |
| ------- | ----------------- |
| pstring | 安全访问          |
| pbool   | 安全计算          |
| pint32  | 安全计算          |
| pfloat  | 安全计算          |
| parray  | 安全计算          |
| *pdict* | 安全访问/安全计算 |

#### 变量

用户可以通过调用`mind.variable()`的方式来声明一个变量。

> variable(name:String[,data:Union,with_type:Type,with_shape:Tuple]) -> var:Placeholder

##### *变量名*

变量名是变量非常重要的一个属性，其可以运算后用于数据的重新激活和输出等功能。使用在声明变量时不能对其缺省。

变量与IO在某种程度上紧密结合，大部分情况下用户通过io接口获得一个变量的实例。

⚠︎实际情况下用户很少需要去主动的声明这样的变量，因为在大多数情况下变量的生成由输入函数和计算过程产生。在以下情况中用户需要主动式的声明此类变量。

- 显式的进行类型转换
- 显式的声明变量名
- 检查中间结果

```python
json = input_with_file("./data.json")	#输入{"w":[1,2,3],"x":[1.2,2.2,4.3]}
print(stype(json["x"])) 							#打印变量的明文类型
> <class 'float'>
z = mind.variable("z",with_type=int) 	#定义变量类型
z = json["w"] * json["x"]
gama = json["w"] * json["x"]
rev = io.output_cls(z)
print(rev, rev.name, type(z)，z.log)					#输出重定义变量后的数据
> [1,4,12] z <class 'int'> "float->int"
rev = io.output_cls(gama)
print(rev, rev.name, type(gama))
> [1.2,4.4,12.9] z <class 'float'>		#输出计算结果
y = mind.variable("z",with_type=int,with_shape=(4,))	#检查中间结果
y = json["w"] * json["x"]							#报错
> TypeError("invalid convert")
```

如上述的代码，`gama`是不进行变量声明后的计算结果，而 `z`是做了变量声明后得到的计算结果。而 `y`则在这基础上做了数组形状的检查。`z`由于做了变量转换，会在`log`属性中打印该过程，而`y`由于无法进行转换会报一个转换错误。



### Var-Implement

#### placeholder

**@property**

- **type**
- **name**
- **value**
- **shape**
- **proto**

**@method**

- 

