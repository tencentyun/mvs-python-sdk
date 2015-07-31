# qcloud_video-python
python sdk for [腾讯云微视频服务]

## 安装

### 使用pip
pip install qcloud_video

### 下载源码
从github下载源码装入到您的程序中，并加载qcloud_video包，依赖requests扩展包

## 修改配置
修改qcloud_video/conf.py内的appid等信息为您的配置

### 举例
```python

#下面接口中的 path 变量 可以为'/dir/test.mp4' 也可以为 'dir/test.mp4'，sdk会自动补齐

import qcloud_video as qcloud

video = qcloud.Video()	#使用conf.py中配置的信息
#video = qcloud.Video(appid,secret_id,secret_key)	#自己设置配置信息
obj = video.upload('test.mp4','bucket','dir/test.mp4')	
#obj = video.upload_slice('test.mp4','bucket','dir/test.mp4', 'title', 'desc', '', 3*1024*1024)	#分片上传，适用于较大视频
print obj

if obj['code'] == 0 :
    # 查询视频状态
    print video.statFile('bucket', 'dir/test.mp4')
    
    # 删除视频
    print video.deleteFile('bucket', 'dir/test.mp4')

#创建目录
obj = video.createFolder('bucket', '/firstDir/')
if obj['code'] == 0 :
    print video.upload('test.mp4', 'bucket', '/firstDir/firstfile.mp4')

#获取指定目录下视频列表
print video.list('bucket', '/firstDir/', 20, 'eListFileOnly')

#获取bucket下视频列表
print video.list('bucket', '/', 20, 'eListFileOnly')

#获取指定目录下以'abc'开头的视频
print video.prefixSearch('bucket', '/firstDir/', 'abc', 20, 'eListFileOnly')

#查询视频属性
print video.statFile('bucket', '/firstDir/firstfile.mp4')

#删除视频
print video.deleteFile('bucket', '/firstDir/firstfile.mp4')
```
