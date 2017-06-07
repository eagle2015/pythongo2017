Go语言的面向对象编程

  Go语言的面向对象编程简单而干净,通过非侵入式接口模型,否定了C/C++ Java C#等传统面向对象编程语言的复杂度的必要性,
我们发现在Go中即使简单的组合也能达到传统面向对象语言的效果,而且耦合度非常低,按照Go的作者之一也就是C语言的作者之一说的一句话:Go是更好的C语言。
1、Go中任意类型Any即  interface{}类型,也就是空接口,可以赋值为任意类型
2、可以为其他类型 内置类型 不包括指针类型添加相应的方法 但是注意的一点是一定要用别名。。进行包装
记住想要 为类型 添加新的方法 那么请把类型定义别名,别名和原来的类型就不一样了成了新类型
在Go中只能对非本地类型添加方法......也就是int不能添加方法 需要 type Int int 才可以为Int添加方法
package main
import(
   "fmt"
)
type Integer int
func (a Integer) Less(b Integer)bool {
    return a<b
}
func main(){
   var a Integer=1
   r:=a.Less(2)
   fmt.Println(r)
}
/////用法2 组合之指针
package main
import(
   "fmt"
)
type Integer int
func (a *Integer) Less(b Integer)bool {
    *a-=10
    return *a<b
}

type Int int
func (a *Int) LessIne(b Int)bool{
    return *a<b
}
func main(){
   var a Integer=1
   var aa int=10
   a=Integer(aa)
   r:=a.Less(2)
   fmt.Println(r)
}

3、go中不存在this指针,通过语法糖显式传递对象
在Go语言中没有隐藏的this指针”这句话的含义是：
 方法施加的目标（也就是“对象” ）显式传递，没有被隐藏起来；
 方法施加的目标（也就是“对象” ）不需要非得是指针，也不用非得叫this。
4、用type定以后的别名类型就是新类型了 只有强制转换才能使用
package main
import(
   "fmt"
)
type Integer int
func (a Integer) Less(b Integer)bool {
    return a<b
}
func main(){
   var a Integer=1
   var aa int=10
   a=Integer(aa)  //不强制转换会编译出错的
   r:=a.Less(2)
   fmt.Println(r)
}
5、Go中的值语义和引用
channel map本质是指针 因为复制他们没有意义  ........数组切片 []type 本质上是值类型 interface接口非常重要
值语义和引用语义的差别在于赋值，比如下面的例子：
b = a
b.Modify()
如果b的修改不会影响a的值，那么此类型属于值类型。如果会影响a的值，那么此类型是引用
类型。
Go语言中的大多数类型都基于值语义，包括：
 基本类型，如byte、int、bool、float32、float64和string等；
 复合类型，如数组（array） 、结构体（struct）和指针（pointer）等。
Go语言中类型的值语义表现得非常彻底。我们之所以这么说，是因为数组。
如果读者之前学过C语言，就会知道C语言中的数组比较特别。通过函数传递一个数组的时
候基于引用语义， 但是在结构体中定义数组变量的时候基于值语义 （表现在为结构体赋值的时候，
该数组会被完整地复制） 。
Go语言中的数组和基本类型没有区别，是很纯粹的值类型，例如：
var a = [3]int{1, 2, 3}
var b = a
b[1]++
fmt.Println(a, b)
该程序的运行结果如下：
[1 2 3] [1 3 3]。
这表明b=a赋值语句是数组内容的完整复制。要想表达引用，需要用指针：
var a = [3]int{1, 2, 3}
var b = &a
b[1]++
fmt.Println(a, *b)
该程序的运行结果如下：
[1 3 3] [1 3 3]
这表明b=&a赋值语句是数组内容的引用。变量b的类型不是[3]int，而是*[3]int类型。
Go语言中有4个类型比较特别，看起来像引用类型，如下所示

数组切片：指向数组（array）的一个区间。
 map：极其常见的数据结构，提供键值查询能力。
 channel：执行体（goroutine）间的通信设施。
 接口（interface） ：对一组满足某个契约的类型的抽象。
但是这并不影响我们将Go语言类型看做值语义。下面我们来看看这4个类型。
数组切片本质上是一个区间，你可以大致将[]T表示为：
type slice struct {
    first *T
    len int
    cap int
}
因为数组切片内部是指向数组的指针，所以可以改变所指向的数组元素并不奇怪。数组切片
类型本身的赋值仍然是值语义。
map本质上是一个字典指针，你可以大致将map[K]V表示为：
type Map_K_V struct {

// ...
}

