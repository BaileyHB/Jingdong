# -*- coding: utf-8 -*-
import scrapy
import json
from ..items  import JingdongItem
import re

class JdZhaopinSpider(scrapy.Spider):
    name = 'jd_zhaopin'
    allowed_domains = ['zhaopin.jd.com']
    start_urls = [
        'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0', #数据分析师URL
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#数据挖掘工程师URL
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#大数据开发工程师URL
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#机器学习工程师
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E7%25AE%2597%25E6%25B3%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#算法工程师
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E5%25BA%2593%25E7%25AE%25A1%25E7%2590%2586&workPlace=&keyWord=&columnId=2&orderInt=0',#数据库管理工程师
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E5%2595%2586%25E4%25B8%259A%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#商业分析师
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E7%25A7%2591%25E5%25AD%25A6%25E5%25AE%25B6&workPlace=&keyWord=&columnId=2&orderInt=0',#数据科学家
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E9%25A6%2596%25E5%25B8%25AD%25E6%2595%25B0%25E6%258D%25AE%25E5%25AE%2598&workPlace=&keyWord=&columnId=2&orderInt=0',#首席数据官
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E4%25BA%25A7%25E5%2593%2581%25E7%25BB%258F%25E7%2590%2586&workPlace=&keyWord=&columnId=2&orderInt=0',#数据产品经理
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E6%2595%25B0%25E6%258D%25AE%25E8%25BF%2590%25E8%2590%25A5&workPlace=&keyWord=&columnId=2&orderInt=0',#数据运营
         'https://zhaopin.jd.com/JD/web/index/webPosition210!getPostListByConditionShowPic?urlCorpEdition=null&operational=4E3C08B66807E31510372F732AD143ACBA6977970C60F32DE9660076C746DBD740259E04F6BF22F7AF728FEC8DC17A9D9C7863D82C9481DA141E2CD0E776939E3071EB90D4EBEE3A082B4925222A3F54B3CC72A6F155C72A5163A0F618432F94F0ADD8D8184A57CC&positionType=&comPart=&sicCorpCode=&brandCode=1&releaseTime=0&trademark=0&useForm=0&recruitType=2&lanType=&positionName=%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%25E6%259E%25B6%25E6%259E%2584%25E5%25B8%2588&workPlace=&keyWord=&columnId=2&orderInt=0',#大数据架构师
                  ]

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url,callback=self.parse_career_list)
            n=1
            while n<=10:
                try:
                    post_data={'pc.currentPage':n}
                    # FormRequest(url, callback=self.parse_career_list, formdata=post_data)
                    yield scrapy.Request(url=url,callback=self.parse_career_list,method="POST",body=json.dumps(post_data))
                    n=n+1
                except:
                    print('there is no the next_page')

    def parse_career_list(self,response):
        research_list_urls =''.join(scrapy.Selector(response).xpath('//tr/td/a/@href').extract())
        print(research_list_urls)

        #使用post方法，所需查询的职位的页码最多不超过10页
        for url in research_list_urls:
            # m = re.search("javascript:changePage\('(.+)',[0-9],[0=9];\)url")
            # if m:
            #     url = m.group(1)
            #"javascript:changePage('/JD/web/index/webPosition210!
            # getPostListByConditionShowPic?
            # columnId=2&urlCorpEdition=null&operational=DECD39C54422CC4756D9E639A54135D4E3F3495CEAD031A92BADE5CB3F863BBF8176C09F3B4F7DCF336F219056362C8A44900F1FA49C619B26A6EC09FEB26539E01EEB9957CDB87AD3F4C3420D570D6EEC6884B3E1FB5109F050EA734DA47BF9621142CB10AAA0C215557059A4FA5B42'
            # ,6,10);"]
            yield scrapy.Request(url="https://zhaopin.jd.com"+url,callback=self.parse_career_information)


    def  parse_career_information(self,response):
        try:
            item = JingdongItem()
            item['Company_Name'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[1]/span[2]/font/text()').extract())
            print(item['Company_Name'])
            item['Job_Title'] = ''.join(scrapy.Selector(response).xpath('//div[@class="position_title"]/span/text()').extract())
            print(item['job_Title'])
            item['Job_Label'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[6]/span[2]//font/text()').extract())
            print(item['Job_Label'])
            item['Department_Name'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[2]/span[2]/font/text()').extract())
            print(item['Department_Name'])
            item['Number'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[4]/span[2]/text()').extract())
            print(item['Number'])
            item['Work_Place'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[3]/span[2]/span/text()').etract())
            print(item['Work_Place'])
            item['Salary'] = 'Null' #数据缺失
            print(item['Salary'])
            item['Job_Highlight'] = 'Null' #数据缺失
            print(item['Job_Highlight'])
            item['Major'] = "Null" #数据缺失
            print(item['Major'])
            #学历由2部分组成
            Education1 = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[5]/span[2]/text()').extract())
            Education2 = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[5]/span[2]/font/text()').extract())
            item['Education'] = Education2 + Education1
            print(item['Education'])
            item['Job_Description'] =  ''.join(scrapy.Selector(response).xpath('//div[@class="position_content"]/p[2]/text()').extract())
            print(item['Job_Description'])
            item['Job_Requirement'] =  ''.join(scrapy.Selector(response).xpath('').extract())
            print(item['Job_Requirement'])
            item['Release_Time'] = ''.join(scrapy.Selector(response).xpath('//ul[@class="position_basic clear"]/li[7]/span[2]/text()').etract())
            print(item['Release_Time'])
            item['Source_Site'] = '京东招聘'
            print(item['Source_Site'])
            item['Source_URL'] = response.url
            print(item['Source_URL'])
            yield item


        except:
            print('something is wrong')
