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
然后点*获取您的API令牌*
![图二](https://raw.githubusercontent.com/sysrom/CloudflareDDNSUpdater/master/img/CF2.png)
