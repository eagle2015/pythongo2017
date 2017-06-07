package Go语言笔记

import (
	"net/http"
	"log"
	"image/color"
	"math"
	"fmt"
	"strings"
	"io"
)


Go 没有类，但可以在结构体类型上定义方法。

复制代码
package main
import (
    "fmt"
    "math"
)

type Vertex struct { X, Y float64 }

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.Xv.X + v.Y*v.Y)
}

func main() {
    v := &Vertex{3, 4} fmt.Println(v.Abs())
}
复制代码


可以对包中的 任意 类型定义任意方法，而不仅仅是针对结构体。但是，不能对来自其他包的类型或基础类型定义方法。 接收者为指针的方法：方法可以与命名类型或命名类型的指针关联。有两个原因需要使用指针接收者：避免在每个方法调用中拷贝值（如果值类型是大的结构体的话会更有效率）；方法可以修改接收者指向的值。

复制代码
package main

import (
    "fmt"
    "math"
)

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0
    {
        return float64(-f)
    }
    return float64(f)
}

func main() {
    f := MyFloat(-math.Sqrt2)
    fmt.Println(f.Abs())
}
复制代码
接口：接口类型是由一组方法定义的集合。接口类型的值可以存放实现这些方法的任何值。

复制代码
package main

import ( "fmt" "math" )

type Abser interface { Abs() float64 }

func main() {
    var a Abser f := MyFloat(-math.Sqrt2)
    v := Vertex{3, 4}
    a = f  // a MyFloat 实现了 Abser
    a = &v // a *Vertex 实现了 Abser
    // 下面一行，v 是一个 Vertex（而不是 *Vertex）
    // 所以没有实现 Abser。
    a = v

    fmt.Println(a.Abs())
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0
    {
        return float64(-f)
    }
        return float64(f)
}

type Vertex struct { X, Y float64 }

func (v Vertex) Abs() float64
{
    return math.Sqrt(v.Xv.X + v.Y*v.Y)
}
复制代码
隐式接口：解藕了实现接口的包和定义接口的包：互不依赖。因此，也就无需在每一个实现上增加新的接口名称，这样同时也鼓励了明确的接口定义。

复制代码
package main

import ( "fmt" "os" )

type Reader interface { Read(b []byte) (n int, err error) }

type Writer interface { Write(b []byte) (n int, err error) }

type ReadWriter interface { Reader Writer }

func main() {

　　var w Writer

　　// os.Stdout 实现了 Writer
　　w = os.Stdout

　　fmt.Fprintf(w, "hello, writer\n")
}
复制代码
下面列举几个go标准包的接口：

type Stringer struct { String() string }

type error interface { Error() string }

io.Reader 接口有一个 Read 方法：

func (T) Read(b []byte) (n int, err error)

Read 用数据填充指定的字节 slice，并且返回填充的字节数和错误信息。

在遇到数据流结尾时，返回 io.EOF 错误。

复制代码
package main
import (
    "fmt"
    "io"
    "strings"
)

func main() {
    r := strings.NewReader("Hello, Reader!")

    b := make([]byte, 8)
    for {
        n, err := r.Read(b)
        fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
        fmt.Printf("b[:n] = %q\n", b[:n])
        if err == io.EOF {
            break
        }
    }
}
复制代码
Web服务器： 包 http 通过任何实现了 http.Handler 的值来响应 HTTP 请求：

 type Handler interface { ServeHTTP(w ResponseWriter, r *Request) }

复制代码
package main

import (
    "fmt"
    "log"
    "net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP( w http.ResponseWriter, r *http.Request) {
　　fmt.Fprint(w, "Hello!")
}

func main() {
    var h Hello err := http.ListenAndServe("localhost:4000", h)
    if err != nil
    {
        log.Fatal(err)
    }
}

复制代码
图片：

type Image interface { ColorModel() color.Model Bounds() Rectangle At(x, y int) color.Color }
