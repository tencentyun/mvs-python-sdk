# -*- coding: utf-8 -*-

import time
import qcloud_video

appid = 'xxxx'
secret_id = 'xxxxx'
secret_key = 'xxxxxx'

# 上传
video = qcloud_video.Video(appid,secret_id,secret_key)
obj = video.deleteFile('bucket01', '123/a.mp4')

print obj, obj['message']
print '----------------------------------------------------------------------'

obj = video.upload('test.mp4','bucket01','123/a.mp4')
print obj, obj['message']
print '----------------------------------------------------------------------'

obj = video.createFolder('bucket01', 'python/')
print obj, obj['message']
print '----------------------------------------------------------------------'

obj = video.list('bucket01', '123/', 30)
print obj, obj['message']
print '----------------------------------------------------------------------'

obj = video.updateFolder('bucket01', '123/')
print obj, obj['message']
print '----------------------------------------------------------------------'
obj = video.statFile('bucket01', '123/a.mp4')

print obj, obj['message']
print '----------------------------------------------------------------------'
obj = video.deleteFile('bucket01', 'abc/a.mp4')

print obj, obj['message']
print '----------------------------------------------------------------------'

obj = video.upload_slice('test.mp4', 'bucket01', 'abc/a.mp4', 'title', 'desc', '', 2*1024*1024)
print obj, obj['message']
