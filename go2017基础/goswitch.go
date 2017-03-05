package main

import (
	//"time"
	"fmt"
	"time"
)
func main(){
	//基础的switch语法：
	i :=1
	fmt.Print("write  ", i ," as")
	switch i {
	case 1:
		fmt.Println("  one",i)
	case 2:
		fmt.Println("  two",i)
	case 3:
		fmt.Println("   three",i)
	}
	//当case都没有满足的时候，执行default所指定的模块
	switch time.Now().Weekday() {
	case time.Saturday,time.Sunday:
		fmt.Println("it's is weekend")
	default:
		fmt.Println("it's a weekday!",time.Now().Weekday())
	}
	t :=time.Now()
	switch  {
	case t.Hour()<12:
		fmt.Println(t.Hour(),"it's before noon")
	default:
		fmt.Println(t.Hour(),"it's after noon")

	}
}