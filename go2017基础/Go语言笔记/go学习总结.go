go2017基础

1、不支持继承、重载 ,比如C++、Java的接口，接口的修改会影响整个实现改接口的类行为的修改,Go 设计者认为这一特点或许根本没用.
2、任何函数定义必须花括号跟在函数声明后面而不能换行 如
func  funca(a int){
}
在Go语言中 函数也是一种类型 可以被推导  使用支持匿名函数 和闭包。
函数的返回值支持多重返回类似Python , 如果不赋值，整数类型默认 0     浮点数类型默认0.0   error类型 默认是nil
3、不用的包一定不要引入，这是Go的原则,就如Python的严格制表符对其一样   ,和 unused 变量都会被  编译器所报错
4、package做为引入包用。
5、import "a"  调用包内部的函数 a.xx()
6、CGo是Go语言的一个特性,可以方便快速的在Go中调用C，相比Java JNI简单容易实现
7、go通过goroutine进行协程优化 提高并发性能。动态线程调整。
8、6g和6l是64位版本的Go编译器和链接器，对应的32位版本工具为8g和8l。Go还有另外一个 GCC版本的编译器，名为 gccgo。
9、注意多个go文件可以用同一个包名字,如果要为 Go生成可执行文件 那么必须 进行 package main
main函数的声明
复制代码
func main() {
    args := os.Args
    if args == nil || len(args) < 2 {
    return
    }
}
复制代码
10、Linux 为了能够构建这个工程， 需要先把这个工程的根目录加入到环境变量GOPATH中。 假设calcproj 目录位于~/goyard下，则应编辑~/.bashrc文件，并添加下面这行代码：
export GOPATH=~/goyard/calcproj
然后执行以下命令应用该设置：
$ source ~/.bashrc,GOPATH和PATH环境变量一样，也可以接受多个路径，并且路径和路径之间用冒号分割。
设置完GOPATH后，现在我们开始构建工程。假设我们希望把生成的可执行文件放到 calcproj/bin目录.
11、GoRoot go安装路径 ....上面的时候工程路径
12、GDB调试
不用设置什么编译选项， Go语言编译的二进制程序直接支持GDB调试， 比如之前用go build calc编译出来的可执行文件calc，就可以直接用以下命令以调试模式运行：   $ gdb calc
因为GDB的标准用法与Go没有特别关联，这里就不详细展开了，有兴趣的读者可以自行查
看对应的文档。需要注意的是，Go编译器生成的调试信息格式为DWARFv3，只要版本高于7.1
的GDB应该都支持它。
13、Go语言会被称为“更好的C语言”
14、每一行不需要加分号自动添加
15、添加了map[string] int
16、添加了类型推导
var a int =1 等价  a:=1
var v1 int = 10 // 正确的使用方式1
var v2 = 10 // 正确的使用方式2，编译器可以自动推导出v2的类型
v3 := 10 // 正确的使用方式3，编译器可以自动推导出v3的类型
出现在:=左侧的变量不应该是已经被声明过的，否则会导致编译错误，比如下面这个
写法：
var i int
i := 2
会导致类似如下的编译错误：
no new variables on left side of :=
17、支持多重赋值,i, j = j, i  两个值可以如此简单的进行交换  而不许引入外部变量

18、我们在使用传统的强类型语言编程时，经常会出现这种情况，即在调用函数时为了获取一个
值，却因为该函数返回多个值而不得不定义一堆没用的变量。在Go中这种情况可以通过结合使
用多重返回和匿名变量来避免这种丑陋的写法，让代码看起来更加优雅。
假设GetName()函数的定义如下，它返回3个值，分别为firstName、lastName和nickName：
func GetName() (firstName, lastName, nickName string) {
return "May", "Chan", "Chibi Maruko"
}
若只想获得nickName，则函数调用语句可以用如下方式编写：
_, _, nickName := GetName()
这种用法可以让代码非常清晰，基本上屏蔽掉了可能混淆代码阅读者视线的内容，从而大幅
降低沟通的复杂度和代码维护的难度

19、在Go语言中，常量是指编译期间就已知且不可改变的值。常量可以是数值类型（包括整型、浮点型和复数类型） 、布尔类型、字符串类型等。所谓字面常量（literal） ，是指程序中硬编码的常量，如：
-12
3.14159265358979323846 // 浮点类型的常量
3.2+12i   // 复数类型的常量
true   // 布尔类型的常量
"foo" // 字符串常量
在其他语言中，常量通常有特定的类型，比如12在C语言中会认为是一个int类型的常量。
如果要指定一个值为12的long类型常量，需要写成-12l，这有点违反人们的直观感觉。Go语言
的字面常量更接近我们自然语言中的常量概念，它是无类型的。只要这个常量在相应类型的值域
范围内，就可以作为该类型的常量，比如上面的常量-12，它可以赋值给int、uint、int32、
int64、float32、float64、complex64、complex128等类型的变量。