type map[K]V struct {
    impl *Map_K_V
}
基于指针，我们完全可以自定义一个引用类型，如：
type IntegerRef struct {
   impl *int
}
channel和map类似，本质上是一个指针。将它们设计为引用类型而不是统一的值类型的原因
是，完整复制一个channel或map并不是常规需求。
同样，接口具备引用语义，是因为内部维持了两个指针，示意为：
type interface struct {
    data *void
    itab *Itab
}
接口在Go语言中的地位非常重要。关于接口的内部实现细节，在后面的高阶话题中我们再
细细剖析。
7、Go语言中的结构体  组合非继承
Go语言的结构体（struct）和其他语言的类（class）有同等的地位，但Go语言放弃了包括继
承在内的大量面向对象特性，只保留了组合（composition）这个最基础的特性。
组合甚至不能算面向对象特性，因为在C语言这样的过程式编程语言中，也有结构体，也有
组合。组合只是形成复合类型的基础。
上面我们说到，所有的Go语言类型（指针类型除外）都可以有自己的方法。在这个背景下，
Go语言的结构体只是很普通的复合类型，平淡无奇。例如，我们要定义一个矩形类型：
type Rect struct {
    x, y float64
    width, height float64
}
然后我们定义成员方法Area()来计算矩形的面积：
func (r *Rect) Area() float64 {
    return r.width * r.height
}
可以看出， Go语言中结构体的使用方式与C语言并没有明显不同。
8、Go中的组合精华  创建结构体指针 和为 结构体扩充成员函数的时候.....传递 值类型和指针类型的区别
package main
import "fmt"
type Rect struct{
    x,y float64
    width,height float64
}
///如果写成rct Rect 那么内部的修改不会影响到 外部结构
///如果写成rct*Rect那么内部的修改会影响到外部结构的值 这就是 指针的效果
func (rct *Rect)Area() float64{
     rct.width=1000 ///也可以(*rct).width=1000一样
    return rct.width*rct.height
}
func main(){
     rct:=new(Rect)
//对于结构体指针,...调用方法和值类型一样直接.唯一的区别是 作为参数传递的时候 传递的是地址 值可以被修改
//所以进行组合的时候就有两种选择
   // 可以写成 var rct*Rect=&Rect{}
  //也可以写成 var rct Rect=Rect{}
 //var rct *Rect=new(Rect)
//也可以写成 var rct Rect=Rect{1,2,3,4}
     rct.width=10.0
     rct.height=10.0
     area:=rct.Area()
     fmt.Println(area)
     fmt.Println(rct.width)
}


9、普通的组合继承 ...........................以及组合指针继承 以及覆盖 和函数 成员名字冲突
//通过值类型继承
package main
import "fmt"
//Go中继承属于匿名组合 .......可以从对象继承 也可以从指针匿名继承...
//匿名继承会去掉包名,,,所以不能同时继承类名相同的  即使不在同一个包中
type Base struct{
    Name string
    Age  uint8
}
///为Base结构体组合进去两个函数
func (pBase*Base) showName(){
     fmt.Println("Age",pBase.Name)
}
func (pBase*Base) showAge(){
     fmt.Println("Age",pBase.Age)
}
//创建Sub结构体
type Sub struct{
    //组合Base修改内存模型
    //匿名组合进Base 对于调用者是不知道的
    //即使我们覆盖了 Base的方法 但是我们还是可以通过xxx.Base.xxx()调用基类的方法的
   //如果是*Base我们需要在调用处手动添加new Base 否则运行会出错的
    Base
}
func (pSub*Sub) showName(){
  fmt.Println("Before Sub ShowName")
    pSub.Base.showName()
    fmt.Println("After Sub ShowName")
}
func main(){
      obj:=new(Sub)
      obj.Name="张三"
      obj.Age=15
      obj.showName()
      obj.showAge()
}
///通过指针类型继承
package main
import "fmt"
//Go中继承属于匿名组合 .......可以从对象继承 也可以从指针匿名继承...
//匿名继承会去掉包名,,,所以不能同时继承类名相同的  即使不在同一个包中
type Base struct{
    Name string
    Age  uint8
}
///为Base结构体组合进去两个函数
func (pBase*Base) showName(){
     fmt.Println("Age",pBase.Name)
}
func (pBase*Base) showAge(){
     fmt.Println("Age",pBase.Age)
}
//创建Sub结构体
type Sub struct{
    //组合Base修改内存模型
    //匿名组合进Base 对于调用者是不知道的
    //即使我们覆盖了 Base的方法 但是我们还是可以通过xxx.Base.xxx()调用基类的方法的
    *Base
}
func (pSub*Sub) showName(){
  fmt.Println("Before Sub ShowName")
    pSub.Base.showName()
    fmt.Println("After Sub ShowName")
}
func main(){
      obj:=new(Sub)
    //由于使用指针继承所以 我们要设置匿名组合模板的内存对象 地址
      obj.Base=&Base{}
      obj.Name="张三"
      obj.Age=15
      obj.showName()
      obj.showAge()
}

