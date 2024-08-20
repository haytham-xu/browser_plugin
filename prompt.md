
#### receiver.py
```
写一个Flask的，监听一个路径“tabs”的POST请求，接收的url的json结构如下 
{
    tabs: [ 
        "https://baidu.com", 
        "https://bing.com", 
        "https://bing.com.cn" 
    ] 
} 
接收请求并打印tabs下的所有url 应该支持CORS

继续扩展这个应用，添加一个SQLite数据库，将接收到的tabs下的所有url存入数据库 具体的表结构如下： id, file_url, created_at, status, updated_at, type， file_name，retry_times，size 其中type默认使用 DOWLNOAD，status默认使用 TODO， file_name默认使用空字符串"", retry_times为0, file_url的值就是tab的url,size需要根据file_url获取文件的大小 对于每一个tab url, 首先检查数据库中是否存在， 如果存在，则不做任何操作, 否则插入到数据库中 在Python代码中创建一个对象来处理数据库操作，将数据库的连接放在对象的初始化方法中

拓展这个应用，添加一个下载器 应用应该维护一个字典记录当前下载文件的状态和进度 字典应该包含以下信息：file_name, status, size, progress 现在写一个定时器，每隔5秒钟触发一次，每次触发式 首先触发后检查数据库中的数据 如果status是TODO的，则将状态改为IN_PROGRESS 如果status是FAILED，则将状态改为IN_PROGRESS，则将retry_times加1 并将相关信息存进字典中，包括file_name, status, size, progress 然后启动一个线程开始下载这个url的内容，这个文件可能很大，所以要分片下载 下载的进度和状态要实时更新到字典中 文件应该下载到当前目录下的download文件夹下 下载完成后将状态改为DONE 应该有完善的异常处理代码来处理下载中的异常，如果下载出错或失败了，将status设置为FAILED，并打印提示和错误信息 然后然后按照如下格式打印字典中的信息：“download file: xxxx, size: xxx, progress: xxx”

不要遗漏任何的功能点，给出我完整的代码， 
尤其不要遗漏遗漏下载失败的处理代码 
think step by step
```
* `curl -X POST -H "Content-Type: application/json" -d '{"tabs":["https://baidu.com", "https://bing.com", "https://bing.com.cn"]}' http://127.0.0.1:5000/tabs`



#### Frontend
'''
帮我写一个Vue的项目，叫“frontend”
项目里UI上只有一个按钮“Get Tabs Url”,
这个项目是用在浏览器的插件里的
当点击这个URL的时候，获取当前浏览器所有的tab的url，并发送到http://127.0.0.1:5000/tabs POST
结构如下：
{
    tabs: [
        “TAB_URL_1”,
        “TAB_URL_2”
    ]
}
'''


#### 
'''
https://www.aaabbb.com/photos-slide-aid-254610.html
帮我写一段代码,解析这个url,分成 www.aaabbb.com和photos-slide-aid-254610.html


帮我写一段代码, 这段代码提供一个格式，这个格式会有两个用处
1. 从字符串提取出目标内容，举例如下：
photos-slide-aid-254610.html -> 254610
photos-slide-aid-61120.html -> 61120
photos-slide-aid-2451.html -> 2451
2. 提供关键字段，组合并输出，举例如下：
254610 -> photos-slide-aid-254610.html 
34534 -> photos-slide-aid-34534.html
1240 -> photos-slide-aid-1240.html

解析一个字符串的特定部分,举例如下: 
photos-slide-aid-254610.html -> 254610


photos-index-page-5-aid-255382.html
photos-index-aid-252050.html

'''
