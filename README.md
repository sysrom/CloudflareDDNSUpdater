# CloudflareDDNSUpdater
A simple dynamic DNS updater
这个东西最早出来是因为Azure运行给机器分配带公网的动态IP,然后利用这个玩意就能用动态更新一个记录名的记录值了,V2的节点填写域名就能使了
## 食用教程
#### 安装CloudFlare模块
首先你需要安装cloudflare模块<br>
命令: `pip install cloudflare`
#### 获取区域ID与CFToken
然后去到你的CloudFlare仪表盘,点击你的域名进入这个域名的域(啊这,应该是这样表达吧)<br>
![图一](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF1.png)
滑到最下面看右边拦的API 把区域ID记好 要考<br>
然后点 **获取您的API令牌**
![图二](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF2.png)
进去之后,狂戳 **创建令牌**
![图三](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF3.png)
找到下面的 **API 令牌模板**,找到编辑区域DNS 点击旁边的使用模板
![图四](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF4.png)
里面要动的东西就一个 找到*区域资源*<br>
设置为 **包括 特定区域 你的域名** 然后别的都不用动
![图五](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF5.png)
点击 **继续以显示摘要** 然后继续点 **创建令牌**<br>
然后保存好你的令牌 这个玩意不会显示第二次！！！忘记了就再来一次吧（（（
#### 代码需要修改的地方
`Record_name` 填入你的记录名 Ps:例如你的域名是sysrom.xyz,记录名是test,此处就填test.sysrom.xyz 若你要修改的记录值为@就直接填你的一级域名就行<br>
`Cloudflare_Token` 填你的Cloudflare令牌<br>
`Cloudflare_Zone_ID` 填入你的Cloudflare区域ID<br>
填好了应该长这个样子<br>
`Record_name="test.sysrom.xyz"#记录名加域 例如域是sysrom.xyz 记录名是test 此处就填test.sysrom.xyz`
`Cloudflare_Token="fU-5b*************************XYN"#你觉得这是什么就是什么别问我`
`Cloudflare_Zone_ID="40********************0b"`
`IPAddress=""#填了就傻逼`
#### 运行(正常人谁看啊)
`python main.py`