10、Go语言的可见性 权限是包一级的,包外的不能访问包内的小写开头成员......包内无所谓

11、Go的非侵入式接口 和实现
/////Go语言会为每一个成员函数 自动生成对应的函数  比如 func(a *A) 会自动生成 func (a A) .....
///反过来则不行 因为 func (a A)这时候传递的是形参  (&a).xx()改变的是 参数 副本 而不是 外部类
package main
import "fmt"
///非侵入式接口
////接口 和实现完全分析 减少耦合
///实现方只负责实现  接口方只负责封装自己的借口就行...实现方甚至不知道 有这个接口的存在 这就是 Go的 非侵入式接口的特点
type IFly interface{
    fly()
}
type ISay interface{
    say()
}
type Bird struct{

}
//由于匿名传递进来的是指针类型 所对于接口的赋值必须是 指针
func (pBird*Bird) fly(){
   fmt.Println("i am a bird, i can fly()!")
}
//由于匿名传递的不是指针类型是值类型 所以接口赋值 可以不是指针而是值
func (pBird Bird) say(){
   fmt.Println("i am a bird, i can say()!")
}
func main(){
     birdObj:=Bird{}

     var iFly IFly=&birdObj
     iFly.fly()
     var iSay ISay=birdObj
     iSay.say()
}
13、接口之间是可以相互赋值的
实现了相同方法的接口可以相互赋值,如果接口B是A非超集,那么  A可以赋值为B
对象不可以被赋值为接口 ,繁殖接口可以被赋值为实现了 某些方法的对象 或者包含他方法的 接口对象
package main
import "fmt"
///非侵入式接口
////接口 和实现完全分析 减少耦合
///实现方只负责实现  接口方只负责封装自己的借口就行...实现方甚至不知道 有这个接口的存在 这就是 Go的 非侵入式接口的特点
type IFly interface{
    fly()
}
type ISay interface{
    say()
}
type IFly1 interface{
    fly()
}
type ISay1 interface{
    say()
}
type Bird struct{

}
//由于匿名传递进来的是指针类型 所对于接口的赋值必须是 指针
func (pBird*Bird) fly(){
   fmt.Println("i am a bird, i can fly()!")
}
//由于匿名传递的不是指针类型是值类型 所以接口赋值 可以不是指针而是值
func (pBird Bird) say(){
   fmt.Println("i am a bird, i can say()!")
}
func main(){
     birdObj:=Bird{}

     var iFly IFly=&birdObj
     iFly.fly()
     var iSay ISay=birdObj
     iSay.say()
     ////接口之间的赋值
     var iFly1 IFly1=iFly
     iFly1.fly()
}

14、Go中的值类型非常的彻底  数组都是值类型

15、关于给类型添加String()方法   相当于 其他语言的toString 用于打印输出
package main
import "fmt"
///非侵入式接口
////接口 和实现完全分析 减少耦合
///实现方只负责实现  接口方只负责封装自己的借口就行...实现方甚至不知道 有这个接口的存在 这就是 Go的 非侵入式接口的特点
type IFly interface{
    fly()
}
type ISay interface{
    say()
}
type IFly1 interface{
    fly()
}
type ISay1 interface{
    say()
}
type Bird struct{

}
//由于匿名传递进来的是指针类型 所对于接口的赋值必须是 指针
func (pBird*Bird) fly(){
   fmt.Println("i am a bird, i can fly()!")
}
//由于匿名传递的不是指针类型是值类型 所以接口赋值 可以不是指针而是值
func (pBird Bird) say(){
   fmt.Println("i am a bird, i can say()!")
}
func (pBird Bird) String() string{
   return "aaaaaaaaaa"
}
func main(){
     birdObj:=Bird{}

     var iFly IFly=&birdObj
     iFly.fly()
     var iSay ISay=birdObj
     iSay.say()
     ////接口之间的赋值
     var iFly1 IFly1=iFly
     iFly1.fly()
     fmt.Println(birdObj)
}

