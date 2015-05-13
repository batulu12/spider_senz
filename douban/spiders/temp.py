# -*- coding: utf-8 -*-
__author__ = 'batulu'
from scrapy.contrib.spiders import CrawlSpider,Rule
from bs4 import BeautifulSoup
from scrapy.http import Request
from douban.items import WdjItem
from douban.utils.util_opt import *
from selenium import webdriver



import time


class WdjSpider(CrawlSpider):
    name = 'wdj'

    def __init__(self):
        self.start_urls = []
        self.init_start_url()

    def init_start_url(self):
        software_list = ['影音图像','网上购物','阅读学习','常用工具'
           '性能优化','社交网络','办公软件','通讯聊天'
           '美化手机','便捷生活','出行必用','新闻资讯'
           '金融理财','育儿母婴']

        game_list = ['休闲时间','宝石消除','动作射击','儿童益智'
                    '体育格斗','经营策略','跑酷竞速','网络游戏'
                    '扑克棋牌','塔防守卫','角色扮演']


        for software in software_list:
            url = 'http://www.wandoujia.com/tag/%s'%(software)
            print url
            self.start_urls.append(url)

        for game in game_list:
            url = 'http://www.wandoujia.com/tag/%s'%(game)
            print url
            self.start_urls.append(url)

    def parse(self, response):
        br = webdriver.PhantomJS()
        br.get(response.url)
        print response.url
        time.sleep(2)
        page = 0
        while True:
            link = br.find_element_by_id('j-refresh-btn')
            try:
                link.click()
                time.sleep(2)
                page = page + 1
                #print br.page_source

            except:
                break

            soup=BeautifulSoup(br.page_source)
            temp = soup.find_all(attrs={'class':"last"})
            category = ''
            if len(temp) > 1:
                category = soup.find_all(attrs={'class':"last"})[1].get_text().strip().encode('utf-8')
                print category
            appName_list = soup.find_all(attrs={'class':'name'})
            for appName in appName_list:
                print appName.get_text().strip().encode('utf-8')
                item = WdjItem()
                item['appName'] = appName
                item['category'] = category
                item['source'] = WdjSpider.__name__
                yield item


if __name__ == "__main__":
    br = webdriver.PhantomJS()
    br.get('http://www.wandoujia.com/tag/%E5%BD%B1%E9%9F%B3%E5%9B%BE%E5%83%8F')
    time.sleep(2)
    while True:
        link = br.find_element_by_id('j-refresh-btn')
        try:
            link.click()
            time.sleep(2)
            page = page + 1
            #print br.page_source
            soup=BeautifulSoup(br.page_source)
            temp = soup.find_all(attrs={'class':"last"})
            category = ''
            if len(temp) > 1:
                category = soup.find_all(attrs={'class':"last"})[1].get_text().strip().encode('utf-8')
                print category
            appName_list = soup.find_all(attrs={'class':'name'})
            for appName in appName_list:
                print appName.get_text()

        except:
            break
