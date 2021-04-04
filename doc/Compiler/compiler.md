### compiler

compiler向用户提供了一套静态运行的模式，目前的主流MPC框架都采用了此类的模式，在该模块用户将定义的计算任务交由编译函数进行优化和编码，得到运行图入口，然后进行调用得到输出结果。

模块只向用户提供两类接口：

> run(graph:PrivateCell, *args, **kargs) → var:Placeholder

> build(graph:PrivateCell) → fn:class

实际上在PrivateCell底层实现了\_\_run__和\_\_build\_\_方法该方法会去mplibs中搜索对应的底层运行时库，其中run方法直接进行了调用，而build会获取到callable的计算图类，用户可以进行dump和load操作。



> dump_graph(fn:class[callable])  → Int

> load_graph(path:String) → fn:class

由于在mplibs中已经介绍了其实现的底层图结构，以及用户层面PrivateCell一脉相承的图形式，所以我们可以在此之上得到完整的图，如下图所示，几个算子相连形成最后的图。

<img src="/Users/esion/Desktop/截屏2021-03-26 上午9.45.18.png" alt="截屏2021-03-26 上午9.45.18" style="zoom:50%;" />