# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class DianpingItem(Item):
    shop_name = Field() #.shop-list
    shop_url = Field() #.shop-list
    shop_lev = Field() #.shop-list
    comment_num = Field()#.shop-list
    avg_cost = Field()#.shop-list
    shop_taste = Field() #.shop-list
    shop_env = Field() #.shop-list
    shop_service = Field() #.shop-list
    shop_tag = Field() #.shop-list .
    shop_tag_addr = Field()# .shop-list
    shop_addr = Field() #.shop-list

class UserCommentItem(Item):
    pass
