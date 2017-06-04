//代码描述：基于GO的历史上的今天api调用代码实例

package main
import (
    "io/ioutil"
    "net/http"
    "net/url"
    "fmt"
    "encoding/json"
)

//----------------------------------
// 历史上的今天调用示例代码 － 聚合数据
// 在线接口文档：http://www.juhe.cn/docs/63
//----------------------------------

const APPKEY = "CCPK66YDDTD2" //您申请的APPKEY

func main(){

    //1.事件列表
    Request1()

    //2.根据ID查询事件详情
    Request2()

}

//1.事件列表
func Request1(){
    //请求地址
    juheURL :="http://api.juheapi.com/japi/toh"

    //初始化参数
    param:=url.Values{}

    //配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
    param.Set("key",APPKEY) //应用APPKEY(应用详细页查询)
    param.Set("v","") //版本，当前：1.0
    param.Set("month","") //月份，如：10
    param.Set("day","") //日，如：1


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

//2.根据ID查询事件详情
func Request2(){
    //请求地址
    juheURL :="http://api.juheapi.com/japi/tohdet"

    //初始化参数
    param:=url.Values{}

    //配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
    param.Set("key",APPKEY) //应用APPKEY(应用详细页查询)
    param.Set("v","") //版本，当前：1.0
    param.Set("id","") //事件ID


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
