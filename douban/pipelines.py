# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from douban.utils.avos_manager import *

class DoubanPipeline(object):
    def __init__(self):
        self.avosManager = AvosManager()
        #self.res_dict = self.avosManager.getnfdict("activities")
        self.res_dict = {}

    #By Hushuying,generate footprint
    def gen_footprint(self,item):
        str_item = str(item['name'])+item['start_time']['iso']+\
                   item['region']+str(item['ticket'])+\
                   str(item['location']['latitude'])+\
                   str(item['location']['longitude'])+\
                   str(item['date']['iso'])
        return self.avosManager.calMD5(str_item)

    def process_item(self, item, spider):
        if spider.name not in ['damai','douban']:
            return item

        #init res_dict
        if len(self.res_dict) == 0:
            self.res_dict = self.avosManager.getnfdict("activities")

        print item['name']
        dataDict = {"name":item['name'],"date":item['date'],
                    "start_time":item['start_time'],"end_time":item['end_time'],"ticket":item['ticket'],
                    "region":item['region'],
                    "location":item['location'],
                    "category":item['category'],
                    "source" : item['source']}


        try:
            foot_print = self.gen_footprint(item)
            dataDict['foot_print'] = foot_print
            if not self.res_dict.has_key(item['name'].decode('utf-8')):
               self.avosManager.saveActivity(dataDict)
               print '插入数据'
            elif foot_print != self.res_dict[item['name'].decode('utf-8')]:
               self.avosManager.updateDataByName('activities',item['name'],dataDict)
               print '更新数据'
            else:
               print '已存在'
        except:
            print "avos exception!"

        return item


class DbMoviePipeline(object):
    def __init__(self):
        self.avosManager = AvosManager()
        #self.res_dict = self.avosManager.getnfdict("dbmovie")
        self.res_dict = {}

     #By Hushuying,generate footprint
    def gen_footprint(self,item):
        str_item = str(item['name'])+\
                   str(item['score'])+\
                   str(item['summary'])+\
                   str(item['poster'])+\
                   str(item['classification'])
        return self.avosManager.calMD5(str_item)

    def process_item(self, item, spider):
        if spider.name not in ['dbmovie']:
            return item

        #init res_dict
        if len(self.res_dict) == 0:
            self.res_dict = self.avosManager.getnfdict("dbmovie")

        print item['source']
        dataDict = {"name":item['name'],"score":item['score'],
                    "summary":item['summary'],
                    "classification":item['classification'],
                    "poster":item['poster'],
                    "source" : item['source']}


        try:
            foot_print = self.gen_footprint(item)
            dataDict['foot_print'] = foot_print

            if not self.res_dict.has_key(item['name'].decode('utf-8')):
               self.avosManager.saveData('dbmovie',dataDict)
               print '插入数据'
            elif foot_print != self.res_dict[item['name'].decode('utf-8')]:
               self.avosManager.updateDataByName('dbmovie',item['name'],dataDict)
               print '更新数据'
            else:
               print '已存在'
        except:
            print "avos exception!"

        return item

class DzdpPipeline(object):
    def __init__(self):
        self.avosManager = AvosManager()
        #self.res_dict = self.avosManager.getnfdict("dzdp")
        self.res_dict = {}

     #By Hushuying,generate footprint
    def gen_footprint(self,item):
        str_item = str(item['name'])+\
                   str(item['score'])+\
                   str(item['address'])+\
                   str(item['shopname'])
        return self.avosManager.calMD5(str_item)

    def process_item(self, item, spider):
        if spider.name not in ['dzdp']:
            return item

        #init res_dict
        if len(self.res_dict) == 0:
            self.res_dict = self.avosManager.getnfdict("dzdp")

        print item['name']
        dataDict = {"name":item['name'],"shopname":item['shopname'],"score":item['score'],
                    "address":item['address'],
                    "popularity":item['popularity'],
                    "source" : item['source']}

        try:
            foot_print = self.gen_footprint(item)
            dataDict['foot_print'] = foot_print

            if not self.res_dict.has_key(item['name'].decode('utf-8')):
               self.avosManager.saveData('dzdp',dataDict)
               print '插入数据'
            elif foot_print != self.res_dict[item['name'].decode('utf-8')]:
               self.avosManager.updateDataByName('dzdp',item['name'],dataDict)
               print '更新数据'
            else:
               print '已存在'
        except:
            print "avos exception!"

        return item


class WdjPipeline(object):
    def __init__(self):
        self.avosManager = AvosManager()
        #self.res_dict = self.avosManager.getnfdict("appCategory")
        self.res_dict = {}

     #By Hushuying,generate footprint
    def gen_footprint(self,item):
        str_item = str(item['name'])+\
                   str(item['category'])
        return self.avosManager.calMD5(str_item)

    def process_item(self, item, spider):
        if spider.name not in ['wdj']:
            return item

        #init res_dict
        if len(self.res_dict) == 0:
            self.res_dict = self.avosManager.getnfdict("appCategory")

        print item['source']
        dataDict = {"name":item['name'],"category":item['category']}

        try:
            foot_print = self.gen_footprint(item)
            dataDict['foot_print'] = foot_print

            if not self.res_dict.has_key(item['name'].decode('utf-8')):
               self.avosManager.saveData('appCategory',dataDict)
               print '插入数据'
            elif foot_print != self.res_dict[item['name'].decode('utf-8')]:
               self.avosManager.updateDataByName('appCategory',item['name'],dataDict)
               print '更新数据'
            else:
               print '已存在'
        except:
            print "avos exception!"

        return item

class AppStorePipeline(object):
    def __init__(self):
        self.avosManager = AvosManager()
        #self.res_dict = self.avosManager.getnfdict("appstore")
        self.res_dict = {}

     #By Hushuying,generate footprint
    def gen_footprint(self,item):
        str_item = str(item['name'])+\
                   str(item['category'])+\
                   str(item['source'])
        return self.avosManager.calMD5(str_item)

    def process_item(self, item, spider):
        if spider.name not in ['appstore']:
            return item

        if len(self.res_dict) == 0:
            self.res_dict = self.avosManager.getnfdict("appstore")

        print item['name']
        dataDict = {"name":item['name'],"category":item['category'],"source":item['source']}

        try:
            foot_print = self.gen_footprint(item)
            dataDict['foot_print'] = foot_print

            if not self.res_dict.has_key(item['name'].decode('utf-8')):
               self.avosManager.saveData('appstore',dataDict)
               print '插入数据'
            elif foot_print != self.res_dict[item['name'].decode('utf-8')]:
               self.avosManager.updateDataByName('appstore',item['name'],dataDict)
               print '更新数据'
            else:
               print '已存在'
        except:
            print "avos exception!"

        return item


if __name__ == "__main__":
        dp = DbMoviePipeline()