20、常量的定义
通过const关键字，你可以给字面常量指定一个友好的名字：
复制代码
const Pi float64 = 3.14159265358979323846
const zero = 0.0             // 无类型浮点常量
const (
    size int64 = 1024
    eof = -1                // 无类型整型常量
)
const u, v float32 = 0, 3    // u = 0.0, v = 3.0，常量的多重赋值
const a, b, c = 3, 4, "foo"
// a = 3, b = 4, c = "foo", 无类型整型和字符串常量
复制代码
Go的常量定义可以限定常量类型，但不是必需的。如果定义常量时没有指定类型，那么它
与字面常量一样，是无类型常量。
常量定义的右值也可以是一个在编译期运算的常量表达式，比如
const mask = 1 << 3
由于常量的赋值是一个编译期行为， 所以右值不能出现任何需要运行期才能得出结果的表达
式，比如试图以如下方式定义常量就会导致错误
const Home = os.GetEnv("HOME")
原因很简单，os.GetEnv()只有在运行期才能知道返回结果，在编译期并不能确定，所以
无法作为常量定义的右值。

21、Go语言预定义了这些常量：true、false和iota。
iota比较特殊，可以被认为是一个可被编译器修改的常量，在每一个const关键字出现时被
重置为0，然后在下一个const出现之前，每出现一次iota，其所代表的数字会自动增1。
从以下的例子可以基本理解iota的用法：
复制代码
const (     // iota被重设为0
 c0 = iota  // c0 == 0
 c1 = iota  // c1 == 1
 c2 = iota  // c2 == 2
)
const (
 a = 1 << iota // a == 1 (iota在每个const开头被重设为0)
b = 1 << iota  // b == 2
c = 1 << iota  // c == 4
)
const (
u = iota * 42    // u == 0
v float64 = iota * 42   // v == 42.0
w  = iota * 42   // w == 84
)
const x = iota      // x == 0 (因为iota又被重设为0了)
const y = iota      // y == 0 (同上)
复制代码
如果两个const的赋值语句的表达式是一样的，那么可以省略后一个赋值表达式。因此，上
面的前两个const语句可简写为：
复制代码
const (     // iota被重设为0
    c0 = iota   // c0 == 0
    c1   // c1 == 1
    c2   // c2 == 2
)
const (
    a = 1 <<iota     // a == 1 (iota在每个const开头被重设为0)
    b   // b == 2
    c   // c == 4
)
复制代码
22、 关于枚举  所有符号 以大写开头在包外是可见的   小写只能在包内部使用
枚举指一系列相关的常量，比如下面关于一个星期中每天的定义。通过上一节的例子，我们
看到可以用在const后跟一对圆括号的方式定义一组常量， 这种定义法在Go语言中通常用于定义
枚举值。Go语言并不支持众多其他语言明确支持的enum关键字。
下面是一个常规的枚举表示法，其中定义了一系列整型常量：
复制代码
const (
    Sunday = iota
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    numberOfDays        // 这个常量没有导出
)
复制代码
同Go语言的其他符号（symbol）一样，以大写字母开头的常量在包外可见。
以上例子中numberOfDays为包内私有，其他符号则可被其他包访问。

23、go中的布尔类型 只能用 false  true != ==不能进行强制转换
Go语言中的布尔类型与其他语言基本一致，关键字也为bool，可赋值为预定义的true和
false示例代码如下：
var v1 bool
v1 = true
v2 := (1 == 2) // v2也会被推导为bool类型
布尔类型不能接受其他类型的赋值，不支持自动或强制的类型转换。以下的示例是一些错误
的用法，会导致编译错误：
var b bool
b = 1 // 编译错误
b = bool(1) // 编译错误
以下的用法才是正确的：
var b bool
b = (1!=0) // 编译正确
fmt.Println("Result:", b) // 打印结果为Result: true

24、Go语言支持以下的几种比较运算符：>、<、==、>=、<=和!=。这一点与大多数其他语言相 同，与C语言完全一致。
复制代码
if i!=j {  }   //必须带大括号
    i,j:=1,2
     if i==j{
        fmt.Println("i==j");
     }else {
        fmt.Println("i!=j");
     }
