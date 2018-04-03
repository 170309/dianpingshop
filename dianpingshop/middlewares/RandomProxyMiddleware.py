#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-29 下午12:10
# @Author  : do_something
# @Site    : 
# @File    : middlewares.py
# @Software: PyCharm

"""
 use other repository
"""
import requests


def get():
    return requests.get("http://tvp.daxiangdaili.com/ip/?tid=557856587961654&num=1&delay=4&protocol=https").content


class RandomProxyMiddleware(object):

    def __init__(self, crawler):
        super(RandomProxyMiddleware, self).__init__()
        r = get()
        i = r.split(":")[0]
        p = r.split(":")[1]
        self.proxy_url = "https://{0}:{1}".format(i, p)
        self.ip_ = i
        self.port_ = p
        self.count = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        self.count = self.count + 1
        if self.count > 3:
            r = get()
            i = r.split(":")[0]
            p = r.split(":")[1]
            self.proxy_url = "https://{0}:{1}".format(i, p)
            self.count = 0
        request.meta['proxy'] = self.proxy_url
        print self.proxy_url
        # return request
