# README

## 使用指南

### 目录介绍

```tree
├─cases
│  ├─AICardProject ----- AIcard项目组用例文件
│  │  ├─case
│  │  ├─data
│  │  ├─logic
│  │  └─page
│  └─DemoProject ----- Demo项目组用例文件
│      ├─case
│      ├─data
│      ├─logic
│      ├─page
├─conf -----配置文件，用于控制执行用例的参数（例如接收邮箱设置，重跑设置，项目介绍等）
├─outputs ----- 每次用例执行后的执行结果（包括json格式、html格式报告、错误截图）
│  ├─AICardProject
│  │  ├─20200518150459
│  └─DemoProject
│      └─20200518150248
├─template ----- 邮件报告模板
├─myweb ----- 支撑框架的脚本文件
├─run.py ----- 执行文件

```

**cases**

这个目录用于存放项目的用例文件，形式建议基于PO模式（page-object），case目录下的用例脚本需要基于继承于myweb.core.runner文件下的My4wTestCase

```tree
├─cases
│  ├─DemoProject ----- 项目组名称（可以自定义名称，后续都称之为ProjectName）
│  │  ├─case ----- 用例脚本存放的位置
│  │  ├───test_testcase.py ----- 用例脚本必须以test开头，因为需要识别（后期可能会开放匹配方式，支持更多匹配）
│  │  ├─data
│  │  ├─logic
│  │  └─page
```

```python
# -*- encoding=utf8 -*-
from myweb.core.runner import My4wTestCase

class DemoTestCase(My4wTestCase):
    __author__ = "zero"

    def test_case_01(self):
        pass
```

**conf**

这个目录存储各个项目用例的配置信息，定制化项目的执行用例方式。

```tree
─conf
───demo.json ----- demo项目组的配置文件（文件名可以自定义）
───aicard.json ------ aicard项目组的配置文件
```

```json
{
    "project_name": "AICardProject", //必须要配置，这里指定项目名称（ProjectName），用于后续匹配执行用例的目录
    "project_name_zh": "AI云店Web自动化项目", //报告中标题可能会拉取这个名称，如果没有就给默认名称，或者为空
    "desc": "这里是描述",//报告中描述信息可能会拉取这个信息，如果没有就给默认信息，或者为空
    "report_mode": true,//是否开启报告，如果开启则生成html详细报告
    "email_mode": true,//是否开启邮件提醒，如果开启则发送简版报告至邮箱
    "retry": 3,//是否开启重试机制，如果填写大于0的数则开启，某个用例失败时会重跑相应次数，执行成功用例标记为成功，执行失败相应次数用例会标记为失败
    "receiver": [
        "chenyz01@mingyuanyun.com",
        "zhengw@mingyuanyun.com"
    ]//接收邮件人列表，如果没有或者为空，则不会发送
}
```

**run.py**

```python
from myweb.core.runner import Runner


if __name__ == '__main__':
    # 指定项目的配置文件名称，这里不需要写全路径，会自动匹配
    config_path = "aicard.json" 
    r = Runner(config_path=config_path)
    r.run()
```

运行时，需要在run.py文件中修改指定的配置路径。后期可能会优化运行方式（支持命令行运行/脚本运行），让其更加简洁。

### 配置文件介绍

```json
{
    "project_name": "AICardProject", //必须要配置，这里指定项目名称（ProjectName），用于后续匹配执行用例的目录
    "project_name_zh": "AI云店Web自动化项目", //报告中标题可能会拉取这个名称，如果没有就给默认名称，或者为空
    "desc": "这里是描述",//报告中描述信息可能会拉取这个信息，如果没有就给默认信息，或者为空
    "report_mode": true,//是否开启报告，如果开启则生成html详细报告
    "email_mode": true,//是否开启邮件提醒，如果开启则发送简版报告至邮箱
    "retry": 3,//是否开启重试机制，如果填写大于0的数则开启，某个用例失败时会重跑相应次数，执行成功用例标记为成功，执行失败相应次数用例会标记为失败
    "receiver": [
        "chenyz01@mingyuanyun.com",
        "zhengw@mingyuanyun.com"
    ],//接收邮件人列表，如果没有或者为空，则不会发送
    "screen": ["fail", "click", "..."],
    "mark": true,
    "driver_always_open": true,
    "auto_open_driver": true
}
```

