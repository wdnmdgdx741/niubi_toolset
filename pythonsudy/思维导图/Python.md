# Python

## 简介

### python是1991年诞生

### 荷兰人 吉多·范罗苏姆 创造

### 现在已经更新到python3,2020年正式宣布不再更新python2

### python能做什么

- 办公OA自动化

	- 表格处理
	- 表格一键生成

- 网站爬虫

	- 抢购火车票
	- 网站内容爬取

- 文件处理自动化

	- zip套娃解压
	- 一键创建文档

- 数据可视化
- 图片像素处理

## Python安装

### Python解释器安装

- 安装
- https://www.python.org/

### Pychram

- 安装
- https://www.jetbrains.com/pycharm/

## Python基础语法

### print函数使用

- print可以打印数字

  print(123)

- 可打印字符串

  print("hello world")
  print('hello everybody')

	- 打印string，我们需要注意，要加上单引号‘ 或者是双引号“ ，这样python就会原封不动的输出string。否则，python就理解不了（）中的string
	- 同样使用print连接string也需要遵守上面的原则

	  print("hello"+"world")

- 运算符的表达式

  print(1+6)

	- 在表达式中print函数会直接输出表达式的结果

- 把打印的内容写到文件中

  #-*-coding:utf-8-*-
  #Author  :    kt21
  f = open("test.txt", "a+")
  print("hello world", file= f)
  f.close()

	- 文件的读取和写入
	- open打开一个文件，如果文件不存在，就创建这个文件，a+ ,就是追加写入。
	- 打开文件当然就需要关闭文件，我们需要使用close()关闭打开写入的文件

### 转义字符

