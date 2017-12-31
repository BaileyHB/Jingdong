# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl jd_zhaopin -s CLOSEDSPIDER_TIMEOUT=5000 ".split(),
                )