16、接口的组合 就是把多个接口组合到一起......接口中只有函数没有属性
type IFly interface{
    fly()
}
type ISay interface{
    say()
}
type IFly1 interface{
    fly()
}
type ISay1 interface{
    say()
}
type ISay_Fly interface{
    ISay
    IFly
}

17、接口查询 obj,ok=val.(Interface)   返回查询的接口 并且返回查询结果
x.(type) 获取类型 只能在switch中用
x.(OterTypeInterface) 判断x是否是指定接口类型 返回指定接口对象,和查询结果
在Go语言中，还可以更加直截了当地询问接口指向的对象实例的类型，例如：
var v1 interface{} = ...
switch v := v1.(type) {
    case int:    // 现在v的类型是int
    case string: // 现在v的类型是string
...
}
就像现实生活中物种多得数不清一样，语言中的类型也多得数不清，所以类型查询并不经常
使用。它更多是个补充，需要配合接口查询使用，例如：
type Stringer interface {
    String() string
}

func Println(args ...interface{}) {
    for _, arg := range args {
        switch v := v1.(type) {
            case int:                        // 现在v的类型是int
            case string:                     // 现在v的类型是string
            default:
            if v, ok := arg.(Stringer); ok { // 现在v的类型是Stringer
                val := v.String()
                // ...
            } else {
                // ...
            }
        }
    }
}
当然，Go语言标准库的Println()比这个例子要复杂很多，我们这里只摘取其中的关键部
分进行分析。对于内置类型，Println()采用穷举法，将每个类型转换为字符串进行打印。对
于更一般的情况，首先确定该类型是否实现了String()方法，如果实现了，则用String()方
法将其转换为字符串进行打印。否则，Println()利用反射功能来遍历对象的所有成员变量进
行打印。
是的，利用反射也可以进行类型查询，详情可参阅reflect.TypeOf()方法的相关文档。此
外，
18、 Any类型  对于匿名结构体赋值给任意类型  没法取出 具体每个匿名结构体的内部属性 只能前部打印 通过系统默认的String()函数
      var any1 interface{}=1
     var any2 interface{}="b"
     var any3 interface{}=struct{x ,y string}{"hello,world","aaaaa"}
     fmt.Println(any1,any2,any3)
由于Go语言中任何对象实例都满足空接口interface{}，所以interface{}看起来像是可
以指向任何对象的Any类型，如下：
var v1 interface{} = 1       // 将int类型赋值给interface{}
var v2 interface{} = "abc"   // 将string类型赋值给interface{}
var v3 interface{} = &v2     // 将*interface{}类型赋值给interface{}
var v4 interface{} = struct{ X int }{1}
var v5 interface{} = &struct{ X int }{1}
当函数可以接受任意的对象实例时，我们会将其声明为interface{}，最典型的例子是标
准库fmt中PrintXXX系列的函数，例如：
func Printf(fmt string, args ...interface{})
func Println(args ...interface{})
...
总体来说，interface{}类似于COM中的IUnknown，我们刚开始对其一无所知，但可以通
过接口查询和类型查询逐步了解它。
由于Go语言中任何对象实例都满足空接口interface{}，所以interface{}看起来像是可
以指向任何对象的Any类型，如下：
var v1 interface{} = 1       // 将int类型赋值给interface{}
var v2 interface{} = "abc"   // 将string类型赋值给interface{}
var v3 interface{} = &v2     // 将*interface{}类型赋值给interface{}
var v4 interface{} = struct{ X int }{1}
var v5 interface{} = &struct{ X int }{1}
当函数可以接受任意的对象实例时，我们会将其声明为interface{}，最典型的例子是标
准库fmt中PrintXXX系列的函数，例如：
func Printf(fmt string, args ...interface{})
func Println(args ...interface{})
...
总体来说，interface{}类似于COM中的IUnknown，我们刚开始对其一无所知，但可以通
过接口查询和类型查询逐步了解它。