复制代码
25、两个不同类型的值不能比较 比如 int8 int16，只能强制转换 然后再做比较
复制代码
var a int8
var b int16
a,b=1,2
if int16(a)==b{
   fmt.Printf("a==b")
}
复制代码
26、虽然两个 int8 int16不能直接比较 但是 任何整数类型都能和字面常量整数进行比较  ,但是不能和字符串字面常量进行比较
var a int16
if a==1{
    fmt.Printf("a!=\"a\"");
}


27、Go语言中的位运算    注意 C语言中的~ 取反。 而Go中变成了^
Go语言支持表2-2所示的位运算符。
复制代码
表 2-2
运  算      含  义      样  例
x << y      左移       124 << 2   // 结果为496
x >> y      右移       124 >> 2   // 结果为31
x ^ y       异或       124 ^ 2    // 结果为126
 x & y      与         124 & 2   // 结果为0
x | y       或         124 | 2   // 结果为126
^x          取反       ^2        // 结果为-3  =
复制代码
Go语言的大多数位运算符与C语言都比较类似，除了取反在C语言中是~x，而在Go语言中 是^x

28、关于浮点数的操作  浮点数 自动推导 是float64即C语言中的double 不能直接和fload32转换 要进行强制转换
因为浮点数的比较精度
浮点型用于表示包含小数点的数据，比如1.234就是一个浮点型数据。Go语言中的浮点类型
采用IEEE-754标准的表达方式。
1. 浮点数表示
Go语言定义了两个类型float32和float64，其中float32等价于C语言的float类型，
float64等价于C语言的double类型。
在Go语言里，定义一个浮点数变量的代码如下：
var fvalue1 float32

fvalue1 = 12
fvalue2 := 12.0 // 如果不加小数点，fvalue2会被推导为整型而不是浮点型


对于以上例子中类型被自动推导的fvalue2，需要注意的是其类型将被自动设为float64，
而不管赋给它的数字是否是用32位长度表示的。因此，对于以上的例子，下面的赋值将导致编译
错误：
fvalue1 = fvalue2

对于以上例子中类型被自动推导的fvalue2，需要注意的是其类型将被自动设为float64，
而不管赋给它的数字是否是用32位长度表示的。因此，对于以上的例子，下面的赋值将导致编译
错误：
fvalue1 = fvalue2
而必须使用这样的强制类型转换：
fvalue1 = float32(fvalue2)
29、自定义精准的 浮点数比较 ,由于浮点数不是一种精确的表达方式 所以比较精度 可能不准确
因为浮点数不是一种精确的表达方式， 所以像整型那样直接用==来判断两个浮点数是否相等
是不可行的，这可能会导致不稳定的结果。
下面是一种推荐的替代方案：
复制代码
import "math"

// p为用户自定义的比较精度，比如0.00001
func IsEqual(f1, f2, p float64) bool {
return math.Fdim(f1, f2) < p
}
复制代码

30、 Go语言中的复数类型 , real 取出 实部  imag取出虚部  虚部为0 的复数 为纯虚数。 某一类数字可以表示成这种复数类型
复制代码
var v1 complex64
v1 = 2.5+15i
v2 := 2.5+15i
v3 :=complex(2.5,15)
fmt.Println(v1)
fmt.Println(v2)
fmt.Println(v3)
fmt.Println("real:",real(v1))
fmt.Println("real:",imag(v1))
复制代码
复数实际上由两个实数（在计算机中用浮点数表示）构成，一个表示实部（real），一个表示虚部（imag）。

对于什么是复数可以参考：http://baike.baidu.com/view/10078.htm

复数实际上由两个实数（在计算机中用浮点数表示）构成，一个表示实部（real） ，一个表示

虚部（imag） 。如果了解了数学上的复数是怎么回事，那么Go语言的复数就非常容易理解了。

1. 复数表示

复数表示的示例如下：

复制代码
var value1 complex64  // 由2个float32构成的复数类型

value1 = 3.2 + 12i
value2 := 3.2 + 12i    // value2是complex128类型

value3 := complex(3.2, 12)  // value3结果同 value2
复制代码
2. 实部与虚部

对于一个复数z = complex(x, y)，就可以通过Go语言内置函数real(z)获得该复数的实

部，也就是x，通过imag(z)获得该复数的虚部，也就是y。

更多关于复数的函数，请查阅math/cmplx标准库的文档。


31、Golang中的字符串操作
go中的字符串声明之后只能获取 字符不能修改字符   但是可以修改整个字符串
var str string
str = "abc"
str += "d"
str="1111"
fmt.Println(str)
我们可以获取单个字符但是不能修改单个字符
var str string
str = "abc"
str += "d"
ch:=str[0]
fmt.Printf("A:%c",ch)      //println不能格式化

