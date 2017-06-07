package main

import (
	"fmt"
)

func main(){
	fmt.Println("go"+"lang"+"  2017")   //字符串可以用+ 连接
	fmt.Println("10*11 =",10*11)
	//布尔型的几种操作符
	fmt.Println(true && false)   //  and
	fmt.Println(true || false) //  ||   or
	fmt.Println(!true)  //  ! 非
	fmt.Println(!false)
	// var 关键字用来定义一个或多个变量
	var a string = "Flying"
	fmt.Println("a:",a)
	//你一次可以定义多个变量
	var x,y,z int = 111,11,22
	fmt.Println("x+y+z:" + "",x,y,z,x+y+z)
	//go 会推断出具有初始值的变量类型
	var d = true
	fmt.Println("d:",d)
	//定义变量时，没有给出初始值的变量，默认初始值为零值，整型的零值就是0
	var e int
	fmt.Println("e:",e)
	//:= 语法是同时定义和初始化的快捷方式
	f := "eagle"
	fmt.Println("f:",f)
	//使用const 关键字来定义常量
	const s string = "constant"
	fmt.Println("s:",s)
	i :=1
	for i <=10{
		fmt.Println("i:",i)
		i = i+1   //i +=1  i++
	}
	for j :=5;j <=10;j++{   // 经典的循环条件初始化/条件判断/循环后条件变化
		fmt.Println("j:",j)
	}
	//无条件的for 循环是死循环，除非你使用break跳出循环或者使用return 从函数返回
	for {
		fmt.Println("for:","loop")
		break
	}
	var  aa int = 18
	if aa % 2 == 0 {
		fmt.Println("a is even",aa)
	}else {
		fmt.Println("a is odd!",aa)
	}
	num :=19
	if num <0{
		fmt.Println(num,"is negative")
	} else if num<10{
		fmt.Println(num,"has 1 digit")
	}else {
		fmt.Println(num,"has multiple digite")
	}
}