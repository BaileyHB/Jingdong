# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Company_Name = scrapy.Field()       #公司名称：如京东
    Job_Title = scrapy.Field()          # 职位信息：如数据分析师
    Department_Name = scrapy.Field()    #职位所属部门名称：如数据
    Company_Label = scrapy.Field()      #公司领域：如电商
    Company_Type = scrapy.Field()       #公司性质：如私企、外企
    Development_Stage = scrapy.Field()    #公司融资阶段：如：不需要融资
    Company_Size = scrapy.Field()       #公司规模：如150-500
    Company_Home_Page = scrapy.Field()  #公司主页链接：如http://jingdom.com
    Work_Place = scrapy.Field()         #工作地点：如北京
    Salary = scrapy.Field()             #薪水：如15k
    Job_Highlight = scrapy.Field()     #职位诱惑：如：多金
    Job_Type = scrapy.Field()           #工作性质：全职、实习、兼职
    Experience = scrapy.Field()         #经历要求：如经历1-3年
    Education = scrapy.Field()          #学历要求：如本科及本科以上
    Job_Description = scrapy.Field()    #职位描述
    Job_Requirement = scrapy.Field()   #职位要求
    Release_Time = scrapy.Field()       #发布时间：如2017-12-1
    Source_Site = scrapy.Field()        #网站名称：发布职位的招聘
    Source_URL = scrapy.Field()         #发布招聘信息的网站
    Major = scrapy.Field()              #专业要求：如计算机
    Number = scrapy.Field()             #招聘人数：若干人
    Industry = scrapy.Field()           #行业信息




    #pass