32、关于Go的编码处理 只支持 Unicode UTF-8格式
import strings 这个包中包含了处理string类型的所有工具函数函数 Go编译器支持UTF-8的源代码文件格式。这意味着源代码中的字符串可以包含非ANSI的字符，比如“Hello world. 你好，世界！ ”可以出现在Go代码中。但需要注意的是，如果你的Go代码需要包含非ANSI字符，保存源文件时请注意编码格式必须选择UTF-8。特别是在Windows下一般编辑器都默认存为本地编码，比如中国地区可能是GBK编码而不是UTF-8，如果没注意这点在编译和运行时就会出现一些意料之外的情况。 字符串的编码转换是处理文本文档（比如TXT、XML、HTML等）非常常见的需求，不过可惜的是Go语言仅支持UTF-8和Unicode编码。对于其他编码，Go语言标准库并没有内置的编码转换支持。不过，所幸的是我们可以很容易基于iconv库用Cgo包装一个。这里有一个开源项目：
https://github.com/xushiwei/go-iconv

33、在Go中字符串的单个字符就是 byte类型也就是 uint8
一个字符串的长度len返回的默认是int类型也就是平台相关类型,我们在做相应的操作的收 要么自动推导 要么进行强制转换
复制代码
var str string
str = "abcdefghijklmn"
var length int8=int8(len(str))
for i:=0 ;i<int(length) ;i++{
    fmt.Printf("%c",str[i])
}
复制代码

34、关于遍历Unicode字符,每个 unicode的字符类型是 rune
每个中文字符在UTF-8中占3个字节，而不是1个字节。
另一种是以Unicode字符遍历：
str := "Hello,世界"
for i, ch := range str {
    fmt.Println(i, ch)//ch的类型为rune
}
输出结果为：
0 72
1 101
2 108
3 108
4 111
5 44
6 32
7 19990
10 30028
以Unicode字符方式遍历时，每个字符的类型是rune（早期的Go语言用int类型表示Unicode
字符） ，而不是byte。

测试代码
复制代码
package main
import "fmt"
func main() {
   var strUnicode string = "hello,世界"
   for i,ch := range strUnicode{
      fmt.Println(i,ch)
   }
}
复制代码
35、关于 Go语言中支持的两种字符类型 一种是 byte 实际上是uint8的别名 ,另一种是unicode类型的字符 关键字为 rune
在Go语言中支持两个字符类型，一个是byte（实际上是uint8的别名） ，代表UTF-8字符串的单个字节的值；另一个是rune，代表单个Unicode字符。
关于rune相关的操作，可查阅Go标准库的unicode包。另外unicode/utf8包也提供了 UTF8和Unicode之间的转换。
出于简化语言的考虑，Go语言的多数API都假设字符串为UTF-8编码。尽管Unicode字符在标 准库中有支持，但实际上较少使用。

36、遍历unicode字符的另一种是 可以用变量占位符去掉不想要的数据
复制代码
package main
import "fmt"
func main() {
   var strUnicode string = "hello,世界"
   for _,ch := range strUnicode{
      fmt.Printf("%c\n",ch)
   }
}
复制代码

37、关于Go语言的指针操作
复制代码
package main
import "fmt"
func main() {
   var inta int8=3 ;
   var pinta*int8=&inta ;
   fmt.Printf("%d",*pinta);
}
复制代码
38、
关于数组的遍历 range 遍历可以选择忽略 索引
复制代码
package main
import "fmt"
func main() {
  byteArr:=[5]byte{1,2,3,4,5}
  for _,val:=range byteArr {
     fmt.Println(val)
  }
}
//////////////////////////////////各种数组的声明/////////////////////////////////
[32]byte   // 长度为32的数组，每个元素为一个字节
[2*N] struct { x, y int32 } // 复杂类型数组
[1000]*float64
  // 指针数组 [3][5]int
  // 二维数组 [2][2][2]float64
  // 等同于[2]([2]([2]float64))

/////关于二维数组的初始化以及声明..................................
package main
import "fmt"
func main() {
  td:=[2][5]int{{1,2,3,4,5},{5,4,3,2,1}}
  for _,val:=range td{
     for _,vall:=range val{
        fmt.Println(vall)
     }

  }
}
复制代码


