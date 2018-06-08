# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class RTPipeline(object):
    def __init__(self):
        #생성자에는 self를 이용해 변수를 만들고, csv모듈의 writer함수를 이용해서, csv파일을 열고 쓸 것이다.(없다면 생성)
        self.csvwriter = csv.writer(open("cafe_list.csv", "ab+"))
         
        #이 순서대로 csv파일의 열들을 채워넣는겠다는 의미로서, 열을 직접 입력해준다.
#        self.csvwriter.writerow( ["title", "url", "members", "contents", "news"] )

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["url"])
        row.append(item["members"])
        row.append(item["contents"])
        row.append(item["news"])
        row.append(item["count"])
        self.csvwriter.writerow( row )
        return item
