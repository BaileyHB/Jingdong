# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  csv
import re



class JingdongPipeline(object):



    def process_item(self, item, spider):
        re_text=re.compile(r'>(.*?)<') #正则表达式提取文本
       #-------提取职位描述和职位要求------------------------------------------
        job_description_list = re_text.findall(item['Job_Description'])
        while "" in job_description_list:
            job_description_list.remove('')
        job_description=""
        for i in range(len(job_description_list)):
            job_replace= i.replace('/t','').replace('/n','').replace('/r','')
            job_description +=job_replace.strip()


        job_requirement_list=re_text.findall(item['Job_Requirement'])
        while "" in job_requirement_list:
            job_description_list.remove('')
        job_requirement=""
        for i in job_requirement_list:
            job_replace=i.replace('/t','').replace('/r','').replace('/n','')
            job_requirement +=job_replace.strip()

        #-----提取job_title----------------------------------------------------
        job_title_list=re_text.findall(item['Job_Title'])
        job_title=""
        while "" in job_title_list:
            job_title_list.remove('')
        for i in job_title_list:
            job_replace=i.replace('/t','').replace('/n','').replace('/r','')
            job_title +=job_replace

        #-----工作地点--------------------------------------------------------
        work_place = re_text.findall(item['Work_Place'])
        while "" in work_place:
            work_place.remove('')

        #----行业信息-------------------------------------------------------
        if "京东" in item['Company_Name']:
            item['Company_Type'] = '国内上市公司'
            item['Company_Label'] = '电商'
            item['Company_Size'] = '410万'
            item['Company_Home_Page']='https://www.jd.com/'
            item['Development_Phase'] ='高成长'
        else:
            item['Company_Label']='金融'
            item['Company_Type'] = "京东旗下独立运营"
            item['Company_Size'] = 'Null'
            item['Company_Home_Page'] = 'http://jr.jd.com/'
            item['Development_Phase']  = '高成长'

        with open( 'THUDataPiCrawler_zhaopin_2017_12_12.csv', 'a' ) as f:
            writer = csv.writer( f, dialect='excel' )
            writer.writerow(  [job_title,  # 职位名称
                              item['Job_Label'],  # 职位分类标签
                              item['Department_Name'],  # 部门
                              work_place,  # 工作地点
                              item['Job_Type'],  # 工作性质
                              item['Experience'],  # 经验
                              item['Education'],  # 学历
                              item['Salary'],  # 薪资
                              item['Major'],  # 专业要求
                              item['Number'],  # 招聘人数
                              item['Job_Highlight'],  # 职位诱惑
                              job_description,  # 职位介绍
                              job_requirement,  #职位要求
                              item['Company_Name'],
                              item['Company_Label'],
                              item['Company_Type'],
                              item['Development_Stage'],
                              item['Company_Size'],
                              item['Company_Home_Page'],
                              item['Release_Time'],
                              item['Source_Site'],
                              item['Source_URL']]
                               )