39、关于Go的数组 是一个值类型,在做为参数传递 或者 做为函数返回的时候 都是 数组的副本,所以不能通过传递 数组参数在函数内部 进行修改 。、
复制代码
package main
import "fmt"
func modify(arr[5]int){
     arr[1]=1
      fmt.Printf("arr[1]=%d\n",arr[1])
}
func main() {
  td:=[5]int{1,2,3,4,5}
  modify(td)
  for _,val:=range td{
        fmt.Println(val)
  }
}
//////Go Web
复制代码

40、Go语言中的数组切片   可以从一个已存在的数组创建 也可以直接手动创建一个数组切片
 一个指向原生数组的指针；
 数组切片中的元素个数；
 数组切片已分配的存储空间。
从底层实现的角度来看，数组切片实际上仍然使用数组来管理元素，因此它们之间的关系让
C++程序员们很容易联想起STL中std::vector和数组的关系。基于数组，数组切片添加了一系
列管理功能，可以随时动态扩充存放空间，并且可以被随意传递而不会导致所管理的元素被重复

基于数组创建切片
复制代码
package main
import "fmt"
func modify(arr[]int){
     arr[1]=1
      fmt.Printf("arr[1]=%d\n",arr[1])
}
func main() {
  td:=[]int{1,2,3,4,5}
  //基于数组创建切片
  slice:=td[:3]    //  td[:]  td[begin:end] 都可以创建数组切片  还可以创建一个比数组还大的切片
  for _,val:=range slice{
     fmt.Println(val)
  }
}
复制代码
41、主动创建数组切片 操作数组 所有的方法 都是适用于数组切片 ,合理利用切片能极大提高内存操作的速度
数组切片支持内建的cap()函数和len()函数
从数组切片创建数组切片的时候只要不超过模板切片的大小那么创建是没问题的,否则会报出数组切片越界的错误。

td:=[]int{1,2,3,4,5}   //这样创建出来的实际上是数组切片
数组切片做为参数传递给函数是可以被修改值的 ，解决了Go中数组属于值类型 结果函数传递参数的时候值被复制
复制代码
package main
import "fmt"
func modify(arr[]int){
     arr[1]=1
      fmt.Printf("arr[1]=%d\n",arr[1])
}
func main() {
  td:=[]int{1,2,3,4,5}
  //基于数组创建切片
  slice:=td[:3]     //从切片创建切片 都可以
  modify(slice)
  for _,val:=range slice{
     fmt.Println(val)
  }
}
复制代码
从输出结果我们发现了 数组切片可以作为参数传递到函数中并且被函数所修改
并非一定要事先准备一个数组才能创建数组切片。Go语言提供的内置函数make()可以用于
灵活地创建数组切片。下面的例子示范了直接创建数组切片的各种方法。
创建一个初始元素个数为5的数组切片，元素初始值为0：
mySlice1 := make([]int, 5)
创建一个初始元素个数为5的数组切片，元素初始值为0，并预留10个元素的存储空间：
mySlice2 := make([]int, 5, 10)
直接创建并初始化包含5个元素的数组切片：
mySlice3 := []int{1, 2, 3, 4, 5}
当然，事实上还会有一个匿名数组被创建出来，只是不需要我们来操心而已。
数组切片支持Go语言内置的cap()函数和len()函数，代码清单2-2简单示范了这两个内置
函数的用法。可以看出，cap()函数返回的是数组切片分配的空间大小，而len()函数返回的是
数组切片中当前所存储的元素个数
动态创建 一个 初始化五个0 并且 内存储空间初始化20的 数组切片
  td1:=make([]int,5,20)
  fmt.Println(cap(td1))
  fmt.Println(len(td1))

//为数组切片动态增加元素
append(td1,1,2,3,4,56,6,7)
//为数组元素添加数组切片
append(td1,td2...)  //一定要加... 附加数组切片的时候
需要注意的是，我们在第二个参数mySlice2后面加了三个点，即一个省略号，如果没有这个省
略号的话，会有编译错误，因为按append()的语义，从第二个参数起的所有参数都是待附加的
元素。因为mySlice中的元素类型为int，所以直接传递mySlice2是行不通的。加上省略号相
当于把mySlice2包含的所有元素打散后传入

42. 数组切片支持内容复制
数组切片支持Go语言的另一个内置函数copy()，用于将内容从一个数组切片复制到另一个
数组切片。如果加入的两个数组切片不一样大，就会按其中较小的那个数组切片的元素个数进行
复制。下面的示例展示了copy()函数的行为：
复制代码
slice1 := []int{1, 2, 3, 4, 5}
slice2 := []int{5, 4, 3}

copy(slice2, slice1) // 只会复制slice1的前3个元素到slice2中
copy(slice1, slice2) // 只会复制slice2的3个元素到slice1的前3个位置

