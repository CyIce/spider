# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaikePipeline(object):
    def __init__(self):
        self.fout = open('output.html', 'w', encoding='utf-8')
        self.fout = open('output.html', 'w', encoding='utf-8')
        self.fout.write("<html>")
        self.fout.write("<body>")
        self.fout.write("<a>")

    def process_item(self, item, spider):
        self.fout.write('<p>%s</p>' % item['name'])
        self.fout.write('<a href="%s">%s</a>' % (item['url'], item['title']))
        return item

    def close_spider(self, spider):
        self.fout.write("</a>")
        self.fout.write("</body>")
        self.fout.write("</html>")
        self.fout.close()
