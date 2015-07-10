#!/bin/sh
PATH=$PATH:/usr/local/bin
export PATH
cd /home/batulu/code/spider/douban
#scrapy crawlall
scrapy crawl dbmovie --set LOG_FILE=log/dbmovie.log
