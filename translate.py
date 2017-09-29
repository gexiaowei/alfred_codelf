#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import print_function
import sys
import requests
import hashlib
import urllib
from workflow import Workflow

__author__ = "gexiaowei"
__version__ = "1.0"
__email__ = "gandxiaowei@gmail.com"
__status__ = "Development"

youdao_open_api = 'http://openapi.youdao.com/api'
youdao_app_id = '11aa8743c7548256'
youdao_app_secret = 'NAOO3PPYhA8VhPcOmdAK9at7BeyKQpv0'


def translate(query):
    salt = 'code_lf'
    print(youdao_app_id + query + salt + youdao_app_secret)
    sign = hashlib.md5(youdao_app_id + query + salt + youdao_app_secret).hexdigest()
    print(sign)
    response = requests.request("GET", youdao_open_api, headers={}, params={"q": query, "from": "auto", "to": "EN", "appKey": youdao_app_id, "salt": salt, "sign": sign})
    print(response.text)
    return response.text


def main(wf):
    args = wf.args
    keyword = urllib.quote_plus(args[0].encode('utf-8'))
    translate(keyword)


if __name__ == '__main__':
    # code_lf('test')
    wf = Workflow()
    sys.exit(wf.run(main))
