# -*- coding: utf-8 -*-

import scrapy

#우리프로젝트의 items.py에 만들어준 [RTItem 클래스] 도 import
from cafe_crawler.items import RTItem

#scrapy에서 제공하는 Spider클래스를 상속한다.
class RTSpider(scrapy.Spider):
    
    # 해당 Spider의 이름. 웹 크롤링 및 스크래핑을 실행할 때 여기서 지정한 이름을 사용함.
    name = "NaverCafe"
    
    #Spider로 하여금 크롤링하도록 허가한 웹 사이트의 도메인 네임.
    allowed_domains= ["section.cafe.naver.com"]
    
    #웹 크롤링의 시작점이 되는 웹 페이지 URL. 해당 웹 페이지에서 출발하여 이어지는 웹 페이지들을 크롤링함
#    start_urls=["https://section.cafe.naver.com/SectionHome.nhn?t=1"]

    
    start_urls=["https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22100%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22101%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22102%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22103%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22104%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22105%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22106%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22107%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22108%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22109%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D",
                "https://section.cafe.naver.com/SectionHome.nhn?t=1#%7B%22search.dirType%22%3A1%2C%22search.dir1Id%22%3A%221%22%2C%22search.dir2Id%22%3A%22110%22%2C%22search.listType%22%3A%22AT%22%2C%22search.sortType%22%3A%222%22%2C%22search.page%22%3A1%7D"
               ]
            
    
    #start_urls의 웹페이지를, spider가 서버에 요청하게 되고, 이에 대한 응답을 reponse라는 변수에 받는데, 이 reponse를 받아 처리하는 parse()함수를 정의
    def parse(self, response):
        #response로 얻어진 웹사이트의 어떤부분을 스크래핑할지 명시해줘야한다
        for li in response.xpath('//*[@id="ListArea"]/li'):
            item = RTItem() #임폴트한 RTItem의 객체 생성
            item["title"] = li.xpath('./h5/a/@title')[0].extract().encode('euc-kr').strip()
            url = li.xpath('./h5/a/@href')[0].extract().strip()
            item["url"] = url
            item["members"] = li.xpath('./dl[2]/dd[1]/text()')[0].extract().strip()
            item["contents"] = li.xpath('./dl[2]/dd[2]/text()')[0].extract().strip()
            item["news"] = li.xpath('./dl[2]/dd[3]/text()')[0].extract().strip()
            
#            yield scrapy.Request(url, callback = self.parse_page_contents)
            
#            def parse_page_contents(self, response):
#                allpage_href=response.xpath('//*[@id="menuLink0"]/@href')[0].extract().strip()
#                allpage_url=response.urljoin(allpage_href)
                
#                yield scrapy.Request(allpage_url, callback = self.parse_allpage_contents)
                
            okCnt=0
#                def parse_allpage_contents(self, response):
#                    for tr in response.xpath('//*[@class="article-board m-tcol-c"]/form/table/tbody/tr'):
#                        sCnt=tr.xpath('./td[5]/text()')[0].extract()
#                        if(sCnt > 100):
#                            okCnt+=1
                            
                    
            item["count"] = okCnt
                    
            yield item    
            
