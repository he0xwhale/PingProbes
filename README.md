# PingProbes
一个基于python2的使用ping方式多进程探测多IP存活项目，可以通过邮件等方式来通知IP异常情况。可以用于IT运维等多场景中。
## Get Started
1. Clone repo

    ```bash
    git clone https://github.com/he0xwhale/PingProbes.git
    cd PingProbes
    ```
2. 运行main.py
    ```bash
    python main.py
    ```
## 配置文件说明
### config.json
- 文件路径：`config/config.json`
- 配置项：
    - duration: ping的检测周期，单位为s
    - heartBeat: 该功能主要是为了防止检测进程意外中断，周期性的发送邮件到监测邮箱
        - enable: 是否开启心跳检测
        - intervalTime: 心跳检测间隔周期
    - email：邮件通知
        - enable: 是否开启邮箱通知
        - addr: 邮件接收地址，可以发送邮件到多个邮箱
    - smtp: 邮箱smtp设置
        - sender：邮件发送者地址
        - server：SMTP服务器地址
        - port：SMTP服务器端口
        - username：用户名
        - password：密码
### ip.list
- 路径: `config/data/ip.list`
- 将需要监控的IP写入到这个文件中
## 进一步开发计划
将来可能根据需要不断改进
- 增加对csv文件格式的支持，设置多列，包括对IP的描述等
- 升级到Python3，当前由于Ping模块使用了python2，需要找到对应的python3版本，进行替换
- i18n 国际化
## More
欢迎star、fork、issue、pull request

有问题也可以发送邮件