# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class QidianNewPipeline(object):
    print('This is a sample.\n')
    def process_item(self, item, spider):
        return item
