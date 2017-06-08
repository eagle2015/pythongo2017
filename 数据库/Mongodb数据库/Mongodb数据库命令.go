package Mongodb数据库
数据库基本命令操作

数据库常用命令
1、Help查看命令提示

 help

  db.help();

  db.yourColl.help();

  db.youColl.find().help();

  rs.help();

2、切换/创建数据库

 use yourDB;  当创建一个集合(table)的时候会自动创建当前数据库

3、查询所有数据库

 show dbs;

4、删除当前使用数据库

 db.dropDatabase();

5、从指定主机上克隆数据库

 db.cloneDatabase(“127.0.0.1”); 将指定机器上的数据库的数据克隆到当前数据库

6、从指定的机器上复制指定数据库数据到某个数据库

 db.copyDatabase("mydb", "temp", "127.0.0.1");将本机的mydb的数据复制到temp数据库中

7、修复当前数据库

 db.repairDatabase();

8、查看当前使用的数据库

 db.getName();

 db; db和getName方法是一样的效果，都可以查询当前使用的数据库

9、显示当前db状态

 db.stats();

10、当前db版本

 db.version();

11、查看当前db的链接机器地址

 db.getMongo();

Collection聚集集合
1、创建一个聚集集合（table）

 db.createCollection(“collName”, {size: 20, capped: 5, max: 100});

2、得到指定名称的聚集集合（table）

 db.getCollection("account");

3、得到当前db的所有聚集集合

 db.getCollectionNames();

4、显示当前db所有聚集索引的状态

 db.printCollectionStats();

 用户相关
1、添加一个用户

 db.addUser("name");

 db.addUser("userName", "pwd123", true); 添加用户、设置密码、是否只读

2、数据库认证、安全模式

 db.auth("userName", "123123");

3、显示当前所有用户

 show users;

4、删除用户

 db.removeUser("userName");

错误信息操作
1、查询之前的错误信息
 db.getPrevError();
2、清除错误记录
 db.resetError();

查看聚集集合基本信息
1、查看帮助  db.yourColl.help();
2、查询当前集合的数据条数  db.yourColl.count();
3、查看数据空间大小 db.userInfo.dataSize();
4、得到当前聚集集合所在的db db.userInfo.getDB();
5、得到当前聚集的状态 db.userInfo.stats();
6、得到聚集集合总大小 db.userInfo.totalSize();
7、聚集集合储存空间大小 db.userInfo.storageSize();
8、Shard版本信息  db.userInfo.getShardVersion()
9、聚集集合重命名 db.userInfo.renameCollection("users"); 将userInfo重命名为users
10、删除当前聚集集合 db.userInfo.drop();

索引操作
1、创建索引
db.userInfo.ensureIndex({name: 1});
db.userInfo.ensureIndex({name: 1, ts: -1});

2、查询当前聚集集合所有索引
db.userInfo.getIndexes();

3、查看总索引记录大小
db.userInfo.totalIndexSize();

4、读取当前集合的所有index信息
db.users.reIndex();

5、删除指定索引
db.users.dropIndex("name_1");

6、删除所有索引索引
db.users.dropIndexes();


查询操作

Mongodb-SpringMvc下Query数据库操作SQL
http://blog.csdn.net/xiaohulunb/article/details/27828381

1.查询所有
> db.foo.find()
{ "_id" : ObjectId("5389aa1df06b88aaa313746a"), "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "_id" : ObjectId("5389aaa4afce65313a5614f7"), "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "_id" : ObjectId("5389aabaafce65313a5614f8"), "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "_id" : ObjectId("5389aac5afce65313a5614f9"), "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
2.显示指定列
 第一个{} 放where条件 第二个{} 指定哪些列显示和不显示 （0表示不显示 >0表示显示)

后面演示使用{'_id':0} 默认隐藏‘_id列’减少显示量

