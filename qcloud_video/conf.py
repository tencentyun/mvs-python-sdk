# -*- coding: utf-8 -*-
import pkg_resources
import platform

API_VIDEO_END_POINT = 'http://web.file.myqcloud.com/files/v1/'
APPID = '您的APPID'
SECRET_ID = '您的SECRETID'
SECRET_KEY = '您的SECRETKEY'

config = {
    'end_point':API_VIDEO_END_POINT,
    'appid':APPID,
    'secret_id':SECRET_ID,
    'secret_key':SECRET_KEY,
}

eMaskBizAttr = 1 << 0
eMaskTitle = 1 << 1
eMaskDesc = 1 << 2
eMaskAll = eMaskBizAttr | eMaskTitle | eMaskDesc

def get_app_info():
	return config

def set_app_info(appid=None,secret_id=None,secret_key=None):
    if appid:
        config['appid'] = appid
    if secret_id:
        config['secret_id'] = secret_id
    if secret_key:
        config['secret_key'] = secret_key

def get_ua():
    version = pkg_resources.require("qcloud_video")[0].version
    return 'Qcloud-Video-PYTHON/'+version+' ('+platform.platform()+')';