old:=[]int{1,2,3,4,5,6}
newSlice:=[]int{1,3,3}
copy(old,newSlice)
fmt.Println(old)
复制代码

43、在map中使用复杂数据类型
我们可以使用Go语言内置的函数make()来创建一个新map。下面的这个例子创建了一个键
类型为string、值类型为PersonInfo的map:
myMap = make(map[string] PersonInfo)
也可以选择是否在创建时指定该map的初始存储能力，下面的例子创建了一个初始存储能力
为100的map:
myMap = make(map[string] PersonInfo, 100)
关于存储能力的说明，可以参见2.3.6节中的内容。
创建并初始化map的代码如下：
复制代码
myMap = map[string] PersonInfo{
 "1234": PersonInfo{"1", "Jack", "Room 101,..."},
}
package main
import "fmt"
type Info struct{
    name string
    age  int8
}
func main() {
  var infoMap map[string] Info
      infoMap=make(map[string] Info)
  infoMap["s1"]= Info{"ydw",11}
  infoMap["s2"]=Info{"xxx",22}
  fmt.Println(infoMap)
  /////如果sone 没有查找到那么返回值应该是nil 实际上我们只需要判断 ok是否是 true or false 即可判断元素是否查找到
  sone,ok:=infoMap["s1"]
  if ok {
     fmt.Println("s1 student info exists!",sone.name,":",sone.age)
  }else{
     fmt.Println("s1 student info not exists!")
  }
}
/////删除一个map用
delete(map,"key")
复制代码
Go语言提供了一个内置函数delete()，用于删除容器内的元素。下面我们简单介绍一下如
何用delete()函数删除map内的元素：
delete(myMap, "1234")
上面的代码将从myMap中删除键为“1234”的键值对。如果“1234”这个键不存在，那么这个调
用将什么都不发生，也不会有什么副作用。但是如果传入的map变量的值是nil，该调用将导致
程序抛出异常（panic）


44、对于函数的返回值的限制
复制代码
func returnFunc(num int) int{
     if num > 0 {
        return 100  //错误 返回值不能写在if...else之中结构之中
     }
     return 100
}
复制代码


45、switch case default用法
复制代码
switch i {
    case 0:
        fmt.Printf("0")
    case 1:
        fmt.Printf("1")
    case 2:
        fallthrough
    case 3:
        fmt.Printf("3")
    case 4, 5, 6:
        fmt.Printf("4, 5, 6")
    default:
        fmt.Printf("Default")
}
复制代码

46、Go语言的goto 和break Label更加的灵活处理 循环和跳转

47、自定义复杂数据类型
type Info struct{
    name string
    age  int8
}
48、关于函数返回 一个值和函数返回多个值
复制代码
package main
import "fmt"
func ret1() int{
   return 1
}
func ret2()(a int,b int){
   a,b=1,2
   return
}

func main() {
    a,b:=ret2()
 fmt.Println(ret1(),a,b)
}
复制代码
48、Go的大小写规则
Go牢记这样的规则：小写字母开头的函数只在本包内可见，大写字母开头的函数才能被其他包使用。
这个规则也适用于类型和变量的可见性。

49、函数的不定参数  实际上是一种"语法糖"
复制代码
package main
import "fmt"
func show(args ...int){
    for _,val:= range args{
       fmt.Println(val)
    }
}
func main() {
    show(1,2,3)
}
复制代码
50、不定参数的传递   不定参数还可以传递给其他不定参数的 函数  并且可以打乱传递 ...
复制代码
unc myfunc(args ...int) {
    // 按原样传递
    myfunc3(args...)
    // 传递片段，实际上任意的int slice都可以传进去
    myfunc3(args[1:]...)
}
复制代码
51、// ...   传递任意类型的参数
复制代码
package main
import "fmt"
func Printfx(args ...interface{}) {
  for _,val:= range args{
       fmt.Println(val)
    }
}
func main() {
    Printfx(1,2,3,"adsd","sdaddf")
}
复制代码
52、Go的不定参数语法糖
Go的不定参数语法糖会把 参数构成一个数组切片 当然你直接传递  切片数组是不可以的,因为他的参数就是1,2,3,4,5,66,7,  但是我们可以通过...的方式打乱 数组 或者数组切片
...只可以打乱数组切片,常规数组是个值类型你是无法操作的

