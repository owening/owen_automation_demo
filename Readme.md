# 简易版接口测试框架

##### Owen来给大伙介绍下


<br>

## 简介
- 使用的技术：pytest+requests+allure+yaml+Template+jsonpath+PyMySQL
- Log日志可以获取每个测试用例的请求参数、响应参数、数据库操作成功与失败的信息
- 利用Template技术，实现API请求+参数化断言+参数化用例标题的yaml数据驱动
- 解决api请求非必填参数的数据驱动，一个yml文件覆盖全部api参数
- 运用conftest+fixture，实现每一个用例不同的前置和后置需求，做到每个用例数据不冲突，实现并行运行
- 利用数据库封装的类，实现连接数据库进行数据操作，解决用例间简单的数据关联
  - 保存在yml文件，担心操作失误，导致数据清空
- 封装requests的方法，测试用例中，只需一行代码即可完成输入的请求参数，获得响应内容

<br>

<br>


## 使用指南 
- 安装的包在根目录的requirement,pip install -r requriements.txt即可安装
- config.ini的配置，在根目录下
  - 数据库，数据库涉及到的类在mysql的section
- allure的使用
  - 在项目根目录下，输入：pytest --alluredir=./report/result即可生成结果
  - 输入：allure serve ./report/result可临时查看结果
  - 输入：allure generate ./report/result -o report/result/html 生成永久报告，放到nginx服务器可查看
- 推荐观看代码的顺序，都是一步一步完善的过程
  - 先看common的三个公共类的实现
  - 再看api下业务模块类
  - test_case文件夹的顺序和api的顺序差不多


<br>

<br>


## 目录结构
#### api
- 作用：把所有发送请求和返回响应的api汇集在此
- base_api：所有api类的父类，实现了各种有用的方法
- 其他api类，比如fmp_member.py，表示新会员体系成员相关的api集合，每个方法表示每个api
#### log 
- 存放日志的文件夹
#### common
- 作用：汇集api和test_case需要用到的类和方法
- get_log:获取log的封装类，导入log变量，即可通过log.info(msg)获取文件和屏幕的日志
- config.py：读取配置文件的封装类，导入cf变量，即可通过cf.get(section,option)获取value
- conn_DB.py，连接和操作数据库，导入sql变量，
  - 即可通过sql.select(query)、sql.insert(query)、sql.delete(query)，对数据库进行增删查
#### test_case
- 作用：作为pytest架构的测试类
- 每个文件夹的文件
  - conftest.py：为每个用例添加不同的前后置步骤
  - test_xxxx.py：测试用例
#### data
- 作用：存放api请求的数据和参数化的数据
- 每个文件夹的文件
  - xxxx_api.yml：存放每一个类中的api请求数据，比如member的增删改查的api数据
  - xxx_para.yml：包含请求参数+断言+ids标题的参数化数据
#### config.ini文件：保存配置文件的数据
#### pytest.ini文件：pytest的配置文件


<br>

<br>

## 自动化项目编写规范

#### 一、项目模块划分
项目文件目录按业务模块进行划分，以订单模块为例如下，订单相关文件目录命名为order，对应的测试文件目录为test_order,目录下存放对应的模块接口请求定义文件和测试文件；例如：insure_order.py和test_insure_order.py<br />
#### 二、自动化脚本文件命名(统一使用下划线分隔)

1. 文件目录按模块名进行命名。例如order（订单）、underwriting（核保）,对应测试文件目录为 test_order、test_underwriting
1. 文件命名尽量简单易懂，例如：insure_order（投保订单）对应的测试文件名为 test_insure_order
1. 参数化数据文件命名：

请求参数文件命名(以_api结尾)为： insure_order_api<br />接口测试参数化数据文件命名(以_para结尾)：insure_order_data
#### 三、测试函数和测试用例函数名命名

1. 调用查询类接口函数命名为 :  query_xx() , 例如：投保订单查询  query_insure() 
1. 调用新增操作类接口函数命名为 :  add_xx() , 例如：新增成员  add_member() 
1. 调用修改更新操作类接口函数命名为 :  update_xx() , 例如：修改成员信息  update_member_info() 
1. 调用删除操作类接口函数命名为 :  delete_xx() , 
1. 例如：删除测试新增的无用费率模板 delete_fee_template() ----删除类接口谨慎调用

#### 四、测试用例断言规则

1. 接口请求的返回参数中包含业务数据时，优先以业务数据进行断言，例如请求中返回的具体的订单号，账户信息等
1. 当请求的返回参数没有返回具体的业务数据时，以响应code码和msg进行断言，如果没有msg可以使用success和code码进行断言