- 反斜杠\ + 实现转义功能的首字母
- \'     \"这样的使用print输出的时候就会出现问题

	- print('I'm this is computer')
	- python不认识这样的东西，他认为'  '   " " 都是成对的，但是你现在这样在I‘m 中存在 ' 没有成对，所以程序就会报错.
	- 我们可以经过转义来实现这样的功能

		- print('I\'m this is computer')

	- 这样I'm的分号就不会被python解析

- \\ 转义

	- 输入https:\\www.baidu.com

		- 这里python解释器就会解释成https:\www.baidu.com

			- 解决方法

				- 我们可以使用\\转义http:\\\\www.baidu.com
				- 也可以使用//,这种方法多用于windows文件路径转义
				- 在字符串中希望，不改变原string，我们可以在string前面加上r或者R,实现转义

				  print(r"I'm this is book")

					- 注意：使用这种方法最后一个string不能是反斜线\

- 转义功能的首字母

	- 换行 \n

		- 本意就是换行print("hello\nworld"),输出的结果就是分两行来显示

	- 制表符 \t

		- 制表符，占用是四个字节的位置。print("hello\tworld")输出的结果就是

			- print("hello\tworld")

			  hello	world

			- print("hellooo\tworld")

			  hellooo world

	- 退格 \b

		- 就是先退一个字符然后继续拼接
		- print("hello\bworld")

			- 输出的结果就是hellworld

	- 回车 \r

		- 实际上就是确定了回车的位置，就是每次\r都是一次回车，光标就回到行首，如果在同一行里就会覆盖上面的内容

			- print("hello\rworld")

				- 对应输出的内容就是word
				- hello是之前的内容\r换行之后覆盖了之前的内容，所以只有world了

### 二进制与字符编码

- 计算机是以逻辑电路组成的

	- 逻辑电路就是开和关，在计算机里就是0和1表示
	- 在计算中有个字节为8bit

		- 8个位置可以表示256种状态2^8

			- 256种状态对应ASCII码表

				- ASCII可以表示128种状态
				- 其他的128种状态是给其他国家使用的

			- ASCII使用一个字节表示8个位置

		- 8bit=1byte
		- 1024byte=1KB
		- 1024KB=1MB
		- 1024MB=1G

	- 世界上未来统一编码推出了

		- Unicode十六进制

			- 不管中英文统一使用2个字节表示
			- 验证

				- print(chr(0b1000001))=A

					- 在python中使用0b表示这是一个二进制数
					- 不指定0b 0X ，Python都是以int类型表示的

						- 这里不指定0b就会报错，错误int类型超过最大值

					- 0b  (bin)  表示二进制
					- 0x  (hex)  表示十六机制
					- 0o  (oct)  表示八进制
					- chr  表示字符串

						- 注意：但是只能传入一个参数，所以指定类型的之后不可以，使用print(chr("706E6773", 16))

					- ord 将一个字符转化为ascii对应的十进制数字

						- 注意：只能转化一个字符，转化两个字符会报错

		- utf-8

			- 英文1个字节表示
			- 中文3个字节表示

### 保留字及标识符

- 在Python保留字查看
- keyword

  import keyword
  print(keyword.kwlist)

	- python中的保留字['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

- 自己给定名字的变量、函数等都属于标识符

	- 可以以划线_、数字、字母组成
	- 不可以于数字开头
	- 不能使用保留字
	- 区分大小写

		- test
		- Test

### 变量

- 就像是带标签的盒子，变量就是标签盒子

	- 标识，是一种人们可以读懂的昵称，但是在计算机中指的就是内存中的位置，我们可以使用id()来打印在内存中的位置

		- 标识地址，是计算机内存分配的所以大家的都不一样

	- 数据类型，我们说的整数型int、浮点数float、布尔bool、null。我们可以使用type()打印数据类型
	- 值，value，我们print()打印的就是值，hellowoed就是value(值)

- 变量在内存中保存值的方式

	- 比如：name = "hali"

		- 实际上name指向的是内存中id的地址

			- 标识（id）：23443....
			- 数据类型(type ) ：string
			- 值（value）：hali

- 变量在内存中多次赋值的指向变化

	- 比如：name = "hali"
	- name = "haoke"

### 数据类型

- 数据类型

	- int整数型

		- 可以表示正数、负数、0

			- 十进制，python默认类型
			- 二进制，使用0b表示
			- 八进制，使用0o表示
			- 十六进制，只用0x表示

	- float浮点数

		- 是由整数部分和小数部分组成

			- 会出现计算不准确的情况，但是只是部分小数计算

				- 比如说1.1+2.2，计算的结果就是3.3000000000000003

			- from decimal import Decimal

				- 导入模块来计算，就可以避免错误

			- print(Decimal("1.1")+Decimal("2.2"))

	- bool布尔

		- 只有两种状态true、false

			- 布尔也可以当做操作数

				- 在定义布尔的True、False的时候我们首字母要大写，否则会报错

					- True+1=2；False+1=1

			- True表示真，表示1
			- False表示假，表示0

	- str字符串

		- 你好这样的形式就是string（str）类型

			- 使用单引号’

				- 只能在一行中

			- 双引号“

				- 只能在一行中

			- 三双引号'''   '''表示

				- 表示多行

		- 类型转化

			- str()将其他类型转化为str类型

				- int转str

					- str(123)=string "123"

				- float转str

					- str(3.1415)=string “3.1415”

				- bool转str

					- str(True)=sting"True"

			- int()将其他类型转化为int类型

				- str转int

					- 无法转化，在int转化中，只能转化数字类型

				- float转int

					- 只能转化成整数，会舍去小数部分

				- bool换int

					- 会转化成数据表达，True就是1，False就是0

			- float将其他类型转化为float类型

				- str转float

					- 可以转化数字串，但是不可以转化字符串

				- int转float

					- 转化整数，会在末尾加上0，就像2.0这样

				- bool转float

					- 同样会显示 0, 1，加上1.0 ，0 这样表示

### 注释

- 在python中分为单行注释和多行注释

	- #单行注释
	- 多行注释在python中没有指定，通常都是三对引号来表示
	- 在python中注释编码方式

		- #codeing:utf-8
		- #codeing:gbk

### input输入

-  input是一个输入函数，输入的类型通常都是str类型

	- 我们需要用一个变量来接收传入的数据，所以是s = input("你需要什么？")

- input输入的都是string类型，当我们需要使用int类型的时候我们可以使用int来转化

	- i = int(input("请输入一个数字："))

### 运算符

- 数字运算符

	- 加 +

		- 1+1=2

	- 减 -

		- 2-1=1

	- 乘 *

		- 1*2=2

	- 除 /

		- 4/2=2

	- 次幂 **

		- 2**3=8

	- 整除 //

		- 11//3=3

	- 取余 %

		- 10%3=1

- 赋值运算符=

	- 执行顺序是右->左

		- i = 74，安装从右到左的执行顺序，把74这个值赋给了i

	- 链式赋值

		- a=b=c=20

			- 这里a,b,c,指向的都是一个地址就是，20这个内存所在的地址（id）

	- 参数赋值

		- +=、-=、/=、*=、%=、//=、

			- 这个参数赋值的意思就是i += 10=i = i +10,同理就是本身加一个参数

	- 解包赋值

		- a,b,c=10,20,30

			- 顾名思义，解包，那么就是说包前后都是一样的，才能实现解包。就是说左右要一样，定义的参数，要和值项数是一样的，否则就会报错

- 比较运算符

	- <、>、<=、>=、==、!=

		- !=是不相等、一个=是赋值运算符、两个==是比较运算符，比较是否相等，这里比较的是value值。

	- is、is not

		- 上面的==比较的是value，这里比较的是标识（id）

			- 在Python中数组中的值相同，但是id不同，变量不同值相同id就相同

- 布尔运算符

	- and 并且

		- and比较两边，都为True结果为True、两边有一边为False，结果为False。比较类型为布尔类型

	- or 或者

		- or比较两边，有一边为True，则结果为True。

	- not 取反

		- 如果操作数为True，就返回False、为False，就返回True

	- in 在里面

		- 寻找字符，用来判断一个字符串，里面有没有指定的字符，有就是True没有就是False

			- 比如：print(“h” in "hello")结果为True

	- not in 不在里面

		- 寻找操作数、里面没有指定的字符。结果为True，有则为False

			- 比如：s = "Hello Everybody";print("H" in s)

- 位运算符

	- 将数据转化为二进制进行计算

		- 位与&

			- 对应数位都是1，结果才是1。否则为0

		- 位或|

			- 对应数位都是0，结果才是0。否则为1

		- 左移位运算符>>

			- 高位溢出舍去，低位补0≈操作数/2

		- 右移位运算符<<

			- 高位补0，低位溢出截断≈操作数*2

### 运算符优先级

- 数字运算符

	- 先算乘除后加减

- 比较运算符
- 布尔运算符
- 赋值运算符

### 程序的流程控制结构

- 顺序结构

	- debug，按照代码顺序一步步执行下去

- 选择结构

	- Python中一切皆对象，所有的对象都会有一个布尔值

		- 判断对象布尔值函数bool()

			- print("------以下对象布尔值都为False-----------")
			- print(bool(False))
			- print(bool(None))
			- print(bool(0))
			- print(bool(0.0))
			- print(bool(""))
			- print((bool('')))
			- print(bool([]))         #空列表
			- print(bool(list()))     #空列表
			- print(bool(()))         #空元组
			- print(bool(tuple()))    #空元组
			- print(bool({}))         #空字典
			- print(bool(dict()))     #空字典
			- print(bool(set()))      #空集合

	- 单分支条件语句if

		- if (条件判断) :为真就就执行条件语句里面的代码，不成功就不执行条件语句内的代码

	- 双分支条件语句if else

		- 条件判断为真执行if里面的，为假执行else里的语句

	- 多分支条件语句 if else elif

		- 多次判断，找到True结束判断。比如第二个条件就是True，就不会继续向下判断。直接退出if。直到找到True。

	- 嵌套分支语句

		- if else 里面套一个if else，但是前提是第一个if 判断通过，才能继续执行里面的if else

	- 条件表达式

		- 类似于三目运算符

			- print(str(num_a) + "小于等于" + str(num_b)  if num_a >= num_b else str(num_a) + "小于等于"  + str(num_b))

				- 条件为True返回左边的内容，条件为False返回右边的内容

- pass

	- 没有特殊的含义就是一个占位符，写在需要表达式的地方

		- if age : pass else pass 

			- 比如说要打印的内容还没有想好就可以使用pass，这样的语法也不会报错

- 循环结构

	- ranger()函数的使用

		- 用于生成数字序列ranger(0, 101, 2)就会生成一个0-100的，序列，步长为2，就是中间隔着2

			- 要注意的是，生成的序列最后一个-1，就像这里101-1=100

	- while循环的使用

		- 不同if ，不停地判断条件循环语句。直到条件不成立退出循环

			- 初始变量
			- 条件判断
			- 循环体
			- 改变初始变量值

	- for循环

		- for i in range(0, 21)

			- i 是定义的变量，range是序列，for 遍历这个序列，把每次遍历的值赋给i

				- 不使用循环，不定义变量我们可以使用 _ ，此时就会循环输出循环体的内容

	- break

		- 例如：取款机可以错误输入3次密码，但是你第一次就输入真确，需要提前结束循环体，就需要使用break

			- 一般情况下使用在if条件语句

	- continue

		- 不同于break直接结束循环而是，结束当前循环，进入下一次循环

			- print("----使用continue实现----")
for i in range(1, 101):
    if i%5 != 0:
        continue
    print(i)

				- 就是结束当前if循环，进入下一个循环for

	- else

		- if     else

			- 分支条件语句

		- for    else

			- 在条件判断中没有break，就会执行else，如果有break就会跳出循环，不执行else

		- while   else

			- 在条件判断中没有break，就会执行else，如果有break就会跳出循环，不执行else

	- 二重break，continue

		- break

			- 就会跳出当前循环体的上一层循环

				- print("---break---")
for i in range(0, 5):
    for j in range(1, 11):
        if j%2 == 0:
            break
        print(j)

					- 这里就会跳出for j  range(1,11)；直接进入第一个循环体

		- continue

			- 会跳出当前循环体

				- print("---continue---")
for k in range(0, 5):
    for s in range(1, 11):
        if s %2 == 0:
            continue
        print(s, end=" ")
    print()

					- 这里回跳转到  if  重新判断

### 列表的创建与删除

- 列表

	- list=[123,456,hello]

		- []就像是一个盒子，但是盒子里面分了很多的夹层，每一个夹层对应指向一个value的id，全部的隔层，是一个盒子，所以盒子也有一个id，list指向这个id

- 列表创建

	- list=[123.345.567]
	- i = list(["hello", "world", 98])

		- 使用list()函数定义的在（）中还是需要使用【】

	- index方法来查询元素的索引

		- '''
使用index的方法来查询元素的索引
'''

list = ["hello", 99, "hello", "world"]
print(list.index("hello"))
print(list.index("hello", 1, 4))

			- 如果列表中有两个相同的元素，index只会索引第一个元素

	- 切片操作

		- 可以规定开始和结束的列表

			- list[strat,stop,step]
			- 当步长为正数的情况，切片的默认顺序为start=0，stop=到最后，step=1
			- 当步长为负数的情况，切片的默认顺序为start=最大的，也就是-1，stop=0，step=-1

- 列表的数据添加

	- append

		- 就是在列表的最后添加一个元素，但是不管你，添加的是不是元素，统一按元素处理。就比如，这里添加一个列表，但是会被处理成一个元素

	- extend

		- 合并列表，不同上面的就是，添加一个列表的时候不会被单独的，处理成一个元素，而是合并了列表

	- insert

		- list.insert(位置，元素)，指定位置插入一个元素

	- 切片

		- list[1::] = list2 第二个元素开始替换成list2中的元素。切除列表中指定位置后面的元素，替换成要放入的元素，或者列表元素

- 列表元素的修改

	- 更改单个元素索引位置赋值

		- list[2] = 200；列表中索引是2的元素就是更新成了200

	- 更改多个元素的值，使用切片索引

		- list[1:3] = [10, 20, 30, 40]

- 列表的排序操作

	- sort方法，是在原列表上进行排序，不会生成新的列表

		- lst.sort()默认是从小到大排序
		- lst.sort(reverse=True)#从大到小
		- lst.sort(reverse=False) #从小到大

	- sorted()函数，会生成新的列表

		- new_list = sorted(lst1)#从小到大
		- disk_lst1 = sorted(lst1, reverse=True)

- 列表生成式

	- [i*i for i in range(1, 10)]

		- i*1是一个表达式，最终生成的列表是这个决定的

			- s = [i for i in range(1, 10)]
print(s)

print("-----生成2， 4， 6， 8，10的列表")
lst = [i*2 for i in range(1,6)]
print(lst)
lst1 = [i for i in range(2, 11, 2)]
print(lst1)

- 列表数据删除

	- remove

		- 一次只能删除一个元素
		- 有重复的元素，按照顺序删除第一个元素
		- 没有指定删除元素就会报错

	- pop

		- 删除一个指引位置的元素
		- 索引位置不存在就会报错
		- 没有索引位置就，默认删除元素中最后一个元素

	- 切片

		- list[1:3] = [] 这样可以删除1到3不包括3的中间的所有元素。切片一次最少删除一个元素

	- clear

		- 清除列表中的所有元素，处理完就剩下[ ]

	- del 

		- 删除列表

### 字典

- 字典原理

	- 因为存在字典里的键，经过hash函数计算，所以里面存放的键必须是不可变序列，比如说string int、float
	- 可变序列，list dic

- 创建字典

	- disk = {"张三“ : 21, ”李四“ : 30}
	- 使用dict函创建s = dict(name="张三", age=20)

- 查找字典中的value

	- 方法一就是dict["键值"]
	- 方法二就是使用get方法获取

		- dict.get(“键值”)

- 字典的增删改查

	- del disk["zhangsan"]

		- 删除字典中键值对是zhangsan的数据

	- dsik.clear()

		- 清空字典内容，打印输出的就是{}

	- disk["zhaoliu“] = 100

		- 往字典中添加了一个键值对为zhaoliu的value为100的元素

	- disk["zhaoliu“] = 120

		- 修改了zhaoliu键值对的value

- 使用keys, values, items方法获取字典中的数据

	- keys 获取键值对

		- keys = disk.keys()

	- values 获取值

		- values = disk.values()

	- items 获取键值对

		- items = disk.items()

- 字典元素遍历

	- for i in disk:

		- 字典的遍历是输出字典的键值，而不是value
		- 可以使用上面的get方法来获取value

			- print(disk, disk[i])
			- print(disk, disk.get[i])

- 字典生成式

	- '''
字典生成式
'''

itmes = ["zhangsan", "lisi", "wangwu"]
price = [98,99,102]
k = {q : k for q, k in zip(itmes, price)}
print(k)

		- for i 遍历的时候要注意的是，这里定义的变量，要和前面定义的字典键key：值value相对应否则程序会报错

### 元组

- t = ("zhangsan", "lisi", "wangwu")

	- 他和列表之间的外观区别就在于列表式[],元组是()

		- 元组是不可变序列，就说明，我们不可以进行增删改查的操作

- 创建元组的方法

	- t = ("zhangsan", "lisi", "wangwu")
	- t1 = tuple((12,34,56))
	- t2 = "hello", “world’, 45
	- t3 = (10,)

- 元组本身不可增删，但是如果元组中有列表，那么我们可以通过索引列表，来对列表进行增删。

	- '''
元组本身不可以增删，但是列表可以，我们可以通过在元组中的列表来进行操作
'''
t = (10, [10, 20], 87)
t[1].append(100)
print(t)

- 元组遍历

	- 我们可使用for in来遍历元组中的元素

		- '''
元组中元素的遍历
'''
t = (10, 10, 20, 87)
for i in t:
    print(i)

### 集合

- 是可变的类型序列

	- s = {"nihao",23,32}
	- 创建空元素不可使用{},使用这个指挥被程序认为是字典，我们需要使用set函数来创建空字典

- 集合的增删改查

	- s.add(100)

		- 一次添加一个元素

	- s.update([1,2,3])s.update((10,20))

		- 一次至少添加一个元素

	- s.remove(10)

		- 一次删除一个元素，要是指定的元素没有就会报错

	- s.discard(10)

		- 一次删除一个元素，但是没有这个元素的时候也不会报错，有就删除

	- s.pop()

		- 不需要指定参数，随机删除一个元素。指定参数就会找不到元素，而报错

	- s.clear()

		- 清除集合中的元素

- 集合之间的关系（判断）

	- 判断两个几个是否相等

		- 集合是否相等的判断依据就是集合中元素值是否相等

	- 子集，A集合中包含B集合中所有的元素，我们就叫B是A的子集

		- 判断子集用到issubset方法

	- 真子集，A集合中包含B集合中所有的元素，我们就叫A是B的真子集

		- 判断真子集用issuperset方法

	- 交集，A集合中的元素有一部分是B集合中的元素。我们就称为交集。

		- 判断交集用isdisjoint方法

			- 有交集返回的是False
			- 没有交集返回的是True

- 集合的数学操作

	- 交集，A集合和B集合共同拥有的元素就是交集

		- intersection方法

			- 等同于s & s1

	- 并集，A集合和B集合共同元素合并

		- union方法

			- 等同于s | s1

	- 差集，A集合减去和B集合重复的部分元素和B集合全部

		- difference方法

			- 等同于s - s1

	- 对称差集，A集合和B集合共同的部分减去

		- symmetric_difference方法

			- 等同于s ^ s1

- 集合生成式

	- s = {i for i in range(6)}

		- 生成集合的方法和列表是一样的，就是类型不一样，列表是[] 结合是{}

### 字符串

- 字符串查询操作

	- index()

		- 查找字符串正向索引位置
		- 没有就会报错

	- rindex()

		- 查找字符串逆向索引位置
		- 没有就会报错

	- find()

		- 查找字符串正向所用位置
		- 没有这个字符串不会报错，会返回-1

	- rfind()

		- 查找字符串逆向索引位置
		- 没有这个字符串不会报错，会返回-1

- 字符串的大小写转化

	- upper

		- 所有字符转化为大写

	- lower

		- 所有字符转成小写字母

	- swapcase

		- 将字符中大写的转化为小写，小写的转化为大写

	- title

		- 将字符串中的单词首字母大写

- 字符串内容对齐

	- center(20, '*')

		- 字符串居中对齐，一个是总长度，长度小于原字符串长度，就输出原字符串；对齐填充参数，填充参数不写默认是空格。

	- ljust(20, '*')

		- 字符串左对齐，接受两个参数，第一个参数就是长度，长度小于字符串长度输出原字符串；对期填充字符，不写默认空格。

	- rjust(20, '*')

		- 字符串右对齐，接受两个参数，第一个参数是长度，长度小于字符串长度，就输出原字符串；对齐填充字符可定义，不定义默认空格

	- zfill(20)

		- 字符右对齐，只接受一个参数，字符串长度，填充是0，但是要是出现负数填充是在-号后面，比如-0000876

- 字符串分割

	- split()

		- 从左开始分割

	- rsplit()

		- 从右开始分割

- 判断字符串

	- isidentifier()判断字符串是不是标识符
	- isspace()判断指定字符串是否是全部由空白字符串组成（回车、换行、水平制表符）
	- isalpha()判断指定字符串是否由字母组成
	- isdecimal()判断指定字符串是否由十进制数字组成
	- isnumeric()判断字符串是否由数字组成
	- isalnum判断指定字符串是否全部字母和数字组成

- 字符串的替换与合并

	- replace()

		- 替换字符中的值，可以指定三个参数，第一个是替换对象、替换值、替换个数，不指定就替换所有

	- join()

		- 将列表或者元组中的字符串合并成一个字符串

- 字符串比较

	- > < = <= >= == !=

		- 字符串的比较是一个一个比较的，如果中间有一个不相等就不会继续比较下去
		- 比较的原理是，比较原始值ord()可以看到你原始值，对应chr()可以看到字符，比较其实就是比较两个字符串的ASCII码对应的值
		- 一般比较我们会使用==，但是和 is 有什么区别呢

			- ==比较的是值，is 比较的是内存地址
			- 因为python的驻留机制，所以这里a b c 的id是一样的

- 字符串的切片操作

	- 和列表一样可以索引，不一样的是列表是可变序列，字符串是不可变序列

		- '''
字符串的切片操作
'''

s = 'hello,python'
print(s[1::])
print(s[::2])
#倒序
print(s[::-1])

- 格式化字符串

	- 就是按一定格式输出的字符串

		- 占位符%

			- %s  字符串
			- %d  或者 %i 数字
			- %f 浮点数

		- {}做占位符

			- {0}
			- {1}

		- f-string

			- print(f‘hello{name}’)

		- 使用%，指定宽度和精度

			- print('%10d' % 99)

				- 10表示宽度是10

			- print('%f' % 3.1415926)

				- 浮点数

			- print('%.3f' % 3.1415926)

				- 浮点数保留三位小数

			- print('%10.3f' % 3.1415926)

				- 宽度为10保留三位小数

		- 使用{}，指定宽度和精度

			- print('{}'.format(3.1415926))
			- print('{0}'.format(3.1415926))
			- print('{0:.3}'.format(3.1415926))

				- 表示指定的输出总数为3,输出为3.1

			- print('{0:.3f}'.format(3.1415926))

				- 精度为3，小数点保留三位

			- print('{0:10.3f}'.format(3.1415926))

				- 宽度为10，小数点保留三位小数

- 字符串的编码转换

	- 编码：是将字符串类型的数据通过二进制bytes转化

		- s.encode(encoding="GBK")
		- s.encode(encoding="UTF-8")

	- 解码：是将二进制数据转化为字符串

		- byet.decode(encoding="GBK")
		- byet.decode(encoding="UTF-8")

### bug

- 语法错误

	- SyntaxError

- 索引越界

	- IndexError

- 异常处理机制

	- try:      except()

		- except() 指定错误类型

			- try:
    a = int(input("请输入一个整数："))
    b = int(input("请输入第二个整数："))
    rec = a + b
    print("a+b=",rec)
except ZeroDivisionError:
    print("输入错误")

	-  BaseException 

		- try:
    a = int(input("请输入一个整数："))
    b = int(input("请输入第二个整数："))
    rec = a / b
except BaseException as e:
    print("出错了",e)
else:
    print("a/b=",rec)

	- finally:

		- 无论程序是否错误或者执行else；都会输出finally的内容

			- finally是为了释放内存的就是关闭的作用

- 常见的错误类型

	- ZeroDivisionError

		- 除0或者取模所有数据类型

	- IndexError

		- 系列中没有索引

	- ValueError

		- 传入无效参数

	- KeyError

		- 映射没有这个键

	- NameError

		- 未声明初始化对象

	- SyntaxError

		- python语法错误

- 异常处理的模块

	- traceback

		- 不指定错误类型，通过模块识别

			- '''
异常处理模块
'''
import traceback
try:
    print("--------------------")
    print(1/0)
except:
    traceback.print_exc()

### 函数

- 函数定义

	-  函数是定义之后可以复用的
	-  函数可调用
	- 函数有一定的隐藏性

- 函数的创建

	- def 自定义函数名 (参数):

		- return返回值是必需要有的，不然就会返回Nono

			- '''
函数创建
'''

def calc (a, b):
    c = a + b
    return c

rec = calc(10, 20)
print(rec)

- 函数的参数传递

	- def 函数中的参数我们就称为形参
	- 传入的值，没有指定特殊顺序；位置传参，就默认从左到右
	- b = 10,  a = 20，指定值的数据，我们就称为关键之参数。实参

- 函数可变对象和不可变对象的影响

	- 传入函数的实参，和函数定义的形参名称不同也不影响
	- 当函数没有返回值的时候可以不写return
	- string是不可变对象，所以就算在函数体内，改变了参数的值，函数体执行完成也不会影响本来的值
	- 但是改变可变参数，例如列表。改变参数的值，就会影响参数本身的值。

- 函数的返回值

	- 再有一个返回值的时候就会返回原类型
	- 如果有多个返回值的时候就会输出元组类型
	- 函数是否返回值是情况而定的，就不需要写return

- 函数的参数定义

	- 默认参数就是可以指定实参，也可以不指定实参，使用默认值

		- '''
默认参数
'''

def fun(a, b=10):       #这里的b=10就是默认参数
    print(a,b)

fun(100)
fun(10,20)

- 函数的参数定义

	- 在我们不确定形参个数的时候我们可以使用*args

		- 输出的数据类型为元组

	- 标识符形参我们使用**args

		- 输出的数据类型为字典

- 函数的参数总结

	- 函数调用

		- 列表转化为位置实参使用*
		- 字典转化为关键字实参使用**

	- 函数定义

		- 位置实参*args
		- 关键字实参**args
		- 函数定义形参顺序问题

			- 先定义位置参数，后定义关键字参数，否则程序会出现错误

				- '''
函数形参定义顺序问题
'''

def fun(a,b,*,c,d,**args):
    print("a=", a)
    print("c=", c)
    print("b=", b)
    print("d=", d)
    print("args=", args)
fun(10,20,c=20,d=10,k=20)

- 变量的作用域

	- 全局变量，在程序中任何位置都可以调用这个变量
	- 局部变量，函数中定义的变量，只能在函数体中才能被使用，函数体外就无法使用了
	- 改变局部变量我们可以使用global

- 递归函数

	- 递归就是自己调用自己

		- 计算6的阶乘

			- '''
计算6的阶乘
'''

def fun(n):
    if n == 1:
        return 1
    else:
        return n*fun(n-1)

print(fun(6))

- 斐波那契数列

	- 123个数3=1+2,依次递归

		- '''
斐波那契数列
'''

def fun(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fun(n-1)+fun(n-2)

print(fun(4))

## 面向对象

### 面向对象

- 面向过程

	- 做东西的过程

- 面向对象

	- 就像买做好的东西

- 类和对象

	- 类就像是人类

		- 大人小孩就可以叫做是对象

			- python中一切皆对象

### 类的创建

- 类属性

	- 直接写在类里的变量，我们称为类属性

- 类方法

	- def 在类中我们称为类属性，在类外面我们称为函数

- 静态方法

	- @staticmethod，所以我们称为静态方法

- 类方法

	- @classcmethod，所以我们称为类方法

- 初始化方法

	-     #初始化方法
    def __init__(self, name, age):
        self.name= name     #self.name是实例属性，这里进行了赋值操作，将我们的name赋值给实例属性self.name
        self.age = age

### 对象的创建

- 对象的创建又称为类的实例化
- 实例名(对象名) =  类名

	- #创建Student类的对象
stu = Student("张三", 20)         #实例对象，初始化方法,定义的相符

- print(stu.name)#使用实例属性
print(stu.age)#使用实例属性
- stu.eat()#使用实例方法

	- 类调用对象

		- Student.eat(stu)

- stu.method()#使用静态方法
- stu.cm()#使用类方法
- 类属性的使用

	- #类属性的使用
stu1 = Student("张三",20)
stu2 = Student("李四",30)
print(Student.native_pace)
Student.native_pace = "江西"
print(stu1.native_pace)
print(stu2.native_pace)

		- 因为两个类对公共一个类属性，所以改变类属性的值，两个类对象都会改变

### 动态绑定属性和方法

- 指定类对象添加的，所以stu没有这个实例对象

	- stu = Student("zhagnsan",20)
stu1 = Student("lisi",30)
print("-------------")
stu1.gender = "女"
print(stu.name, stu.age)
print(stu1.name, stu1.age, stu1.gender)

### 面向对象的三大特征

- 封装

	- 提高程序的安全性

		- '''
Python面向对象封装
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age            #不希望在类的外部被访问加上__

    def show(self):
        print(self.name, self.__age)

stu = Student("zhangsan", 20)
stu.show()

#在类的外部使用name,age
print(stu.name)
print(dir(stu))
print(stu._Student__age)

- 继承

	- 提高代码复用性

		- '''
Python面向对象继承
'''
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, student_no):
        super().__init__(name, age)
        self.student_no = student_no

stu = Student("zhagnsan", 18, '11001')
stu.info()

			- object就是祖宗、Person就是爸爸、Student就是儿子，这样的继承关系。依次称为父类、父类、子类

	- 方法重写

		- class Student(Person):
    def __init__(self, name, age, student_no):
        super().__init__(name, age)
        self.student_no = student_no
    def info(self):
        super().info()
        print("学号", self.student_no)

			- 改变子类，新建一个方法重写

- object类

	- 其他类没有指定父类，都默认继承object类

		- dir()查看所有对象属性
		- _str_()方法

			- '''
Python面向对象object类
'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def __str__(self):
        return "{0}，今年{1}岁".format(self.name, self.age)
stu = Student("zhangsan",20)
print(dir(stu))
print(stu)

		- 不重写str默认输出类的id

- 多态

	- 提高程序的可扩展性、可维护性

		- '''
Python面向对象多态
'''
class Aimal(object):
    def eat(self):
        print("动物会吃")
class Dog(Aimal):
    def eat(self):
        print("狗吃骨头")
class Cat(Aimal):
    def eat(self):
        print("猫吃鱼")
class Person(object):
    def eat(self):
        print("人是五谷杂粮")
def fun(i):
    i.eat()
fun(Aimal())
fun(Cat())
fun(Dog())
print("-------------")
fun(Person())

### 特殊属性和方法

- 特殊属性

	- __dict__    获得类对象或者实例对象所绑定的所有属性和方法的字典
	- __class__    输出对象所属的类
	- __bases__    类对象的父类类型的元素
	- __mro__    类的层次结构
	- __base__    类的基类（就是和子类最近的类）
	- ___subclasses__()    子类的类表

- 类的特殊方法

	- __len__()

		- 通过重写__len()__方法，让内置函数len()的参数可以是自定义类型的

	- __add__()

		- 通过重写__add__方法，可以使用自定义对象具有+功能

	- __new__()

		- 用于创建对象

	- __init__()

		- 创建的对象进行初始化

### 类的浅拷贝与深拷贝

- 变量的赋值操作

	- 创建一个对象但是赋值给两个变量使用就是赋值操作

- 浅拷贝

	- import copy

		- 创建时不同的类但是里面值是相同的

- 深拷贝

	- from copy import deeepcopy

		- 拷贝类对象和方法都拷贝一遍

## 模块

### 导入模块的两种方式

- import 模块
- form 模块 inport 模块中的类/方法/函数

### 导入自定义模块

- 使用pycharm改变”标记目录"，为根

### 以主程序的方式运行

- 当这个程序被运行的时候才被执行，如果是被调用，就不会执行if里面的语句

	- '''
以主程序运行
'''
def fun(a,b):
    return a + b

if __name__ == '__main__':
    print(fun(10,20))

### 包

- 我们创建包当调用的时候我们需要这样写

	- import 报名.类名

		- as 改别名

### python常用的内置模块

- sys

	- 与python解释器及其环境操作相关的标准库

- time

	- 提供与实践相关的各种函数的标准库

- os

	- 提供了访问操作系统相关的各种函数的标准库

- calendar

	- 提供与日期相关的各种函数标准库

- urllib

	- 用于读取来自网上的数据标准库

- json

	- 用于使用JSON序列化和反序列化对象

- re

	- 用于字符串执行正则表达式匹配和替换

- math

	- 提供标准算数运算函数的标准库

- decimal

	- 用于进行精确控制运算精度、有效位数和四舍五入操作的十进制运算

- logging

	- 提供了灵活的记录事件、错误、警告和调试信息等日志信息功能

-  schedule

	- 定时执行

### 第三方模块安装

- pip install module

	- '''
间隔执行模块
'''
import schedule
import time

def job():
    print("哈哈---")

#定时执行程序
schedule.every(3).seconds.do(job)
while True:
    #开始跑
    schedule.run_pending()
    time.sleep(1)#延迟一秒

## 编码格式

### 编码格式介绍

- Unicode
- py文件使用的是UTF-8
- Python默认保存的是UTF-8，我们要修改只需要在文件最上面加上#encoding = gbk就可以改变
- 不同编码方式决定占用磁盘空间的大小

### 文件的读写IO

- '''
IO读写操作
I = input 读入
O = output 输出
'''
file = open("1.txt","r")
print(file.readlines())
file.close()

## 文件的IO

### 常用的文件打开模式

- r

	- 以只读模式打开

- w

	- 以只写模式打开，没有就创建，有就替换覆盖

- a

	- 以追加模式打开，没有就创建，有就在后面追加内容

- b

	- 以二进制打开，不能单独使用，要和其他读写模式一起使用，如rb或者wb

		- '''
二进制读写模式
'''
src_file = open("hacher.png","rb")
save_file = open("1.png", "wb")
save_file.write(src_file.read())
src_file.close()
save_file.close()

- +

	- 以只读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+

### 文件对象的常用方法

- read(size)

	- 从文件中读取size字节内容，不写就读全部

- readline()

	- 从文件中读取一行内容

- readlines()

	- 以类表形式返回文件中的字符串

- write()

	- 写入str内容到文件

- writelines(s_list)

	- 将字符串列表写入文本文件中，不添加换行符

- seek(offset,[whence])

	- 把文件指针移动到新的文职，offset表示相对于whence的位置

- tell()

	- 返回文件指针的当前位置

- flush()

	- 把缓冲区的内容写入文件，但不关闭文件

- close()

	- 不缺爱缓冲区内容写入文件，同时关闭文件，释放文件对象相关资源。

### with语句上下文管理器

- 不用手动关闭释放资源，跳出with语句自动关闭文件，释放资源

	- with open('1.txt', 'r') as file:
    print(file.read())

### 目录操作

- os模块

	- 与操作系统相关的模块，可以调用我们的系统文件

		- getcwd()

			- 返回当前工作路径

		- listdir()

			- 返回指定路径下的文件和目录信息

		- mkdir()

			- 创建目录

		- makedirs(0

			- 创建多级目录

		- rmdir()

			- 删除目录

		- removedirs()

			- 删除多级目录

		- chdir(path)

			- 将path设置为当前工作目录

- os.path模块

	- abspath(path)

		- 用于获取文件或目录的绝对路径

	- exists(path)

		- 用于判断文件或者目录是否存在，如果存在返回True，否则False

	- Join(path,name)

		- 将目录与目录或者文件名拼接起来

	- splitext()

		- 分离文件名和拓展名

	- basename(path)

		- 从一个目录中提起文件名

	- dirname(path)

		- 从一个路径中提取文件路径，不包括文件名

	- isdir(path)

		- 用于判断是否为路径

*XMind: ZEN - Trial Version*