复制代码
package main
import "fmt"
func show(args ...int){
    for _,val:= range args{
       fmt.Println(val)
    }
}
// ...
func Printfx(args ...interface{}) {
  for _,val:= range args{
       fmt.Println(val)
    }
}
func main() {
    Printfx(1,2,3,"adsd","sdaddf")
    slice:=[]int{5,4,3,2,6,7,8}
    show(slice...)
}
复制代码
53、通过传递不定参数获取  任意类型不定参数的类型
复制代码
package main
import "fmt"
func checkType(args...interface{}){
    for _,val:=range args{
       switch val.(type){
          case int :
          fmt.Println("Type is int!")
          case string:
          fmt.Println("Type is string!")
          default:
          fmt.Println("Type is unknow!")
       }
    }
}
func  main() {
    checkType(1,2,3,"aaaa",int64(22))
}
复制代码
54、使用匿名函数和闭包     Go的匿名函数实际上就是闭包
复制代码
///定义匿名函数 并且调用
    funAdd:=func(a,b int)int{
       return a+b
    }
    r:=funAdd(11,22)
    fmt.Println("a+b=",r)
////定义 +调用匿名函数 一起
    r=func(a,b int)int{
          return a-b
      }(11,2)
    fmt.Println("a+b=",r)
////Go闭包 通过函数创建匿名函数 并且返回函数
package main
import "fmt"
func createFunc()(func(aa,bb,cc int) int){
    return func(aa,bb,cc int)int{
       return aa+bb+cc
    }
}
func  main() {
     add:=createFunc()
     addNum:=add(1,2,3)
     fmt.Println("addNum:",addNum)
}

package main

import (

"fmt"
)
///////函数的闭包定义 直接调用 .......闭包内部使用的代码块外部的变量 只要代码块没有释放那么变量不会被释放的
func main() {
    var j int = 5
    a := func()(func()) {
        var i int = 10
        return func() {
            fmt.Printf("i, j: %d, %d\n", i, j)
        }
    }()
    a()
    j *= 2
    a()
}
复制代码


55、函数多返回值
func ret()(int,int){
    return 1,2
}
 a,b:=ret()
 fmt.Println("a,b=",a,b)


56、对于结构类型空的值是nil

57、定义结构体一定要加 type,type和C/C++的 typedef 类似也可以 起别名
复制代码
package main
import "fmt"
type Data struct{
   name string
   age  int
}
func  main() {
    data:=Data{"a",1}
    fmt.Println(data)
}
///////////////////给结构体起个别名
package main
import "fmt"
type Data struct{
   name string
   age  int
}
type DData Data
func  main() {
    data:=DData{"a",1}
    fmt.Println(data)
}
复制代码

58、Go的defer和资源释放 相关问题   defer语句是按照 先进后出的原则,也就是说最后一个defer将会被先执行。
defer字面的意思是延迟执行,也就是说会在不需要的时候自动执行
而Go语言使用defer
关键字简简单单地解决了资源何时释放的问题，比如以下的例子：
复制代码
func CopyFile(dst, src string) (w int64, err error) {
    srcFile, err := os.Open(src)
    if err != nil {
        return
    }
    defer srcFile.Close()
    dstFile, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dstFile.Close()
    return io.Copy(dstFile, srcFile)
}
复制代码
即使其中的Copy()函数抛出异常，Go仍然会保证dstFile和srcFile会被正常关闭。
如果觉得一句话干不完清理的工作，也可以使用在defer后加一个匿名函数的做法：
defer func() {
    // 做你复杂的清理工作
} ()

另外，一个函数中可以存在多个defer语句，因此需要注意的是，defer语句的调用是遵照
先进后出的原则，即最后一个defer语句将最先被执行。只不过，当你需要为defer语句到底哪
个先执行这种细节而烦恼的时候，说明你的代码架构可能需要调整一下了

59、panic()和recover()
复制代码
////panic场景1
package main
import "fmt"
func  main() {
    defer func(){
       fmt.Println("hello,defer go")
    }()
    panic(11111)
}
////recover场景2
package main
import "fmt"
func  main() {
    defer func(){
       fmt.Println("hello,defer go")
    }()
    panic(11111)
}
复制代码