> db.foo.find({},{'_id':0,'name':1,'user':1})
{ "name" : "yiwa", "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "user" : { "phone" : [ 63, 137 ] } }
3.使用and操作
#名字是yiwa且年龄是25岁


> db.foo.find({'name':'yiwa','age':25},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
4.使用or操作
#名字是yiwa或者年龄是75岁

> db.foo.find({'$or':[{'name':'yiwa'},{'age':75}]},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
5.使用<, <=, >, >= ($lt, $lte, $gt, $gte )操作，取模运算$mod
#年龄在 15<= x <=75 岁


> db.foo.find({'age':{'$gte':15,'$lte':75}},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
# 对age%3==1的取模结果


> db.foo.find({'age':{'$mod':[3,1]}},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
6.使用in, not in ($in, $nin)
#名字不是siwa且年龄在[15，25，85]
> db.foo.find({'name':{'$nin':['siwa']},'age':{'$in':[15,25,85]}},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
7.匹配null操作
#名字是null的
> db.foo.find({'name':null},{'_id':0})
>
8.使用like (mongoDB 支持正则表达式)
#名字like%iwa%的
#名字like  yi%的
> db.foo.find({'name':/iwa/},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.find({'name':/^yi/},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
9.使用distinct、count查询
> db.foo.distinct('name')
[ "yiwa", "erwa", "sanwa", "siwa" ]
> db.foo.count()
4
#distinct结合条件，排序使用


> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 95, "user" : { "phone" : [ 123, 133, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 133, 137, 186 ] } }
> db.foo.distinct("age",{'user.phone':{'$in':[63,65,186]}}).sort({'age':1})
[ 25, 85, 95 ]
> db.foo.distinct("age",{'user.phone':{'$in':[63,65,186]}}).sort({'age':-1})
[ 25, 85, 95 ]
> db.foo.distinct("age",{'user.phone':{'$in':[63,65,186]}})
[ 25, 95, 85 ]
待解疑问：？为什么 排序时候 age ：-1 与 age ：1 结果一样？

10.数组查询 （mongoDB自己特有的）（all,size）
#电话中含有186的
> db.foo.find({'user.phone':186},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
#电话中含有188，186的
> db.foo.find({'user.phone':{'$all':[188,186]}},{'_id':0})
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
#电话中有2个值的
> db.foo.find({'user.phone':{'$size':2}},{'_id':0})
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
11.exists判断是否存在，type判断类型,Sort排序
#name中值是字符型，age中值是整型，按name升序，age降序
> db.foo.find({'name':{'$type':2},'age':{'$type':16}},{'_id':0}).sort({'name':1,'age':-1})
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
#name中值存在的：true
#name中值不存在的：false
> db.foo.find({'name':{'$exists':true}},{'_id':0})
{ "name" : "yiwa", "age" : 25, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.find({'name':{'$exists':false}},{'_id':0})
>
12.$elemMatch数组元素匹配
#插入测试数据
> db.foo.save({x:[{'a':1,'b':5},999,'liw',{'a':12},{'b':100}]})
WriteResult({ "nInserted" : 1 })
#查询某元素中a=1，b=5的元素
> db.foo.find({'x':{'$elemMatch':{'a':1,b:{'$gt':4}}}},{'_id':0})
{ "x" : [ { "a" : 1, "b" : 5 }, 999, "liw", { "a" : 12 }, { "b" : 100 } ] }
> db.foo.find({'x.a':1,'x.b':5},{'_id':0})
{ "x" : [ { "a" : 1, "b" : 5 }, 999, "liw", { "a" : 12 }, { "b" : 100 } ] }



更新操作
1.update( criteria, objNew, upsert, multi)、save() 方法
criteria : update的查询条件，类似sql update查询内where后面的
objNew   : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
upsert   : 这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
multi    : mongodb默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
save()方法相当于upsert与multi 都为true时候
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 55, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.update({'age':{$gte:30}},{$set:{'age':55}},fasle,false)
2014-05-31T19:36:05.407+0800 ReferenceError: fasle is not defined
> db.foo.update({'age':{$gte:30}},{$set:{'age':55}},false,false)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 0 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 55, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.update({'age':{$gte:30}},{$set:{'age':56}},false,false)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 56, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.update({'age':{$gte:300}},{$set:{'age':56}},true,false)
WriteResult({
	"nMatched" : 0,
	"nUpserted" : 1,
	"nModified" : 0,
	"_id" : ObjectId("5389bee8afce65313a5614fa")
})
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 56, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 75, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 85, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
{ "age" : 56 }
> db.foo.update({'age':{$gte:30}},{$set:{'age':56}},true,true)
WriteResult({ "nMatched" : 4, "nUpserted" : 0, "nModified" : 2 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 56, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 56, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
{ "age" : 56 }
2.$inc 对于数字字段的值增加value
#年龄大于30的 全部age值增加20
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 58, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 56, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.update({'age':{$gte:30}},{$inc:{'age':20}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 78, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 56, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
3.$set 相当于sql的set field = value
#年龄=56的，设置为名字='laoda',年龄=65
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 78, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "erwa", "age" : 56, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
> db.foo.update({'age':56},{$set:{'name':'laoda','age':65}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 78, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "laoda", "age" : 65, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
#只更新了一条数据，因为 multi 默认为false
4.$unset 删除字段
#查询name='laoda',user字段存在的数据中，删除age=65的age字段
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 78, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "laoda", "age" : 65, "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
{ "age" : 65, "name" : "laoda" }
> db.foo.update({'name':'laoda','user':{$exists:true}},{$unset:{"age":65}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.foo.find({},{'_id':0})
{ "name" : "yiwa", "age" : 78, "user" : { "phone" : [ 123, 13, 186 ] } }
{ "name" : "laoda", "user" : { "phone" : [ 63, 188, 13, 186 ] } }
{ "name" : "sanwa", "age" : 56, "user" : { "phone" : [ 186 ] } }
{ "name" : "siwa", "age" : 15, "user" : { "phone" : [ 63, 137 ] } }
{ "age" : 65, "name" : "laoda" }
5.$push 数组下操作
#把value追加到field里面去，field一定要是数组类型才行，如果field不存在，会新增一个数组类型加进去
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda" }
> db.array.update({'name':'laoda','age':65},{$push:{"phone":65}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 65 ] }
> db.array.update({'name':'laoda','age':65},{$push:{"phone":[65,75,{'iphone':'188'},85]}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 65, [ 65, 75, { "iphone" : "188" }, 85 ] ] }
6.$pushAll 数组下操作
#一次可以追加多个值到数组
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda" }
> db.array.update({'name':'laoda','age':65},{$pushAll:{"phone":[111,222]}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222 ] }
> db.array.update({'name':'laoda','age':65},{$pushAll:{"phone":[111,222]}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222 ] }
7.$addToSet 数组操作
#增加一个值到数组内，而且只有当这个值不在数组内才增加
#插入2次发现，此值存在的时候不插入
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ] ] }
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ] ] }
> db.array.update({'name':'laoda','age':65},{$addToSet:{"phone":333}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ], 333 ] }
> db.array.update({'name':'laoda','age':65},{$addToSet:{"phone":333}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 0 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ], 333 ] }
8.$pop 删除数组内的一个值
#删除最后一个值：{ $pop : { field : 1 } }删除第一个值：{ $pop : { field : -1 } }
注意，只能删除一个值，也就是说只能用1或-1，而不能用2或-2来删除两条
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ], 333 ] }
> db.array.update({'name':'laoda','age':65},{$pop:{"phone":1}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 222, 111, 222, [ 111, 222 ] ] }
> db.array.update({'name':'laoda','age':65},{$pop:{"phone":-1}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 222, 111, 222, [ 111, 222 ] ] }
> db.array.update({'name':'laoda','age':65},{$pop:{"phone":2}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 222, 111, 222 ] }
> db.array.update({'name':'laoda','age':65},{$pop:{"phone":333}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 222, 111 ] }
> db.array.update({'name':'laoda','age':65},{$pop:{"phone":-333}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111 ] }
#测试发现，只要是正整数从最后删除，负数从头部删除。
9.$pull 数组field内删除一个等于value值
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 333 ] }
> db.array.update({'name':'laoda','age':65},{$pull:{"phone":333}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111 ] }
10.$pullAll 数组field内删除多个值
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 111, 333, 222 ] }
> db.array.update({'name':'laoda','age':65},{$pullAll:{"phone":[111,222]}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.array.find({},{'_id':0})
{ "age" : 65, "name" : "laoda", "phone" : [ 333 ] }