project_name: 项目名称，对应的是cases下创建目录时取的名称，用于匹配用例所在项目目录。

project_name_zh: 项目中文名称，用于邮件/报告中呈现。

desc: 项目描述，用于邮件/报告中呈现。

report_mode: 报告模式布尔值，默认关闭。如果设置成false则不生成详细html报告。

email_mode: 报告模式布尔值，默认关闭。如果设置成false则不生成详细html报告。

retry: 重试次数，默认关闭，整数类型。如果设置大于0，则某个用例失败时会默认重跑指定次数，只要有一次成功则记为成功。

receiver: 邮件接收人列表，列表类型。

screen：截图设置。暂时只支持失败截图，只需要在配置列表中增加["fail"]标识，在用例失败时就会截图（前提是编写用例时设置了正确的self.driver）。

mark:是否高亮选择/点击元素

driver_always_open:是否需要浏览器执行后不关闭

auto_open_driver:是否打开webDriver # 启动driver的方法写在My4wTestCase.setUpClass

持续补充...

### 使用方式

#### 第一步：新增项目（针对新接入的项目）

1. 在cases目录下新建一个文件夹，以自己组名命名（不能为中文，例如AICardProject）
2. 在刚才新建的文件夹下，再新建一个名为case的文件（用于存放.py文件的用例文件）
3. 在conf目录下新建一个配置文件，以自己组名命名，后缀为.json（例如AiCard.json）

#### 第二步：用例执行配置

1. 在第一步中新建的.json文件中添加基础配置(详细配置参考[配置文件介绍](#配置文件介绍))
```json
{
    "project_name": "AICardProject",
    "project_name_zh": "AI云店Web自动化项目",
    "desc": "这里是描述",
    "report_mode": true,
    "email_mode": true,
    "retry": 3,
    "receiver": [
        "chenyz01@mingyuanyun.com",
        "zhengw@mingyuanyun.com"
    ]
}
```
2. 设置根目录 run.py文件中的config_path路径为第一步新建的.json文件路径
```python
config_path = "AiCard.json"
```

#### 第三步：查看用例运行日志/报告/邮件

如果前面配置文件设置了报告/邮件模式开启、且添加接收人邮箱，则会收到运行报告邮件。其他的日志、报告等可以在outputs目录下查看，根据项目名/时间戳存储。

```tree
├─outputs
│  ├─AICardProject
│  │  ├─20200518150459
```


## 开发过程中一些笔记

### 开启静态服务器

```shell
py -3 -m http.server 8080 -d outputs
```

1、存放html报告
2、存放image，失败截图等
3、存放json格式报告

### 步骤截图

遇到的问题：因为result.json是在每个py用例文件执行完毕之后才填写的，所以会导致无法实时向里面填充数据。

目前预设方案：
1、在storage文件中记录大量操作日志，最后在tearDownClass时插入数据

方案1的步骤：
1、storage中使用info记录具体某个py文件的用例操作的数据
2、tearDownClass时插入缓存的记录
3、步骤2完成后，清除info数据

### 单个用例执行（直接执行test.py文件）

描述：为了满足调试时单个test_*.py文件执行（而不是使用runner.run），需要有一个专门的文件夹存放这些调试用例结果集。

目前方案：
1、在runner中默认一个配置文件，暂时称为single.json
2、single.json中配置相关的配置信息（例如操作步骤截图配置，支持到最大）

### 重跑机制

#### 失败立即重跑

描述：设置3次失败重跑，每个用例失败3次才会真正记做失败

方案：run() 之后直接读取失败用例，重新执行，再将结果写入结果集

#### 暴露重跑

描述：暴露单个/所有 失败用例重跑的途径

方案：在静态服务器中加载bash脚本
