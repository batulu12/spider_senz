#!/bin/sh
PATH=$PATH:/usr/local/bin
export PATH
cd /home/batulu/code/spider/douban
#scrapy crawlall
scrapy crawl douban --set LOG_FILE=log/douban.log
scrapy crawl damai --set LOG_FILE=log/damai.log
