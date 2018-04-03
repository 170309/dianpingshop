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
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):

    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')
        self.count = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        user_agent = get_ua()
        request.headers.setdefault('User-Agent', user_agent)
        # return request
