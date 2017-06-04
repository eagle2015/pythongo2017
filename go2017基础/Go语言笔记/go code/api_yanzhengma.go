package main
import (
    "io/ioutil"
    "net/http"
    "net/url"
    "fmt"
    "encoding/json"
)

//----------------------------------
// 验证码识别调用示例代码 － 聚合数据
// 在线接口文档：http://www.juhe.cn/docs/60
//----------------------------------

const APPKEY = "*******************" //您申请的APPKEY

func main(){

    //1.识别验证码
    Request1()

    //2.查询验证码类型代码
    Request2()

}

//1.识别验证码
func Request1(){
    //请求地址
    juheURL :="http://op.juhe.cn/vercode/index"

    //初始化参数
    param:=url.Values{}

    //配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
    param.Set("key",APPKEY) //您申请到的APPKEY
    param.Set("codeType","") //验证码的类型，&lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;
    param.Set("image","") //图片文件
    param.Set("dtype","") //返回的数据的格式，json或xml，默认为json


    //发送请求
    data,err:=Post(juheURL,param)
    if err!=nil{
        fmt.Errorf("请求失败,错误信息:\r\n%v",err)
    }else{
        var netReturn map[string]interface{}
        json.Unmarshal(data,&netReturn)
        if netReturn["error_code"].(float64)==0{
            fmt.Printf("接口返回result字段是:\r\n%v",netReturn["result"])
        }
    }
}

//2.查询验证码类型代码
func Request2(){
    //请求地址
    juheURL :="http://op.juhe.cn/vercode/codeType"

    //初始化参数
    param:=url.Values{}

    //配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
    param.Set("key",APPKEY) //您申请到的APPKEY
    param.Set("dtype","") //返回的数据的格式，json或xml，默认为json


    //发送请求
    data,err:=Get(juheURL,param)
    if err!=nil{
        fmt.Errorf("请求失败,错误信息:\r\n%v",err)
    }else{
        var netReturn map[string]interface{}
        json.Unmarshal(data,&netReturn)
        if netReturn["error_code"].(float64)==0{
            fmt.Printf("接口返回result字段是:\r\n%v",netReturn["result"])
        }
    }
}



// get 网络请求
func Get(apiURL string,params url.Values)(rs[]byte ,err error){
    var Url *url.URL
    Url,err=url.Parse(apiURL)
    if err!=nil{
        fmt.Printf("解析url错误:\r\n%v",err)
        return nil,err
    }
    //如果参数中有中文参数,这个方法会进行URLEncode
    Url.RawQuery=params.Encode()
    resp,err:=http.Get(Url.String())
    if err!=nil{
        fmt.Println("err:",err)
        return nil,err
    }
    defer resp.Body.Close()
    return ioutil.ReadAll(resp.Body)
}

// post 网络请求 ,params 是url.Values类型
func Post(apiURL string, params url.Values)(rs[]byte,err error){
    resp,err:=http.PostForm(apiURL, params)
    if err!=nil{
        return nil ,err
    }
    defer resp.Body.Close()
    return ioutil.ReadAll(resp.Body)
}