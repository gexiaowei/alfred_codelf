#!/usr/bin/python
#  -*- coding:utf-8 -*-
from __future__ import print_function
import sys
import requests
from workflow import Workflow

__author__ = "gexiaowei"
__version__ = "1.0"
__email__ = "gandxiaowei@gmail.com"
__status__ = "Development"

searchcode_open_api = 'https://searchcode.com/api/codesearch_I/'


def code_lf(query):
    print(query)
    response = requests.request('GET', searchcode_open_api, headers={}, params={"q": query, "p": 0, "per_page": 42, "lan": 22})
    print(response.text)
    return response.text


def main(wf):
    code_lf(wf)


if __name__ == '__main__':
    # code_lf('test')
    wf = Workflow()
    sys.exit(wf.run(main))
