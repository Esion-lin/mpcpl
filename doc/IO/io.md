### IO

io向用户提供输入输出的功能，用户通过调用该模块进行安全输入

| API                                          | 说明                 | 支持模式 |
| -------------------------------------------- | -------------------- | -------- |
| [io.input_cls](api.md#input_cls)             | 硬编码的方式输入数据 | d        |
| [io.input_with_file](api.md#input_with_file) | 由文本文件输入数据   | d/s      |
| [io.input_map](api.md#input_map)             | 以回调的方式输入数据 | d        |
| [io.output_cls](api.md#output_cls)           | 输出数据             | d/s      |
| [io.dump](api.md#dump)                       | 向磁盘存储模型文件   | d/s      |
| [io.load](api.md#load)                       | 从磁盘获取模型文件   | d/s      |
| [Io.set_proto](api.md#set_proto)             | 设置IO使用的协议     | d/s      |

