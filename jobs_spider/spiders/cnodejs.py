# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from jobs_spider.items import JobsSpiderItem


class CnodejsSpider(scrapy.Spider):
    name = 'cnodejs'
    allowed_domains = ['cnodejs.org']
    start_urls = ['https://cnodejs.org/api/v1/topics?tab=job']
    # 获取回复时间在7天以内的职位
    deadline = int(datetime.datetime.now().timestamp()) - 7 * 24 * 60 * 60

    def parse(self, response):
        job_list = json.loads(response.body_as_unicode())['data']
        for info_item in job_list:
            job_item = JobsSpiderItem()
            job_item['title'] = info_item['title']
            # job_item['content'] = info_item['content']
            job_item['origin_url'] = 'https://cnodejs.org/topic/'+info_item['id']
            job_item['last_reply_at'] = int(datetime.datetime.strptime(info_item['last_reply_at'][:10], "%Y-%m-%d").timestamp())
            job_item['create_at'] = int(datetime.datetime.strptime(info_item['create_at'][:10], "%Y-%m-%d").timestamp())


            # if (self.deadline > job_item['create_at'])  and ('深圳' in job_item['title']) and  ('前端' in job_item['title']):
            if (self.deadline > job_item['create_at'])  and ('深圳' in job_item['title']):
                print(job_item)
                # print(job_item['title'], info_item['create_at'][:10])
            else:
                continue

            # yield job_item

