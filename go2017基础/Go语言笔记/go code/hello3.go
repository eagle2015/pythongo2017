package main

import (
	"io"
	"log"
	"net/http"
)

func main(){
	mux :=http.NewServeMux()
	mux.Handle("/",&myHandler{})
	mux.HandleFunc("/hello",sayHello)
	err :=http.ListenAndServe(":8888",mux)
	if err !=nil{
		log.Fatal(err)
	}
}

type myHandler struct {}

func (*myHandler) ServeHTTP(w http.ResponseWriter,r *http.Request){
	io.WriteString(w,"URL:"+r.URL.String())
}
func sayHello(w http.ResponseWriter,r *http.Request){
	io.WriteString(w,"hello go, this is version 2")
}