Go语言引入了两个内置函数panic()和recover()以报告和处理运行时错误和程序中的错误场景：
func panic(interface{})
func recover() interface{}
当在一个函数执行过程中调用panic()函数时，正常的函数执行流程将立即终止，但函数中之前使用defer关键字延迟执行的语句将正常展开执行，之后该函数将返回到调用函数，并导致逐层向上执行panic流程，直至所属的goroutine中所有正在执行的函数被终止。错误信息将被报告，包括在调用panic()函数时传入的参数，这个过程称为错误处理流程。
从panic()的参数类型interface{}我们可以得知，该函数接收任意类型的数据，比如整型、字符串、对象等。调用方法很简单，下面为几个例子：
panic(404)
panic("network broken")
panic(Error("file not exists"))
recover()函数用于终止错误处理流程。一般情况下，recover()应该在一个使用defer
关键字的函数中执行以有效截取错误处理流程。如果没有在发生异常的goroutine中明确调用恢复过程（使用recover关键字） ，会导致该goroutine所属的进程打印异常信息后直接退出。
以下为一个常见的场景。
我们对于foo()函数的执行要么心里没底感觉可能会触发错误处理，或者自己在其中明确加入了按特定条件触发错误处理的语句，那么可以用如下方式在调用代码中截取recover()：
复制代码
defer func() {
    if r := recover(); r != nil {
        log.Printf("Runtime error caught: %v", r)
    }
}()
foo()
复制代码
无论foo()中是否触发了错误处理流程，该匿名defer函数都将在函数退出时得到执行。假如foo()中触发了错误处理流程，recover()函数执行将使得该错误处理过程终止。如果错误处理流程被触发时，程序传给panic函数的参数不为nil，则该函数还会打印详细的错误信息。

60、panic()函数和recover()函数的调用具体区别在哪里
在panic()开始错误处理流程,传入的类型是interface{}任意类型  ,  如果我们在defer 函数中调用
recover()函数那么会打断错误处理流程。 panic的调用会终止正常的程序流程

recover()函数用于终止错误处理流程。一般情况下，recover()应该在一个使用defer
关键字的函数中执行以有效截取错误处理流程。如果没有在发生异常的goroutine中明确调用恢复
过程（使用recover关键字） ，会导致该goroutine所属的进程打印异常信息后直接退出。

复制代码
package main
import "fmt"
func  main() {
  //通过闭包定义 defer匿名函数 并且直接调用
    defer func(){
     //recover 结束当前错误处理过程  并且返回 panic的参数,并不结束其他goroutine的执行.......
       if r:=recover() ;r!=nil{
         fmt.Println("recover() called!")
       }
       fmt.Println("hello,defer go")
    }()
    panic("hello,go")
}
复制代码
61、关于const 和iota的使用
复制代码
package main
import "fmt"
var str string="aaa"
const(
  A=iota
  B
  C
)
func  main() {
  fmt.Println(B)
    defer func(){
       if r:=recover() ;r!=nil{
         fmt.Println("recover() called!")
         fmt.Println(r)
       }
       fmt.Println("hello,defer go")
    }()
    panic("hello,go")
}
复制代码

62、快速排序算法与数组切片的使用
复制代码
package main
import "fmt"
import "math/rand"
/////冒泡排序Go实现 时间复杂富 O(n)=n~n^2
func bubbledSort(values []int){
     var flags bool =true
     for i:=0 ;i<len(values);i++{
         flags=true
        for j:=0;j<len(values)-i-1;j++{
           if values[j]>values[j+1] {
              values[j],values[j+1]=values[j+1],values[j]
              flags=false
           }
        }
        if flags {
           break
        }
     }
}
///////快速排序Go实现
func quickSort(values []int,left,right int){
    temp := values[left]
    p := left
    i, j := left, right
    for i <= j {
        for j >= p && values[j] >= temp {
            j--
        }
        if j >= p {
            values[p] = values[j]
            p = j
        }
        if values[i] <= temp && i <= p {
            i++
        }
        if i <= p {
            values[p] = values[i]
            p = i
        }
    }
    values[p] = temp
    if p - left > 1 {
        quickSort(values, left, p - 1)
    }
    if right - p > 1 {
        quickSort(values, p + 1, right)
    }
}
func  main() {
    //创建初始化0个元素  容量1000的 切片 如果用索引直接访问切片会越界的  容量必须大于等于 初始化元素个数
    //val[1]=11
    val:=make([]int,0,1000)
    for i:=0;i<1000;i++{
      val=append(val,rand.Intn(1000))
    }
    fmt.Println("冒泡排序前:",val)
    bubbledSort(val)
    fmt.Println("冒泡排序后:",val)
}
复制代码

63、Go中的import和package 等等的关系
//import只是引入的文件夹而已,,,可以使用相对路径或者绝对路径
//他会把文件夹中的所有.go文件引入 ,,,,,,
///package xx 实际上是 在外不用调用用的 比如xx.A() 并不是给import使用   package内部的小写全部是私有 大写全部是公有
//外部包不能和主模块放到一起会编译不过的
import "./bubble"

